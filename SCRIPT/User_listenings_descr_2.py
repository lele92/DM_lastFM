import pandas as pd
import datetime


def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


def save_csv(data, filename):
    data.to_csv(filename, index=False)


def merge(general_listenings, artists_listenings):
    df_merged = pd.merge(general_listenings, artists_listenings,
                        left_on=['user_id', 'week_year'],
                        right_on=['user_id', 'week_year'],
                        how ='inner')
    df_merged = df_merged.rename(columns={'listening_count_x': 'total_count', 'listening_count_y': 'artist_count'})
    save_csv(df_merged, "../OUTPUT/user_listenings_week_final_merged.csv")
#
#
def to_year_week(date_str):
    date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    week_str = str(date_time.isocalendar()[1])
    month = int(date_time.strftime("%m"))
    print str(month)
    right_year = int(date_time.strftime("%Y"))
    if week_str == 53 and month == 1:
        right_year -= 1
    if len(week_str) == 1:
        week_str = "0"+week_str
    return str(right_year) + "/" + week_str


# df = load_csv("listenings_genre_merged.csv")
# # Converte timestamp in anno/settimana
#
# df['date'] = df['date'].apply(lambda x: to_year_week(x))
# # Group by user_id, artist e date per ottenere la somma degli ascolti per ogni artista nella stessa settimana
#
# df_grouped = df.groupby(['user_id', 'artist', 'date']).size().to_dict()
# # Salvo csv con gli ascolti settimanali per artista
#
# out_file = open("../OUTPUT/user_listenings_artist_week_count_2.csv", "w")
# out_file.write("user_id,artist,week_year,listening_count_artist\n")
# for i in df_grouped:
#     out_file.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(df_grouped[i])+"\n")
# out_file.close()

merge
general_listenings = load_csv("user_listenings_week_count.csv")
artist_listenings = load_csv("user_listenings_artist_week_count_2.csv")
merge(general_listenings, artist_listenings)
