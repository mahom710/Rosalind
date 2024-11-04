import pandas as pd
from scipy.stats import spearmanr
import os

# load in ctrl and txn DEG data
ctrl_df = pd.read_csv('other/DEG_data.csv')
txn_df = pd.read_csv('other/DEG_data_2.csv')

# column names
col_names  = ctrl_df.columns

# Calculate the summary statistics (mean, median, min, max) for the logFC, pvalue, and FDR columns in both DataFrames.
ctrl_summary = ctrl_df.describe()
txn_summary = txn_df.describe()
ctrl_avg_fc = ctrl_df['logFC'].mean()
txn_avg_fc = txn_df['logFC'].mean()

# check for missing values
ctrl_df[ctrl_df['logFC'].isnull()]
txn_df[txn_df['logFC'].isnull()]

# Filtering Data:
ctrl_df[(ctrl_df['logFC'] > 1) & (ctrl_df['FDR'] < 0.05)]
txn_df[(txn_df['logFC'] > 1) & (txn_df['FDR'] < 0.05)]

# FIND DEG #
# filter for FDR
fil_ctrl_df = ctrl_df[ctrl_df['FDR'] < 0.05]
fil_txn_df = txn_df[txn_df['FDR'] < 0.05]

# inner merge ctrl and txn dfs by gene
merged_df = pd.merge(fil_ctrl_df,fil_txn_df, how='inner', on='Gene')

# create a new col of txn - ctrl logFC
merged_df['adjusted_logFC'] = merged_df.apply(lambda row: row['logFC_y']- row['logFC_x'], axis=1)

# final genes
list(merged_df['Gene'])

# Merge ctrl and txn with a col to indicate where they came from
label_ctrl_df = ctrl_df
label_ctrl_df['type'] = 'control'
label_txn_df = txn_df
label_txn_df['type'] = 'treatment'
concat_df = pd.concat([label_ctrl_df, label_txn_df], ignore_index=True)

# correlation test
correlation,p_val = spearmanr(merged_df['logFC_x'], merged_df['logFC_y'])

# creating a class to hold the data
class control:
    # initialize parameters
    def __init__(self, genes, logFC, FDR):
        self.gene = genes
        self.locFC = logFC
        self.FDR = FDR

    # method to return only signficant genes
    def significant(self):
        return [self.gene[i] for i in range(len(self.FDR)) if self.FDR[i] < 0.05]









