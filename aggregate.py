from pathlib import Path
import glob
import os
from typing import TYPE_CHECKING
import pandas as pd

def csv_to_xlsx(root_directory):
    BASE_DIR = Path(root_directory)
    files = BASE_DIR.glob("*.csv")

    for f in files:
        new_name = f.stem.split(".")[0]
        target = BASE_DIR / f"{new_name}.xlsx"
        f.rename(target)
        
def master_keyword_result(root_directory, file_extension):
    paths = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_extension):
                s = os.path.join(root, file)
                paths.append(s)

    all_data = pd.DataFrame()
    i = 0
    for file in paths:
        df = pd.read_excel(file, parse_dates=False)
        df['广告排名'] = 'x'+df['广告排名'].astype(str)
        df['自然排名'] = 'x'+ df['自然排名'].astype(str)
        date_list = list(map(lambda x: x.replace('.xlsx',''),file.split("_")[2:]))
        print(i)
        i = i+1
        df['ASIN'] = file.split('/')[-1].split('_')[0]
        df['ASIN'] = df['ASIN'].astype(str)
        df['Date'] = '-'.join(date_list)
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
        all_data = all_data.append(df,ignore_index=True)
        all_data = all_data[['ASIN', 'Date', '流量词', '月点击量', '月点击占比', '月搜索量', '流量占比', '广告排名', '自然排名']]
        if(i == 1000):
            all_data.to_csv('C:/Test/master_keyword_result1000.csv', index=False)
            all_data = df
        if(i == 2000):
            all_data.to_csv('C:/Test/master_keyword_result2000.csv', index=False)
            all_data = df
        if(i == 3000):
            all_data.to_csv('C:/Test/master_keyword_result3000.csv', index=False)
            all_data = df
        if(i == 4000):
            all_data.to_csv('C:/Test/master_keyword_result4000.csv', index=False)
            all_data = df
        if(i == 5000):
            all_data.to_csv('C:/Test/master_keyword_result5000.csv', index=False)
            all_data = df
        if(i == 6000):
            all_data.to_csv('C:/Test/master_keyword_result6000.csv', index=False)
            all_data = df
        if(i == 7000):
            all_data.to_csv('C:/Test/master_keyword_result7000.csv', index=False)
            all_data = df
        if(i == 8000):
            all_data.to_csv('C:/Test/master_keyword_result8000.csv', index=False)
            all_data = df
        if(i == 9000):
            all_data.to_csv('C:/Test/master_keyword_result9000.csv', index=False)
            all_data = df
    all_data.to_csv('C:/Test/master_keyword_resultstub.csv', index=False)
#if __name__ == "__main__":
    # csv_to_xlsx('/Users/venkatasai/Downloads/test_folder')
    # master_keyword_result('/Users/venkatasai/Downloads/test_folder', '.xlsx')
csv_to_xlsx('C:/Test/AAA')
master_keyword_result('C:/Test/AAA/','.xlsx')
