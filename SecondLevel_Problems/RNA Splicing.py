
def ReadFasta(file_path):
    # create empty list
    id_list = []
    seq_list = []
    # Start with empty seq
    seq = ''

    # read in lines
    with open(file_path, 'r') as file:
        for line in file:
            # strip line
            line = line.strip()
            # append the id
            if line[0] == '>':
                id_list.append(line[1:])
                if seq: # edge case of start
                    seq_list.append(seq)
                    seq = ''
            else: # create the seq
                seq = seq + line
        # append the final seq
        seq_list.append(seq)
        # return the lists
        return id_list, seq_list

def RemoveIntrons(mRNA,introns_list):
    # for each intron
    for intron in introns_list:
        index = 0
        # find and remove every intron
        while index != -1:
            index = mRNA.find(intron)
            if index != -1:
                mRNA = mRNA[0:index] + mRNA[index+len(intron):]
    return mRNA

def RNA2Protein(seq):
    codon_dict = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # create a new dictionary for DNA (not RNA)
    dna_dict = {(codon.replace('U','T')): aa for codon, aa in codon_dict.items()}

    # empty aa seq
    aa_seq = []

    # convert to aa
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        aa_seq.append(dna_dict[codon])

    return ''.join(aa_seq)


# Run it all together
id_list, seq_list = ReadFasta('rosalind_test.txt')
print(RNA2Protein(RemoveIntrons(seq_list[0], seq_list[1:])))















