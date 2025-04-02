from pathlib import Path
from typing import Union, Dict, List, Tuple, Optional
import logging
import pandas as pd
from Bio import SeqIO
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
import multiprocessing
import click

from .processor import AmpliconProcessor

logger = logging.getLogger(__name__)

def process_samples(
    fastq_dir: Union[str, Path],
    reference: Union[str, Path],
    output_dir: Union[str, Path, None] = None,
    threads: int = 4,
    min_base_quality: int = 20,
    min_mapping_quality: int = 30,
    min_read_count: int = 10,
    max_file_size: int = 10_000_000_000,
    bed_path: Union[str, Path, None] = None,
    max_indel_size: int = 50,
    parallel_samples: int = None
) -> Tuple[Dict[str, pd.DataFrame], AmpliconProcessor]:
    """
    Process all samples in a directory.

    Args:
        fastq_dir: Directory containing FASTQ files
        reference: Path to reference FASTA file
        output_dir: Directory for output files (default: fastq_dir/results)
        threads: Number of threads to use per sample
        min_base_quality: Minimum base quality score
        min_mapping_quality: Minimum mapping quality score
        min_read_count: Minimum number of reads to consider a haplotype
        max_file_size: Maximum file size in bytes
        bed_path: Optional path to BED file for indel comparison
        max_indel_size: Maximum size of indels to consider as small indels
        parallel_samples: Number of samples to process in parallel (default: min(4, CPU count))

    Returns:
        Tuple of (Dictionary mapping sample names to their results DataFrames, AmpliconProcessor)
    """
    fastq_dir = Path(fastq_dir)
    reference = Path(reference)
    output_dir = Path(output_dir) if output_dir else fastq_dir / 'results'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Set parallel processing parameters
    if parallel_samples is None:
        parallel_samples = min(4, multiprocessing.cpu_count())
    
    # Adjust threads per sample based on parallel processing
    threads_per_sample = max(1, threads // parallel_samples)

    # Initialize processor
    processor = AmpliconProcessor(
        reference_path=reference,
        bed_path=bed_path,
        min_base_quality=min_base_quality,
        min_mapping_quality=min_mapping_quality,
        min_read_count=min_read_count,
        max_file_size=max_file_size,
        max_indel_size=max_indel_size
    )

    def process_single_sample(r1_file: Path, processor: AmpliconProcessor) -> Tuple[str, pd.DataFrame]:
        """Process a single sample and return its name and results."""
        try:
            r2_file = r1_file.parent / r1_file.name.replace('_R1_', '_R2_')
            if not r2_file.exists():
                logger.warning(f"No R2 file found for {r1_file.name}")
                return None

            sample_name = r1_file.name.split('_R1_')[0]
            logger.info(f"Processing sample: {sample_name}")

            result = processor.process_sample(
                fastq_r1=r1_file,
                fastq_r2=r2_file,
                output_dir=output_dir / sample_name,
                threads=threads_per_sample
            )
            return sample_name, result

        except Exception as e:
            logger.error(f"Error processing sample {r1_file.stem}: {str(e)}")
            return None

    # Get list of R1 files
    r1_files = sorted(fastq_dir.glob('*_R1_001.fastq*'))
    
    # Process samples in parallel
    results = {}
    with ThreadPoolExecutor(max_workers=parallel_samples) as executor:
        # Create futures for each sample
        future_to_sample = {
            executor.submit(process_single_sample, r1_file, processor): r1_file
            for r1_file in r1_files
        }

        # Process results as they complete
        with click.progressbar(length=len(r1_files), 
                             label='Processing samples') as bar:
            for future in as_completed(future_to_sample):
                result = future.result()
                if result is not None:
                    sample_name, df = result
                    results[sample_name] = df
                bar.update(1)

    return results, processor

def summarize_results(results: Dict[str, pd.DataFrame], processor: Optional['AmpliconProcessor'] = None) -> pd.DataFrame:
    """Create a summary of results across all samples."""
    if not results:
        return pd.DataFrame()
        
    summaries = []
    # Store all data for overall statistics
    all_data = []
    
    for sample, df in results.items():
        if df.empty:
            continue
            
        try:
            total_reads = df['count'].sum()
            
            # Calculate per-reference statistics
            ref_stats = []
            for ref in df['reference'].unique():
                ref_df = df[df['reference'] == ref]
                ref_reads = ref_df['count'].sum()
                
                # Get reference sequence
                ref_seq = processor.reference[ref] if processor else None
                
                # Get theoretical maximum SNPs for this reference
                theoretical_max_snps = ref_df['theoretical_max_snps'].iloc[0]
                
                # Count unique single SNP haplotypes
                single_snp_haplotypes = ref_df[ref_df['snp_count'] == 1]
                unique_snp_positions = set()
                
                # Only count SNPs from haplotypes with exactly one SNP
                for _, row in single_snp_haplotypes.iterrows():
                    haplotype = row['haplotype']
                    for pos, (ref, var) in enumerate(zip(ref_seq, haplotype)):
                        if var.islower() and ref != var.upper():
                            unique_snp_positions.add(pos + 1)
                
                unique_single_snp_count = len(unique_snp_positions)
                
                # Add warning if we exceed theoretical maximum
                if unique_single_snp_count > theoretical_max_snps:
                    logger.warning(f"Sample {sample} reference {ref} has more unique single SNP positions "
                                 f"than theoretically possible: found={unique_single_snp_count}, "
                                 f"max={theoretical_max_snps}")
                
                ref_stats.append({
                    'reference': ref,
                    'reads': ref_reads,
                    'unique_haplotypes': len(ref_df),
                    'unique_single_mut_haplotypes': len(ref_df[ref_df['mutations'] == 1]),
                    'unique_single_snp_haplotypes': unique_single_snp_count,
                    'unique_single_indel_haplotypes': len(ref_df[ref_df['indel_count'] == 1]),
                    'max_frequency': ref_df['frequency'].max(),
                    'avg_mutations': (ref_df['mutations'] * ref_df['count']).sum() / ref_reads if ref_reads > 0 else 0,
                    'avg_snps': (ref_df['snp_count'] * ref_df['count']).sum() / ref_reads if ref_reads > 0 else 0,
                    'avg_indels': (ref_df['indel_count'] * ref_df['count']).sum() / ref_reads if ref_reads > 0 else 0,
                    'full_length_reads': ref_df[ref_df['is_full_length']]['count'].sum(),
                    'full_length_percent': (ref_df[ref_df['is_full_length']]['count'].sum() / ref_reads * 100) if ref_reads > 0 else 0,
                    'theoretical_max_snps': theoretical_max_snps
                })
            
            # Create sample summary
            summary = {
                'sample': sample,
                'total_reads': total_reads,
                'unique_haplotypes': len(df),
                'unique_single_mut_haplotypes': len(df[df['mutations'] == 1]),
                'unique_single_snp_haplotypes': len(df[df['snp_count'] == 1]),
                'unique_single_indel_haplotypes': len(df[df['indel_count'] == 1]),
                'max_frequency': df['frequency'].max(),
                'avg_mutations': (df['mutations'] * df['count']).sum() / total_reads if total_reads > 0 else 0,
                'avg_snps': (df['snp_count'] * df['count']).sum() / total_reads if total_reads > 0 else 0,
                'avg_indels': (df['indel_count'] * df['count']).sum() / total_reads if total_reads > 0 else 0,
                'full_length_reads': df[df['is_full_length']]['count'].sum(),
                'full_length_percent': (df[df['is_full_length']]['count'].sum() / total_reads * 100) if total_reads > 0 else 0,
                'num_references': len(df['reference'].unique())
            }
            
            # Add single mutation stats if available
            if 'single_mutations' in df.columns:
                single_mut_reads = df[df['mutations'] == 1]['count'].sum()
                summary.update({
                    'single_mutation_reads': single_mut_reads,
                    'single_mutation_percent': (single_mut_reads / total_reads * 100) if total_reads > 0 else 0
                })
            
            summaries.append(summary)
            all_data.append(df)
            
            # Add reference-specific statistics
            for ref_stat in ref_stats:
                ref_summary = {
                    'sample': f"{sample}_{ref_stat['reference']}",
                    'total_reads': ref_stat['reads'],
                    'unique_haplotypes': ref_stat['unique_haplotypes'],
                    'unique_single_mut_haplotypes': ref_stat['unique_single_mut_haplotypes'],
                    'unique_single_snp_haplotypes': ref_stat['unique_single_snp_haplotypes'],
                    'unique_single_indel_haplotypes': ref_stat['unique_single_indel_haplotypes'],
                    'max_frequency': ref_stat['max_frequency'],
                    'avg_mutations': ref_stat['avg_mutations'],
                    'avg_snps': ref_stat['avg_snps'],
                    'avg_indels': ref_stat['avg_indels'],
                    'full_length_reads': ref_stat['full_length_reads'],
                    'full_length_percent': ref_stat['full_length_percent'],
                    'num_references': 1,
                    'theoretical_max_snps': ref_stat['theoretical_max_snps']
                }
                if 'single_mutations' in df.columns:
                    ref_single_mut_reads = df[(df['reference'] == ref_stat['reference']) & (df['mutations'] == 1)]['count'].sum()
                    ref_summary.update({
                        'single_mutation_reads': ref_single_mut_reads,
                        'single_mutation_percent': (ref_single_mut_reads / ref_stat['reads'] * 100) if ref_stat['reads'] > 0 else 0
                    })
                summaries.append(ref_summary)
                
        except Exception as e:
            logger.error(f"Error summarizing results for {sample}: {str(e)}")
            continue
    
    # Create per-sample summary DataFrame
    summary_df = pd.DataFrame(summaries)
    
    # Calculate overall statistics if we have data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        total_reads = combined_df['count'].sum()
        
        # Calculate per-reference overall statistics
        ref_overall_stats = []
        for ref in combined_df['reference'].unique():
            ref_df = combined_df[combined_df['reference'] == ref]
            ref_reads = ref_df['count'].sum()
            
            # Get reference sequence
            ref_seq = processor.reference[ref] if processor else None
            
            # Get theoretical maximum SNPs for this reference
            theoretical_max_snps = ref_df['theoretical_max_snps'].iloc[0]
            
            # Count unique single SNP haplotypes
            single_snp_haplotypes = ref_df[ref_df['snp_count'] == 1]
            unique_snp_positions = set()
            
            # Only count SNPs from haplotypes with exactly one SNP
            for _, row in single_snp_haplotypes.iterrows():
                haplotype = row['haplotype']
                for pos, (ref, var) in enumerate(zip(ref_seq, haplotype)):
                    if var.islower() and ref != var.upper():
                        unique_snp_positions.add(pos + 1)
            
            unique_single_snp_count = len(unique_snp_positions)
            
            # Add warning if we exceed theoretical maximum
            if unique_single_snp_count > theoretical_max_snps:
                logger.warning(f"Overall results for reference {ref} have more unique single SNP positions "
                             f"than theoretically possible: found={unique_single_snp_count}, "
                             f"max={theoretical_max_snps}")
            
            ref_overall_stats.append({
                'reference': ref,
                'reads': ref_reads,
                'unique_haplotypes': len(ref_df),
                'unique_single_mut_haplotypes': len(ref_df[ref_df['mutations'] == 1]),
                'unique_single_snp_haplotypes': unique_single_snp_count,
                'unique_single_indel_haplotypes': len(ref_df[ref_df['indel_count'] == 1]),
                'max_frequency': ref_df['frequency'].max(),
                'avg_mutations': (ref_df['mutations'] * ref_df['count']).sum() / ref_reads if ref_reads > 0 else 0,
                'avg_snps': (ref_df['snp_count'] * ref_df['count']).sum() / ref_reads if ref_reads > 0 else 0,
                'avg_indels': (ref_df['indel_count'] * ref_df['count']).sum() / ref_reads if ref_reads > 0 else 0,
                'full_length_reads': ref_df[ref_df['is_full_length']]['count'].sum(),
                'full_length_percent': (ref_df[ref_df['is_full_length']]['count'].sum() / ref_reads * 100) if ref_reads > 0 else 0,
                'theoretical_max_snps': theoretical_max_snps
            })
        
        # Create overall summary
        overall_summary = {
            'sample': 'OVERALL',
            'total_reads': total_reads,
            'unique_haplotypes': len(combined_df),
            'unique_single_mut_haplotypes': len(combined_df[combined_df['mutations'] == 1]),
            'unique_single_snp_haplotypes': len(combined_df[combined_df['snp_count'] == 1]),
            'unique_single_indel_haplotypes': len(combined_df[combined_df['indel_count'] == 1]),
            'max_frequency': combined_df['frequency'].max(),
            'avg_mutations': (combined_df['mutations'] * combined_df['count']).sum() / total_reads if total_reads > 0 else 0,
            'avg_snps': (combined_df['snp_count'] * combined_df['count']).sum() / total_reads if total_reads > 0 else 0,
            'avg_indels': (combined_df['indel_count'] * combined_df['count']).sum() / total_reads if total_reads > 0 else 0,
            'full_length_reads': combined_df[combined_df['is_full_length']]['count'].sum(),
            'full_length_percent': (combined_df[combined_df['is_full_length']]['count'].sum() / total_reads * 100) if total_reads > 0 else 0,
            'num_references': len(combined_df['reference'].unique())
        }
        
        # Add single mutation stats if available
        if 'single_mutations' in combined_df.columns:
            single_mut_reads = combined_df[combined_df['mutations'] == 1]['count'].sum()
            overall_summary.update({
                'single_mutation_reads': single_mut_reads,
                'single_mutation_percent': (single_mut_reads / total_reads * 100) if total_reads > 0 else 0
            })
        
        # Add overall summary as the first row
        summary_df = pd.concat([pd.DataFrame([overall_summary]), summary_df], ignore_index=True)
        
        # Add reference-specific overall statistics
        for ref_stat in ref_overall_stats:
            ref_overall_summary = {
                'sample': f"OVERALL_{ref_stat['reference']}",
                'total_reads': ref_stat['reads'],
                'unique_haplotypes': ref_stat['unique_haplotypes'],
                'unique_single_mut_haplotypes': ref_stat['unique_single_mut_haplotypes'],
                'unique_single_snp_haplotypes': ref_stat['unique_single_snp_haplotypes'],
                'unique_single_indel_haplotypes': ref_stat['unique_single_indel_haplotypes'],
                'max_frequency': ref_stat['max_frequency'],
                'avg_mutations': ref_stat['avg_mutations'],
                'avg_snps': ref_stat['avg_snps'],
                'avg_indels': ref_stat['avg_indels'],
                'full_length_reads': ref_stat['full_length_reads'],
                'full_length_percent': ref_stat['full_length_percent'],
                'num_references': 1,
                'theoretical_max_snps': ref_stat['theoretical_max_snps']
            }
            if 'single_mutations' in combined_df.columns:
                ref_single_mut_reads = combined_df[(combined_df['reference'] == ref_stat['reference']) & (combined_df['mutations'] == 1)]['count'].sum()
                ref_overall_summary.update({
                    'single_mutation_reads': ref_single_mut_reads,
                    'single_mutation_percent': (ref_single_mut_reads / ref_stat['reads'] * 100) if ref_stat['reads'] > 0 else 0
                })
            summary_df = pd.concat([pd.DataFrame([ref_overall_summary]), summary_df], ignore_index=True)
    
    # Format numeric columns
    if not summary_df.empty:
        # Round percentages to 2 decimal places
        for col in ['max_frequency', 'full_length_percent', 'single_mutation_percent']:
            if col in summary_df.columns:
                summary_df[col] = summary_df[col].round(2)
        
        # Round average mutations to 2 decimal places
        if 'avg_mutations' in summary_df.columns:
            summary_df['avg_mutations'] = summary_df['avg_mutations'].round(2)
    
    return summary_df

def validate_input(
    fastq_dir: Union[str, Path],
    reference: Union[str, Path]
) -> List[str]:
    """
    Validate input files and return any warnings.

    Args:
        fastq_dir: Directory containing FASTQ files
        reference: Path to reference FASTA file

    Returns:
        List of warning messages, empty if all valid
    """
    warnings = []
    
    # Check reference file
    ref_path = Path(reference)
    if not ref_path.exists():
        warnings.append(f"Reference file not found: {ref_path}")
    elif ref_path.stat().st_size == 0:
        warnings.append(f"Reference file is empty: {ref_path}")
    else:
        # Validate FASTA format
        try:
            with open(ref_path) as handle:
                records = list(SeqIO.parse(handle, "fasta"))
                if not records:
                    warnings.append(f"No valid FASTA sequences found in: {ref_path}")
        except Exception as e:
            warnings.append(f"Error reading reference file: {str(e)}")

    # Check BWA index files
    for ext in ['.amb', '.ann', '.bwt', '.pac', '.sa']:
        if not (ref_path.parent / (ref_path.name + ext)).exists():
            warnings.append(f"BWA index file missing: {ref_path}{ext}")

    # Check required executables
    for cmd in ['bwa', 'samtools']:
        if not shutil.which(cmd):
            warnings.append(f"Required program not found: {cmd}")

    # Check FASTQ directory
    fastq_dir = Path(fastq_dir)
    if not fastq_dir.is_dir():
        warnings.append(f"FASTQ directory not found: {fastq_dir}")
    else:
        # Look for both .fastq and .fastq.gz files
        r1_files = list(fastq_dir.glob('*_R1_001.fastq*'))
        if not r1_files:
            warnings.append(f"No R1 FASTQ files found in: {fastq_dir}")
        
        # Check for matching R2 files
        for r1 in r1_files:
            r2 = r1.parent / r1.name.replace('_R1_', '_R2_')
            if not r2.exists():
                warnings.append(f"No matching R2 file for: {r1.name}")
            
            # Check file sizes
            try:
                if r1.stat().st_size == 0:
                    warnings.append(f"Empty R1 file: {r1.name}")
                if r2.exists() and r2.stat().st_size == 0:
                    warnings.append(f"Empty R2 file: {r2.name}")
            except Exception as e:
                warnings.append(f"Error checking file sizes: {str(e)}")

    return warnings

def load_results(results_dir: Union[str, Path]) -> Dict[str, pd.DataFrame]:
    """Load previously generated results from CSV files."""
    results_dir = Path(results_dir)
    results = {}
    
    try:
        # Look for results in sample subdirectories
        for csv_file in results_dir.rglob('*_haplotypes.csv'):
            sample_name = csv_file.name.replace('_haplotypes.csv', '')
            try:
                df = pd.read_csv(csv_file)
                
                # Ensure required columns are present
                required_cols = ['reference', 'haplotype', 'count', 'frequency', 'mutations']
                missing_cols = [col for col in required_cols if col not in df.columns]
                
                if missing_cols:
                    logger.warning(f"Results file {csv_file} missing columns: {missing_cols}")
                    continue
                    
                results[sample_name] = df
                logger.debug(f"Loaded results for sample: {sample_name}")
                
            except Exception as e:
                logger.error(f"Error loading results for {sample_name}: {str(e)}")
                continue
    except Exception as e:
        logger.error(f"Error scanning results directory: {str(e)}")
    
    return results