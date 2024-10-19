# Create codon sequence
codon_dict = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# Create a dictionary of amino_acid:codon
all_amino_acids = list(set(codon_dict.values()))
amino_acid_dict = {}

# Create an empty dictionary of amino_acid:[]
for aa in all_amino_acids:
    amino_acid_dict[aa] = [] # values must be list or else .append will not work

# Add each codon to the amino acid dict
for key,value in codon_dict.items():
    amino_acid_dict[value].append(key)

##################################
# alternative way
amino_acid_dict = {aa: [codon for codon, val in codon_dict.items() if val == aa]
                   for aa in set(codon_dict.values())}
##################################

# Get the lengths of each (you could do this as a dict comp)
len_dict = {}
for aa,codon in amino_acid_dict.items(): # You could have added this to inside the last for loop by just taking the length of the value each time
    len_dict[aa] = len(codon)

# load in protein sequence
with open('rosalind_test.txt') as file:
    seq = file.read().strip()

# Calculate all possible RNA seq
total = 1

for aa in seq:
    total = len_dict[aa] * total

total = total * 3 # because of the stop codon

print(total%1000000)













