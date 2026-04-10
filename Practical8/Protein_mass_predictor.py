class ProteinMassPredictor:
    """
    The class to predict the mass of a protein.
    """
    def __init__(self):
        # The dictionary to store the molecular weights of the 20 standard amino acids
        self.amino_acid_weights = {
            'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
            'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
            'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
            'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
            'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
        }

    def predict_mass(self, sequence):
        """
        Calculate the total mass of a protein.
        """
        total_mass = 0.0
        
        # Iterate through each amino acid in the sequence
        for aa in sequence.upper():
            if aa in self.amino_acid_weights:
                total_mass += self.amino_acid_weights[aa]
            else:
                # If an unknown amino acid is found, return an error message
                return f"Error: Amino acid '{aa}' is not recorded in the table."
        
        # Return the final total mass
        return total_mass

predictor = ProteinMassPredictor()

# Example 1: Valid input sequence
example_seq = "GAS"
mass = predictor.predict_mass(example_seq)
print(f"Input: {example_seq} -> Output: {mass}")

# Example 2: Invalid input sequence with an unknown amino acid
error_seq = "GAZ"
error_msg = predictor.predict_mass(error_seq)
print(f"Input: {error_seq} -> Output: {error_msg}")