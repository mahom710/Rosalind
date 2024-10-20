
def FASTA2List(path):
    # Open file
    with open(path) as file:
        # Create list to store data
        id_list = []
        seq_list = []
        seq = ''

        # read strip and read each line
        for line in file:
            line = line.strip()
        # if the line has > then add the seq and ids
            if line[0] == '>':
                # if the seq is not empty
                if seq:
                    seq_list.append(seq)
                # add the new id
                id_list.append(line[1:])
                # reset seq
                seq = ''
            else:
                seq = seq + line

        # add the last seq at the end
        seq_list.append(seq)

    return id_list, seq_list


def ConcensusString(seq_list):
    # Create empty matrix
    total_a = []
    total_t = []
    total_c = []
    total_g = []
    final_string = ''

    # loop through every column
    for i in range(len(seq_list[0])):
        # reset column
        column = ''
        # create column
        for seq in seq_list:
            column = column + seq[i]
        # for every column: count the total of each bp and store in dict
        count_dict = {}
        count_dict['A'] = column.count('A')
        count_dict['T'] = column.count('T')
        count_dict['C'] = column.count('C')
        count_dict['G'] = column.count('G')

        # add the max count to the final string
        final_string += max(count_dict,key=count_dict.get) # note how to do this for a dict, or else it will return not the max

        # create the matrix
        total_a.append(count_dict['A'])
        total_t.append(count_dict['T'])
        total_c.append(count_dict['C'])
        total_g.append(count_dict['G'])

    # create final matrix (outside of loop)
    matrix = {'A':total_a, 'C':total_c, 'G':total_g, 'T':total_t}

    return final_string,matrix

id_list, seq_list = FASTA2List('SecondLevel_Problems/rosalind_test.txt')
final_string, matrix = ConcensusString(seq_list)


print(final_string)
print(f"A: {' '.join(list(map(str, matrix['A'])))} ")
print(f"C: {' '.join(list(map(str, matrix['C'])))} ")
print(f"G: {' '.join(list(map(str, matrix['G'])))} ")
print(f"T: {' '.join(list(map(str, matrix['T'])))} ")