from pathlib import Path
import glob
import os
from typing import TYPE_CHECKING
import pandas as pd


def aggregate_marketinsights_result(root_directory, file_extension):
    paths = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_extension):
                s = os.path.join(root, file)
                paths.append(s)
 #   print(paths)
    all_data = pd.DataFrame()
    i = 0
    for file in paths:
        df = pd.read_excel(file, parse_dates=False)
        all_data = all_data.append(df,ignore_index=True)
    return all_data    


root_directory = "C:\\Test\\BBB"
master_marketinsights_result = pd.DataFrame()
master_marketinsights_result = aggregate_marketinsights_result(root_directory, ".xlsx")
rslt_df = master_marketinsights_result.loc[master_marketinsights_result['月点击量'] == '--']
print(rslt_df)

