# PSEUDOCODE:
# 1. Define function 'predict_protein_mass' taking a string 'sequence' as input.
# 2. Define a weight table (dictionary) for all valid amino acids.
# 3. Set total_mass starting point to 0.0.
# 4. Loop through each amino acid in the provided sequence.
# 5. Check if the current amino acid is in the weight table:
#    - If yes: Add the weight to the running total.
#    - If no: Stop and return an error message mentioning the invalid residue.
# 6. After the loop, return the final calculated total_mass.
# 7. Provide example calls to test the function's logic.

def predict_protein_mass(sequence):
    """
    Calculate the total mass of a protein based on its amino acid sequence.
    Returns the mass in amu, or an error message if an unknown amino acid is found.
    """
    # The dictionary to store the molecular weights of the 20 standard amino acids
    amino_acid_weights = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }

    total_mass = 0.0
    
    # Iterate through each amino acid in the sequence
    for aa in sequence.upper(): # .upper() ensures it works with lowercase inputs too
        if aa in amino_acid_weights:
            total_mass += amino_acid_weights[aa]
        else:
            return f"Error: Amino acid '{aa}' is not recorded in the table."
    
    return total_mass


# Example 1: Valid input sequence
example_seq = "GAS"
mass = predict_protein_mass(example_seq)
print(f"Input: {example_seq} -> Output: {mass}")

# Example 2: Invalid input sequence with an unknown amino acid ('Z')
error_seq = "GAZ"
error_msg = predict_protein_mass(error_seq)
print(f"Input: {error_seq} -> Output: {error_msg}")