import pandas as pd
from scipy import stats
import os

from other.DEG_practice import merged_df

# import data
ctrl_df = pd.read_csv('other/DEG_data.csv')
txn_df = pd.read_csv('other/DEG_data_2.csv')

# summary stats
summary_ctrl = ctrl_df.describe()
summary_txn = txn_df.describe()


# group matching genes and take an average
common_genes = list(set(txn_df['Gene']) & set(ctrl_df['Gene']))

# figure out the average fold change of DEG genes between the control and treatment
# Merge the DataFrames
merge_df = pd.merge(ctrl_df, txn_df, how='inner', on='Gene')

# Filter rows where FDR_x and FDR_y are both less than 0.05
merge_df = merge_df[(merge_df['FDR_x'] < 0.05) & (merge_df['FDR_y'] < 0.05)]

# Calculate Adjusted_logFC
merge_df['Adjusted_logFC'] = merge_df['logFC_y'] - merge_df['logFC_x']

# Sort by absolute values of Adjusted_logFC from largest to smallest
merge_df = merge_df.reindex(merge_df['Adjusted_logFC'].abs().sort_values(ascending=False).index)

# Reset index if needed
merge_df.reset_index(drop=True, inplace=True)

# final filtered dataframe
filtered_gene = merge_df['Gene']
filtered_FC = merge_df['Adjusted_logFC']

gene_fc_filtered_dict = {gene:fc for gene,fc in zip(filtered_gene,round(filtered_FC,2))}






