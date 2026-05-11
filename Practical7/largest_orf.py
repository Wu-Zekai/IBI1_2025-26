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


