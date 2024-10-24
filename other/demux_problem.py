from collections import Counter

def demux(fastq_dict, adaptor_seq):
    # store the seqid and seq in different list
    id_list = [id for id in fastq_dict.keys()]
    seq_list = [seq for seq in fastq_dict.values()]

    # remove adaptor for each read
    rm_adapt_seq_list = [ seq[0:seq.find(adaptor_seq)] + seq[seq.find(adaptor_seq)+len(adaptor_seq):] for seq in seq_list]

    # find all unique umis and create dictionary (umi:read)
    all_umis = list(set([seq[0:6] for seq in rm_adapt_seq_list]))
    umi_dict = {umi: [] for umi in all_umis}

    # put each in the correct value in the dict
    for seq in rm_adapt_seq_list:
        cur_umi = seq[0:6]
        umi_dict[cur_umi].append(seq)

    print(umi_dict)
    return umi_dict


def concenus(same_umi_seq_list):
    # first check that all umi have the same len
    tmp = set([len(seq) for seq in same_umi_seq_list])
    if len(tmp) == 1:

    # create the final string
        consensus = ''

    # for every index of every seq
        for seq_col in zip(*same_umi_seq_list):
            # count the amount of each bp
            col_count = Counter(seq_col)
            # add the max bp to cocensus string
            consensus = consensus + (max(col_count)[0][0])

        return consensus

    else:
        print("not all UMI's are the same length")


# the entire program #

# load in the data
fastq_data = [
    ("@SEQ_ID1", "ACGTTGAGCGTATCGTAGCTAGATCGGAAGAGC"),
    ("@SEQ_ID2", "TGCAGTAGCTACGTCAGTCTAGATCGGAAGAGC"),
    ("@SEQ_ID3", "ACGTTGATCGTATCGCTTAGAGATCGGAAGAGC"),
    ("@SEQ_ID4", "GCTACGTAGCTAGCTGCTCAGATCGGAAGAGC")
]

# fastq in dictionary format
fastq_data = dict(fastq_data)

# adaptor sequence
adaptor_seq = 'AGATCGGAAGAGC'

# demux
demux_dict = demux(fastq_data, adaptor_seq)

# get the concensus per umi
concensus_list = [concenus(umis) for umis in demux_dict.values()]
print(concensus_list)

