import pandas as pd
import datetime

def merge(df_left, df_right, left_on, right_on, columns_rename_obj=None):
    df_merged = pd.merge(df_left, df_right,
                            left_on=left_on,
                            right_on=right_on,
                            how='inner')

    if not columns_rename_obj == None:
        df_merged = df_merged.rename(columns=columns_rename_obj)
    return df_merged


def save_csv(data, filename):
    data.to_csv(filename, index=False)


def load_csv(input_path):
    return pd.read_csv(input_path, skipinitialspace=True, delimiter=",", error_bad_lines=False)

users_listenings_single_row_path = "../OUTPUT/muse/user_listenings_single_row_muse.csv"
users_listenings_quota_path ="../OUTPUT/genre_listenings_user_quota_top10.csv"
active_user_2016_path = "../OUTPUT/active_user_2016_50_ascolti.csv"
out_path_final = "../OUTPUT/users_for_segmentation_final.csv"

df_listenings_single_row = load_csv(users_listenings_single_row_path)
df_listenings_quota = load_csv(users_listenings_quota_path)
del df_listenings_single_row['num_ascolti_artista']
del df_listenings_single_row['settimane_artista']
del df_listenings_single_row['generi_univoci']

df_merged_1 = merge(df_listenings_single_row,df_listenings_quota,["user_id","num_ascolti_totali"],["user_id","num_ascolti_totali"])
df_active_user_2016 = load_csv(active_user_2016_path)
df_final_merge = merge(df_merged_1,df_active_user_2016,'user_id','user_id')
save_csv(df_final_merge,out_path_final)