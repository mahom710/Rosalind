from typing import final


def ReadFASTA(file_path):
    # Create list for id and seq
    id_list = []
    seq_list = []

    # Open the file and process it line by line
    with open(file_path, 'r') as file:
        seq = ""  # A temporary variable to build each sequence
        for line in file:
            line = line.strip()  # Remove any trailing newline characters

            # Check if the line is an ID
            if line.startswith('>'):
                # If there's already a sequence built, append it to the seq_list
                if seq:
                    seq_list.append(seq)
                    seq = ""  # Reset sequence builder for the next sequence
                # Append the ID (without the '>' character) to the id_list
                id_list.append(line[1:])
            else:
                # If it's not an ID, it's part of a sequence, so concatenate it
                seq += line

        # Don't forget to append the last sequence after the loop finishes
        if seq:
            seq_list.append(seq)

    return id_list, seq_list

def AdjacencyList(id_list,seq_list):
    final_list = []

    # iterate through each seq pair
    for i in range(len(seq_list)):
        # the sequence at i
        seq_i = seq_list[i]

        for j in range(len(seq_list)):
            # the sequence at j
            seq_j = seq_list[j]

            # as long as it is not the exact same read
            if i != j:
                # if the end of seq_i is the same as the start of seq_j
                if seq_i[-3:] == seq_j[0:3]:
                    final_list.append(f"{id_list[i]} {id_list[j]}")
    return final_list

# call it all
id, seq = ReadFASTA('rosalind_test.txt')
final = AdjacencyList(id,seq)

[print(pair) for pair in final]












