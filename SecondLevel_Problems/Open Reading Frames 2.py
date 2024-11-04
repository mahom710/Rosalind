from numpy.ma.core import remainder


def revcomp(seq):
    bp_dict = {'A': 'T', 'T':'A', 'C': 'G', 'G': 'C'}
    return ''.join([bp_dict[bp] for bp in seq[::-1]])

def AllProteins(seq):
    # create all orf
    all_orf_list = []
    for i in range(3):
        orf1= seq[i:]
        orf2 = seq[i:]
        # ensure div by 3
        remainder = -(len(orf1) % 3)
        if remainder != 0:
            all_orf_list.append(orf1[:remainder].replace('T','U'))
            all_orf_list.append(orf2[:remainder].replace('T','U'))
        else:
            all_orf_list.append(orf1[i:].replace('T','U'))
            all_orf_list.append(orf2[i:].replace('T','U'))

    # convert each to protein
    codon_dict = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'X', 'UAG': 'X',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'X', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    aa_list = []

    for orf in all_orf_list:
        temp = []
        for i in range(0,len(orf),3):
            temp.append(codon_dict[orf[i:i+3]])
        aa_list.append(''.join(temp))

    print(aa_list)

    # find all of the proteins
    final_list = []

    for orf in aa_list:
        not_at_end = True
        i = 0
        while not_at_end:
            cur_seq = orf[i:]
            #print(cur_seq)
            start = cur_seq.find('M')

            end = cur_seq.find('X', start)
            print(end)
            #print(start, end)
            if end != -1 and start != -1:
                final_list.append(cur_seq[start:end])
                #print(cur_seq[start:end])
                i = start + 1
                #print(i)
            else:
                not_at_end = False



# test
AllProteins('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
