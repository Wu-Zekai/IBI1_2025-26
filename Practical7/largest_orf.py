# PSEUDOCODE:
# 1. Import the regular expression (re) library to handle pattern matching.
# 2. Define the mRNA sequence as a string variable 'seq'.
# 3. Define a regex pattern to identify in-frame Open Reading Frames (ORFs):
#    - Must start with 'AUG'.
#    - Followed by zero or more groups of 3 nucleotides (triplets).
#    - Must end with a stop codon ('UAA', 'UAG', or 'UGA').
# 4. Use re.findall to extract all matching ORFs from the sequence into a list.
# 5. Check if the list of ORFs is not empty:
#    - If found, identify the longest ORF using the max function with key=len.
#    - Print the longest ORF and its character count (length).
# 6. If no ORF is found:
#    - Print a message stating no valid ORF exists and report length as 0.

import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
regex_pattern = r'AUG(?:...)*?(?:UAA|UAG|UGA)'

orfs = re.findall(regex_pattern, seq)

if orfs:
    longest_orf = max(orfs, key=len)
    print('The longest ORF is:', longest_orf)
    print('The length of the longest ORF is:', len(longest_orf))
else:
    print('No valid ORF was found in the sequence.')
    print('The length of the longest ORF is: 0')


