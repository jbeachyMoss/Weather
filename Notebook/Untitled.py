# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd
from datetime import datetime

bfp_prod_path = 'C:/Users/jbeachy/Moss & Associates/Data Management - Data Team/Projects/BFP Weather/BFP Plan of Day Master.xlsx'
bfp_df_raw = pd.read_excel(bfp_prod_path , sheet_name = 'Mech')

col_name = bfp_df_raw.iloc[0,0:18].fillna('Date')
bfp_df_full = bfp_df_raw.iloc[4:,0:18].rename(columns = col_name).reset_index(drop = True)
bfp_df_full['Date'] = pd.to_datetime(bfp_df_full['Date'])
bfp_df_full['dayofweek'] = bfp_df_full.loc[:,'Date'].dt.strftime('%a')

bfp_df_full.head()

bfp_piles = bfp_df_full.loc[:,['Date','dayofweek','Piles (Ea)']]

bfp_piles


