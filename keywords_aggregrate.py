import pandas as pd
import os


def main_metrics_master_table(root_dir_path, file_substr):
    paths = []
    for root, dirs, files in os.walk(root_dir_path):
        for file in files:
            if file.endswith(file_substr):
                s = os.path.join(root, file)
                paths.append(s)

    all_data = pd.DataFrame()
    for file in paths:
        df = pd.read_excel(file)
        df['ASIN'] = file.split('/')[-1].split('_')[0]
        df['KeyWord'] = file.split('/')[-1].split('_')[1]
        all_data = all_data.append(df,ignore_index=True)
    all_data.to_csv(root_dir_path + '/' + 'main_metrics_master_table.csv', index=False)
    
    return all_data
    
    
def main_sales_attribution(root_dir_path, file_substr):
    paths = []
    for root, dirs, files in os.walk(root_dir_path):
        for file in files:
            if file.endswith(file_substr):
                s = os.path.join(root, file)
                paths.append(s)

    all_data = pd.DataFrame()
    for file in paths:
        df = pd.read_excel(file, header=None)
        df_mod = df.set_index(0).T
        df_mod['ASIN'] = file.split('/')[-1].split('_')[0]
        df_mod['KeyWord'] = file.split('/')[-1].split('_')[1]
        all_data = all_data.append(df_mod,ignore_index=True)
    all_data.to_csv(root_dir_path + '/' + 'main_sales_attribution.csv', index=False)
    
    return all_data

def main_top102050100_master(root_dir_path, file_substr):
    paths = []
    for root, dirs, files in os.walk(root_dir_path):
        for file in files:
            if file.endswith(file_substr):
                s = os.path.join(root, file)
                paths.append(s)

    all_data = pd.DataFrame()
    for file in paths:
        keyword_df = pd.read_excel(file)
        keyword_df = keyword_df.T
        keyword_df.reset_index(drop=True, inplace=True)
        keyword_df.columns = keyword_df.iloc[0]
        keyword_df.drop(index=keyword_df.index[0], axis=0, inplace=True)
        keyword_df.reset_index(drop=True, inplace=True)
        keyword_df_slice_1 = keyword_df.iloc[0:1]
        keyword_df_slice_2 = keyword_df.iloc[1:2]
        keyword_df_slice_1.columns = [str(col) + ' Orders/Day' for col in keyword_df_slice_1.columns]
        keyword_df_slice_2.columns = [str(col) + ' Min. Reviews' for col in keyword_df_slice_2.columns]
        keyword_df_slice_1.reset_index(drop=True, inplace=True)
        keyword_df_slice_2.reset_index(drop=True, inplace=True)
        main_keyword_df = pd.concat([keyword_df_slice_1, keyword_df_slice_2], axis=1)
        main_keyword_df['ASIN'] = file.split('/')[-1].split('_')[0]
        main_keyword_df['KeyWord'] = file.split('/')[-1].split('_')[1]
        all_data = all_data.append(main_keyword_df,ignore_index=True)
    all_data.to_csv(root_dir_path + 'main_top102050100.csv', index=False)
    
    return all_data
    
    
if __name__ == "__main__":
    root_dir_path = 'C:/Test/BBB/'
    main_metrics = main_metrics_master_table(root_dir_path, 'MAINMETRICS_2021_8_17.xlsx')
    sales_attribution = main_sales_attribution(root_dir_path, "SALESATTRIBUTION_2021_8_17.xlsx")
    top102050100 = main_top102050100_master(root_dir_path, 'TOP102050100_2021_8_17.xlsx')
    main_metrics_sales_combined = pd.merge(main_metrics, sales_attribution, on=['ASIN', 'KeyWord'], how='inner')
    all_combined = pd.merge(main_metrics_sales_combined, top102050100, on=['ASIN', 'KeyWord'], how='inner')
    all_combined = all_combined.set_index(['ASIN', 'KeyWord'])
    all_combined.reset_index(inplace=True)
    all_combined.to_excel(root_dir_path + 'master_keywords_aggregated.xlsx', index=False)