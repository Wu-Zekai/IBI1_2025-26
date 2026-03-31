import re 
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
orfs=re.findall(r'AUG(?:...)*?UAA|AUG(?:...)*?UAG|AUG(?:...)*?UGA', seq)
longest_orf = max(orfs, key=len)
print('The longest ORF is:', longest_orf)
print('The length of the longest ORF is:', len(longest_orf))


