import pandas as pd
import datetime

def merge(df_left, df_right, left_on, right_on, out_file, columns_rename_obj=None):
    df_merged = pd.merge(df_left, df_right,
                            left_on=left_on,  #['user_id', 'week_year']
                            right_on=right_on,
                            how='inner')

    if not columns_rename_obj == None:
        df_merged = df_merged.rename(columns=columns_rename_obj) #{'listening_count_x': 'total_count', 'listening_count_y': 'artist_count'}
    save_csv(df_merged, out_file)


def save_csv(data, filename):
    data.to_csv(filename, index=False)


def load_csv(input_path):
    return pd.read_csv(input_path, skipinitialspace=True, delimiter=",", error_bad_lines=False)


churn_info_path = "../OUTPUT/muse/ascolti_utenti_costanti_muse_churning_15.csv"
friends_info_path = "../OUTPUT/muse/users_listenings_with_friends.csv"
out_path_churn_friends = "../OUTPUT/muse/users_listenings_churn_friends.csv"


df_churn_info = load_csv(churn_info_path)
df_friends_info = load_csv(friends_info_path)


merge(df_friends_info,df_churn_info,"user_id","user_id",out_path_churn_friends)
merge(df_friends_info,df_churn_info,"user_id","user_id",out_path_churn_friends)

