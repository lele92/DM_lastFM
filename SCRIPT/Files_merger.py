import pandas as pd
import datetime

def merge(df_left, df_right, left_on, right_on, out_file, columns_rename_obj=None):
    df_merged = pd.merge(df_left, df_right,
                            left_on=left_on,  #['user_id', 'week_year']
                            right_on=right_on,
                            how='right')

    if not columns_rename_obj == None:
        df_merged = df_merged.rename(columns=columns_rename_obj) #{'listening_count_x': 'total_count', 'listening_count_y': 'artist_count'}
    save_csv(df_merged, out_file)


def save_csv(data, filename):
    data.to_csv(filename, index=False)


def load_csv(input_path):
    return pd.read_csv(input_path, skipinitialspace=True, delimiter=",", error_bad_lines=False)


churn_info_path = "../OUTPUT/muse/ascolti_utenti_costanti_muse_churning_10.csv"
friends_info_path = "../OUTPUT/muse/users_listenings_with_friends.csv"
initial_degree_path = "../OUTPUT/network_degree_node.csv"
out_path_churn_friends_15 = "../OUTPUT/muse/users_listenings_churn_friends_15.csv"
out_path_churn_friends_10 = "../OUTPUT/muse/users_listenings_churn_friends_10.csv"
out_path_user_listenings = "../OUTPUT/muse/user_listenings_muse.csv"
out_path_listenings_friends_churn = "../OUTPUT/muse/users_listenings_listenings_churn_friends_15.csv"
out_path_listenings_degree_info = "../OUTPUT/muse/user_listenings_degree.csv"
out_path_listenings_degree_friends_churn = "../OUTPUT/muse/users_listenings_degree_friends_churn_10.csv"

df_listenings_info = load_csv(out_path_user_listenings)
df_degree_info = load_csv(initial_degree_path)
merge(df_listenings_info,df_degree_info,"user_id","user_id",out_path_listenings_degree_info)

df_churn_info = load_csv(churn_info_path)
df_friends_info = load_csv(friends_info_path)
merge(df_friends_info,df_churn_info,"user_id","user_id",out_path_churn_friends_10)

df_listenings_degree_info = load_csv(out_path_listenings_degree_info)
df_friends_churn_info = load_csv(out_path_churn_friends_10)
merge(df_listenings_degree_info,df_friends_churn_info,"user_id","user_id",out_path_listenings_degree_friends_churn)
