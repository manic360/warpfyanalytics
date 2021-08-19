from pathlib import Path
import glob
import os
import pandas as pd

def master_keyword_result(root_directory, file_extension):
    paths = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_extension):
                s = os.path.join(root, file)
                paths.append(s)

    all_data = pd.DataFrame()
    for file in paths:
        df = pd.read_excel(file, parse_dates=False)
        date_list = list(map(lambda x: x.replace('.xlsx',''),file.split("_")[2:]))
        df['ASIN'] = file.split('/')[-1].split('_')[0]
        df['Date'] = '-'.join(date_list)
        #df['Date'] = pd.to_datetime(df['Date'], format='%Y-%M-%D', errors='coerce')
        all_data = all_data.append(df,ignore_index=True)
        all_data = all_data[['ASIN', 'Date', '流量词', '月点击量', '月点击占比', '月搜索量', '流量占比', '广告排名', '自然排名']]
    #all_data.to_csv('master_keyword_result.csv', index=False)
    all_data.to_excel('I:/Shared drives/08 Technology/master_keyword_result.xlsx', index=False)

def csv_to_xlsx(root_directory):
    BASE_DIR = Path(root_directory)
    files = BASE_DIR.glob("*.csv")

    for f in files:
        new_name = f.stem.split(".")[0]
        target = BASE_DIR / f"{new_name}.xlsx"
        f.rename(target)


csv_to_xlsx('I:/Shared drives/08 Technology/0 - Collected Keyword (Home & Kitchen)/')
master_keyword_result('I:/Shared drives/08 Technology/0 - Collected Keyword (Home & Kitchen)/', ".xlsx")

