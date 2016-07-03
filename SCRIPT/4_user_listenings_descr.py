__author__ = 'Trappola'


import pandas as pd
import datetime
import sys
import matplotlib.pyplot as plt
from collections import Counter


def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


def save_csv(data, filename):
    data.to_csv(filename, index=False)


def merge(general_listenings, artists_listenings):
    df_merged = pd.merge(general_listenings, artists_listenings,
                        left_on=['user_id', 'week_year'],
                        right_on=['user_id', 'week_year'],
                        how ='inner')
    save_csv(df_merged, "../OUTPUT/user_listenings_week_final_merged.csv")


def to_year_week(date_str):
    date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    week_str = int(date_time.isocalendar()[1])
    month = int(date_time.strftime("%m"))
    # print month
    # print str(month)
    right_year = int(date_time.strftime("%Y"))
    # print right_year
    if week_str == 53 and month == 1:
        right_year -= 1
    if len(str(week_str)) == 1:
        week_str = "0"+str(week_str)
    return str(right_year) + "/" + str(week_str)


def plot_user_distribution(g_data, out=None):
    print g_data
    g_data = sorted(g_data.iteritems(), key=lambda (k, v): k)

    # sys.exit()
    x_axis = []
    y_axis = []
    y_axis_artist = []
    genres_label = []
    count = 1
    for key, value in g_data:
        x_axis.append(count)
        y_axis.append(value["ascolti_tot"])
        y_axis_artist.append(value["ascolti_artista"])
        genres_label.append(key)
        count += 1
    print y_axis_artist
    # sys.exit()
    plt.bar(x_axis, y_axis, align='center', color="b", alpha=0.5)
    plt.bar(x_axis, y_axis_artist, align='center', color="r", alpha=0.5)
    plt.xticks(x_axis, genres_label, rotation='vertical')
    # plt.title(title)
    plt.tick_params(axis='x', labelsize=9)
    plt.tick_params(axis='y', labelsize=9)
    plt.xlim([+0, len(x_axis)+1])
    # plt.ylim([-10, 105])
    plt.gca().yaxis.grid(True)
    if (out):
        plt.savefig(out, bbox_inches="tight")
    plt.show()


# df = load_csv("prova3.csv")
df = load_csv("listenings_genre_merged.csv")
print "######################### File Letto ##################################################################"
# Converte timestamp in anno/settimana

df['date'] = df['date'].apply(lambda x: to_year_week(x))
print "######################### DATE refactoring ##################################################################"
# Group by user_id, artist e date per ottenere la somma degli ascolti per ogni artista nella stessa settimana

df_grouped = df.groupby(['user_id', 'date'])
print "######################### Grouping ##################################################################"
# Salvo csv con gli ascolti settimanali per artista

artist_name = "Muse"
artist_name_without_string = "muse_v2"

out_file_user_listening = open("../OUTPUT/"+artist_name_without_string+"/user_listenings_"+artist_name_without_string+".csv", "w")
out_file_user_listening.write("user_id,num_ascolti_totali,num_ascolti_artista,settimane_totali,settimane_artista,artisti_univoci,generi_univoci\n")

out_file_distribution_user = open("../OUTPUT/"+artist_name_without_string+"/user_listenings_distribution_"+artist_name_without_string+".csv", "w")
out_file_distribution_user.write("user_id,week_year,num_ascolti_totali,num_ascolti_artista,artisti_univoci,generi_univoci\n")

out_file_global = open("../OUTPUT/"+artist_name_without_string+"/user_listenings_single_row_"+artist_name_without_string+".csv", "w")
out_file_global.write("user_id,num_ascolti_totali,num_ascolti_artista,settimane_totali,settimane_artista,artisti_univoci,generi_univoci\n")


users = {}
sum_count_listening_artist = 0
sum_count_listening = 0
week_listening_artist = 0
week_listening = 0

generi_univoci = {}
artisti_univoci = {}

artisti_univoci_week = {}
generi_univoci_week = {}

string_data_distribution = ""
old_key = None
first = True
count_row = 0

for key, value in df_grouped:
    # print key

    if count_row % 1000 == 0:
        print "##################### Numero di righe lette in groupby: "+str(count_row)
    count_row += 1

    # if old_key != key[0] and sum_count_listening_artist > 1:
    #     # fare write riga dell'utente relativa ad artista
    #     # plot_user_distribution(users[old_key], "../PLOT/"+artist_name_without_string+"/distribution_"+artist_name_without_string+"_"+old_key+".jpg")
    #     # sys.exit()

    if key[0] not in users:
        users[key[0]] = {}

        if old_key is not None:
            general_row_artist = old_key+","+str(sum_count_listening)+","+str(sum_count_listening_artist)+","+\
                                     str(week_listening)+","+str(week_listening_artist)+","+str(len(artisti_univoci))\
                                 +","+str(len(generi_univoci))+"\n"
            out_file_global.write(general_row_artist)
            out_file_global.flush()

            if sum_count_listening_artist > 0:
                out_file_user_listening.write(general_row_artist)
                out_file_distribution_user.write(string_data_distribution)

                out_file_user_listening.flush()
                out_file_distribution_user.flush()

            sum_count_listening_artist = 0
            sum_count_listening = 0
            week_listening_artist = 0
            week_listening = 0
            artisti_univoci = {}
            generi_univoci = {}

            string_data_distribution = ""

    week_listening += 1
    sum_count_listening += len(value)
    sum_count_listening_artist_in_week = 0

    artisti_univoci_week = {}
    generi_univoci_week = {}

    # for row_key, row in value.iterrows():
    #     # print row_key
    #     # print row["artist"]
    #     if artist_name == row["artist"].lower():
    #         sum_count_listening_artist += 1
    #         sum_count_listening_artist_in_week += 1
    #         if sum_count_listening_artist_in_week == 1:
    #             week_listening_artist += 1

    artisti = value["artist"].values.tolist()
    counter = Counter(artisti)

    artisti_univoci_week = {}
    artisti_univoci_week = dict(counter)
    if artist_name in artisti_univoci_week:
        sum_count_listening_artist += artisti_univoci_week[artist_name]
        sum_count_listening_artist_in_week += artisti_univoci_week[artist_name]
        week_listening_artist += 1
    for key_artist in artisti_univoci_week:
        if key_artist not in artisti_univoci:
            artisti_univoci[key_artist] = None

    generi = value["genre"].values.tolist()
    counter = Counter(generi)

    generi_univoci_week = {}
    generi_univoci_week = dict(counter)
    if artist_name in generi_univoci_week:
        sum_count_listening_artist += generi_univoci_week[artist_name]
        sum_count_listening_artist_in_week += generi_univoci_week[artist_name]
        week_listening_artist += 1
    for key_genre in generi_univoci_week:
        if key_genre not in generi_univoci:
            generi_univoci[key_genre] = None


    string_data_distribution += str(key[0])+","+str(key[1])+","+str(len(value))+","+str(sum_count_listening_artist_in_week)\
                                +","+str(len(artisti_univoci_week))+","+str(len(generi_univoci_week))+"\n"

    # users[key[0]][key[1]] = {
    #     "ascolti_tot": len(value),
    #     "ascolti_artista": sum_count_listening_artist_in_week
    # }
    # print string_data
    old_key = key[0]
    # sys.exit()
# out_file.close()

general_row_artist = old_key+","+str(sum_count_listening)+","+str(sum_count_listening_artist)+","+\
                         str(week_listening)+","+str(week_listening_artist)+"\n"
out_file_global.write(general_row_artist)
out_file_global.flush()

if sum_count_listening_artist > 0:
    out_file_user_listening.write(general_row_artist)
    out_file_distribution_user.write(string_data_distribution)

    out_file_user_listening.flush()
    out_file_distribution_user.flush()

out_file_global.close()
out_file_user_listening.close()
out_file_distribution_user.close()

# print users
print "Ciao Bel ho finito tutto!!!"
# plot_user_distribution(users["000Silenced"])

# Merge
# general_listenings = load_csv("user_listenings_week_count.csv")
# artist_listenings = load_csv("user_listenings_artist_week_count_2.csv")
# merge(general_listenings, artist_listenings)

# with open(fname) as f:
#     next(f)
#     for line in f:
#         #do something