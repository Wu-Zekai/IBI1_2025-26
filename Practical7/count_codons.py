# PSEUDOCODE:
# 1. Define a function 'get_user_input' to:
#    - Prompt the user to enter a stop codon (TAA, TAG, or TGA).
#    - Use a while loop to ensure the input is valid and case-insensitive.
# 2. Define a function 'get_upstream_codons' to identify the longest ORF:
#    - Locate the first 'ATG' in the sequence as the start index.
#    - Extract the coding sequence and split it into triplets (codons).
#    - Find all positions where the user-specified stop codon occurs in-frame.
#    - Identify the LAST occurrence of that stop codon to ensure the longest ORF.
#    - Return all codons located upstream of this specific stop codon.
# 3. Define a function 'process_fasta_and_count':
#    - Initialize a Counter object to aggregate codon frequencies.
#    - Open the FASTA file and parse it line by line (handling multi-line sequences).
#    - For each gene, call 'get_upstream_codons' and update the global Counter.
# 4. Define a function 'create_visual_report':
#    - Sort the codon counts in descending order for better visualization.
#    - Create a large, high-resolution pie chart using matplotlib.
#    - Include labels, percentages (autopct), and a title.
#    - Save the plot as a .png file named after the chosen stop codon.
# 5. In the MAIN section:
#    - Execute the steps: Get input -> Process data -> Print Top 10 to console -> Save Chart.

import matplotlib.pyplot as plt 
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

    start_idx = sequence.find('ATG')
    if start_idx == -1:
        return[]
    
    coding_seq = sequence[start_idx:]
    
    codons = [coding_seq[i:i+3] for i in range(0, len(coding_seq) - 2, 3)]
    
    indices =[i for i, codon in enumerate(codons) if codon == target_stop]
    
    if not indices:
        return[] 
    longest_stop_idx = max(indices)
    return codons[:longest_stop_idx]

def process_fasta_and_count(filename, target_stop):
    """Read the file and summarize the codon counts for all matching genes"""
    total_counts = Counter()
    
    with open(filename, 'r') as f:
        header = None
        sequence_parts =[]
        
        for line in f:
            line = line.strip()
            if not line: continue
            
            if line.startswith('>'):
                if header:
                    full_seq = "".join(sequence_parts).upper()
                    upstream = get_upstream_codons(full_seq, target_stop)
                    if upstream:
                        total_counts.update(upstream)
                
                header = line
                sequence_parts =[]
            else:
                sequence_parts.append(line)
        
        if header:
            full_seq = "".join(sequence_parts).upper()
            upstream = get_upstream_codons(full_seq, target_stop)
            if upstream:
                total_counts.update(upstream)
                
    return total_counts

def create_visual_report(counts, target_stop):
    """Pie chart of codon distribution and save the report as an image file"""
    if not counts:
        print("Do not have any codon data to visualize. Exiting.")
        return

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_items]
    sizes =[item[1] for item in sorted_items]

    plt.figure(figsize=(15, 15)) 
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 6}, pctdistance=0.85)
    
    plt.title(f"Codon Distribution Upstream of {target_stop} (Longest ORF)", fontsize=16)
    
    output_file = f"codon_dist_{target_stop}.png"
    plt.savefig(output_file, bbox_inches='tight', dpi=300) 
    print(f"\nThe report is done")
    print(f"The pie chart is saved as {output_file}")

if __name__ == "__main__":
    FILENAME = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    
    # Step 1: Get user input
    chosen_stop = get_user_input()
    
    # Step 2: Process FASTA and count
    print(f"Scanning file and counting codons upstream of the longest ORF ending with {chosen_stop}...")
    codon_stats = process_fasta_and_count(FILENAME, chosen_stop)
    
    # Step 3: Print summary to console
    print(f"\nThe top 10 most common codons upstream of the longest ORF ending with {chosen_stop} are:")
    for codon, count in codon_stats.most_common(10):
        print(f"{codon}: {count}")
    
    # Step 4: Visual Report
    create_visual_report(codon_stats, chosen_stop)