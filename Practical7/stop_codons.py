def find_in_frame_stops(sequence):
    """
    Scans a sequence 3 nucleotides at a time starting from index 0.
    Returns a list of stop codons found in-frame.
    """
    stop_codons = ['TAA', 'TAG', 'TGA']
    found_in_sequence = []
    
    # Iterate through the sequence in steps of 3
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in stop_codons:
            found_in_sequence.append(codon)
            
    return found_in_sequence

def process_genes(input_file, output_file):
    genes_processed = 0
    genes_with_stops = 0

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        header = None
        sequence_parts = []

        # We use a loop to handle the multi-line FASTA format
        for line in f_in:
            line = line.strip()
            if not line:
                continue

            if line.startswith('>'):
                # Process the PREVIOUS gene before starting the new one
                if header:
                    full_seq = "".join(sequence_parts).upper()
                    # Only process if it starts with ATG as per instructions
                    if full_seq.startswith('ATG'):
                        stops = find_in_frame_stops(full_seq)
                        if stops:
                            # Extract gene name (first word after '>')
                            gene_name = header.split()[0].replace('>', '')
                            # Create new header with found stops
                            stop_list_str = " ".join(set(stops)) # set() gets unique types
                            f_out.write(f">{gene_name} {stop_list_str}\n")
                            f_out.write(f"{full_seq}\n")
                            genes_with_stops += 1

                # Reset for the new gene
                header = line
                sequence_parts = []
                genes_processed += 1
            else:
                sequence_parts.append(line)

        # Handle the very last gene in the file
        if header:
            full_seq = "".join(sequence_parts).upper()
            if full_seq.startswith('ATG'):
                stops = find_in_frame_stops(full_seq)
                if stops:
                    gene_name = header.split()[0].replace('>', '')
                    stop_list_str = " ".join(set(stops))
                    f_out.write(f">{gene_name} {stop_list_str}\n")
                    f_out.write(f"{full_seq}\n")
                    genes_with_stops += 1

    print(f"Processing complete.")
    print(f"Total genes analyzed: {genes_processed}")
    print(f"Genes written to {output_file}: {genes_with_stops}")

if __name__ == "__main__":
    # Ensure the input filename matches your downloaded file
    input_filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_filename = "stop_genes.fa"
    
    try:
        process_genes(input_filename, output_filename)
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")