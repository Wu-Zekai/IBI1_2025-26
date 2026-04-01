import matplotlib.pyplot as plt # type: ignore
from collections import Counter

def get_user_input():
    """Ask the user to input a valid stop codon and return it."""
    valid_stops = ['TAA', 'TAG', 'TGA']
    while True:
        user_choice = input("Please enter a valid stop codon (TAA, TAG, TGA): ").strip().upper()
        if user_choice in valid_stops:
            return user_choice
        print(f"Invalid input! Please ensure you enter one of {valid_stops}.")

def get_upstream_codons(sequence, target_stop):
    """
    recognize the longest ORF upstream of the specified target_stop codon in the given sequence.
    longest ORF is determined by the last occurrence of the target_stop codon in the sequence.
    """
    # catonize the sequence into codons (triplets)
    # ensure we only consider complete codons, hence the -2 in the range
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]
    
    # find all indices where the target_stop codon appears
    indices = [i for i, codon in enumerate(codons) if codon == target_stop]
    
    if not indices:
        return [] # if the target stop codon is not found, return an empty list
    
    # consider the longest ORF as the one that ends at the last occurrence of the target stop codon
    longest_stop_idx = max(indices)
    
    # return all codons upstream of the longest stop codon (not including the stop codon itself)
    return codons[:longest_stop_idx]

def process_fasta_and_count(filename, target_stop):
    """Read the file and summarize the codon counts for all matching genes"""
    total_counts = Counter()
    
    with open(filename, 'r') as f:
        header = None
        sequence_parts = []
        
        for line in f:
            line = line.strip()
            if not line: continue
            
            if line.startswith('>'):
                if header:
                    full_seq = "".join(sequence_parts).upper()
                    # check if the sequence starts with ATG as per instructions
                    if full_seq.startswith('ATG'):
                        upstream = get_upstream_codons(full_seq, target_stop)
                        total_counts.update(upstream)
                
                header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)
        
        # the last gene in the file also needs to be processed
        if header:
            full_seq = "".join(sequence_parts).upper()
            if full_seq.startswith('ATG'):
                upstream = get_upstream_codons(full_seq, target_stop)
                total_counts.update(upstream)
                
    return total_counts

def create_visual_report(counts, target_stop):
    """pie chart of codon distribution and save the report as an image file"""
    if not counts:
        print("Do not have any codon data to visualize. Exiting.")
        return

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_items]
    sizes = [item[1] for item in sorted_items]

    plt.figure(figsize=(12, 12))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 7})
    plt.title(f"Codon Distribution Upstream of {target_stop} (Longest ORF)")
    
    # Save the figure to a file
    output_file = f"codon_dist_{target_stop}.png"
    plt.savefig(output_file)
    print(f"\nthe report is done")
    print(f" the pie chart is saved as {output_file}")

if __name__ == "__main__":
    FILENAME = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    
    # Step1: Get user input for the stop codon
    chosen_stop = get_user_input()
    
    # Step2: Process the FASTA file and count codons upstream of the longest ORF ending with the chosen stop codon
    print(f"Scanning file and counting codons upstream of the longest ORF ending with {chosen_stop}...")
    codon_stats = process_fasta_and_count(FILENAME, chosen_stop)
    
    # print the top 10 most common codons and their counts
    print(f"\nthe top 10 most common codons upstream of the longest ORF ending with {chosen_stop} are:")
    for codon, count in codon_stats.most_common(10):
        print(f"{codon}: {count}")
    
    # Step3: Create and save the visualization
    create_visual_report(codon_stats, chosen_stop)