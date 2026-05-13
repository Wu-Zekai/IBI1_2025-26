import pandas as pd

# 1. Read FASTA files function
def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    sequence = "".join([line.strip() for line in lines if not line.startswith('>')])
    return sequence

# 2. Import BLOSUM62 matrix function
def get_blosum62_matrix():
        from Bio.Align import substitution_matrices
        matrix = substitution_matrices.load("BLOSUM62")
        return matrix

# 3. Alignment function
def align_sequences(name1, seq1, name2, seq2, matrix):
    if len(seq1) != len(seq2):
        raise ValueError("Error: Sequences must be of the same length for this simple alignment.")
    
    score = 0
    identical_count = 0
    length = len(seq1)
    
    # Iterate through each position in the sequences
    for i in range(length):
        res1 = seq1[i]
        res2 = seq2[i]
        
        # Calculate score: look up the score for res1 and res2 in the matrix
        score += matrix[(res1, res2)]
        
        # Check if the residues are identical
        if res1 == res2:
            identical_count += 1
            
    # Calculate percentage identity
    percentage_identity = (identical_count / length) * 100
    
    print(f"\n: {name1} vs {name2}")
    print(f"Sequence 1 length: {len(seq1)}")
    print(f"Sequence 2 length: {len(seq2)}")
    print(f"Percentage Identity: {percentage_identity:.2f}%")
    print(f"Total Score (BLOSUM62): {score}")
    
    return score, percentage_identity

# --- Main execution ---
if __name__ == "__main__":
    matrix = get_blosum62_matrix()
    print("BLOSUM62 matrix loaded successfully.")
    
    if matrix is not None:
        human_seq = read_fasta("P56178_DLX5_HUMAN.fa")
        mouse_seq = read_fasta("P70396_DLX5_MOUSE.fa")
        random_seq = read_fasta("random_sequence.fa")
        
        print("="*40)
        print("Results of Sequence Alignments")
        print("="*40)
        
        # 1. Human vs Mouse
        align_sequences("Human", human_seq, "Mouse", mouse_seq, matrix)
        
        # 2. Human vs Random
        align_sequences("Human", human_seq, "Random", random_seq, matrix)
        
        # 3. Mouse vs Random
        align_sequences("Mouse", mouse_seq, "Random", random_seq, matrix)