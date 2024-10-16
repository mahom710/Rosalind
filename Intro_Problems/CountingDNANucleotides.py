def CountingDnaNucleotide(sequence):
    # Start count for each base pair
    num_a = 0
    num_t = 0
    num_c = 0
    num_g = 0

    #
    sequence = sequence.lower()

    # Count each
    for bp in sequence:
        if bp == 'a':
            num_a += 1
        elif bp == 't':
            num_t += 1
        elif bp == 'c':
            num_c += 1
        elif bp == 'g':
            num_g += 1
        else:
            print(f'{bp} does not match')

    bp_dict = {
        'A': num_a,
        'T': num_t,
        'C': num_c,
        'G': num_g
    }

    return print(bp_dict['A'], bp_dict['C'], bp_dict['G'], bp_dict['T'])