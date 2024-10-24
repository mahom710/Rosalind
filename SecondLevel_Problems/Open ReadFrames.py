def ORF(seq):
    # obtain the correct coding RNA seq
    coding_RNA = seq.replace('T','U')

    # obtain the reverse comp
    rc_RNA = ''
    for bp in coding_RNA:
        # get the compliment
        if bp == 'A':
            bp = 'U'
        elif bp == 'U':
            bp = 'A'
        elif bp == 'C':
            bp = 'G'
        elif bp == 'G':
            bp = 'C'
            # reverse
        rc_RNA = bp + rc_RNA

    # create function to convert sequences to protein with varying orf
    def protein(seq):
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

        # convert from codon to protein
        aa_list = []
        for i in range(0,len(seq),3):
            # accounting for if the last bit of the sequence is not a codon (not 3 bp long)
            if i+3 <= len(seq):
                aa_list.append(codon_dict[seq[i:i+3]])
        return ''.join(aa_list)

    # find every protein sequence of every orf
    all = [protein(seq) for seq in [coding_RNA,coding_RNA[1:],coding_RNA[2:],rc_RNA,rc_RNA[1:],rc_RNA[2:]]]

    # find all protein sequences
    final_list = []

    for protein_seq in all:
        switch = True
        start = 0

        while switch:
            start_index = protein_seq.find('M')

            # break the loop if there are no more start
            if start_index == -1:
                switch = False
            else:
                end_index = protein_seq.find('X')
                real_motif = protein_seq[start_index:end_index]
                if real_motif:
                    final_list.append(real_motif)
                protein_seq = protein_seq[start_index+1:]


    return final_list


print(ORF('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'))