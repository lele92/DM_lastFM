import numpy as np
import sys
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def plot_user_distribution(g_data, out):
    g_data = sorted(g_data.iteritems(), key=lambda (k, v): v, reverse=True)[:10]
    x_axis = []
    y_axis = []
    genres_label = []
    count = 1
    for key, value in g_data:
        x_axis.append(count)
        y_axis.append(value)
        genres_label.append(key)
        count += 1

    plt.bar(x_axis, y_axis, align='center', color="b", alpha=0.5)
    plt.xticks(x_axis, genres_label, rotation='vertical')
    # plt.title(title)
    plt.tick_params(axis='x', labelsize=9)
    plt.tick_params(axis='y', labelsize=9)
    plt.xlim([+0, len(x_axis)+1])
    # plt.ylim([-10, 105])
    plt.gca().yaxis.grid(True)
    plt.savefig(out, bbox_inches="tight")
    plt.show()


# df = pd.read_csv("../OUTPUT/prova.csv", skipinitialspace=True, delimiter=",", error_bad_lines=False)
df = pd.read_csv("../OUTPUT/listenings_genre_merged.csv", skipinitialspace=True, delimiter=",", error_bad_lines=False)

groupby_artisti = df.groupby(df['artist'])
groupby_artisti = sorted(groupby_artisti, key=lambda x: len(x[1]), reverse=True)  # reverse the sort i.e. largest first

# print groupby_artisti
# out_file = open("../OUTPUT/top_artists_user.csv", "w")
count = 1
count_unique = 0
artist = "Coldplay"
array_user = []
artist_dict = {}
unique_users_artist = {}
# array_florence = ["florence + the machine", "florence and the machine"]
for key, item in groupby_artisti:
    artist_dict[key] = len(item)
    unique_users_artist[key] = len(item['user_id'].unique())
    # unique_user = len(item['user_id'].unique())
    # newStr = str(count) + "," + key + "," + str(len(item))+"," + str(unique_user) + "\n"
    # out_file.write(newStr)
    # if "coldplay" in key.lower():
    #     # print key
    #     # print unique_user
    #     for index, row in item.iterrows():
    #         array_user.append(row["user_id"])
    #     count_unique += unique_user
    #
    # count += 1
# out_file.close()
# print len(array_user)
# print array_user
# np_array = np.array(array_user)
# unique_array = np.unique(np_array)
# print len(unique_array)
# print count_unique

# out_file = open("../OUTPUT/utent  i_univoci_"+artist+".txt", "w")
# # scrive su file array con utenti utnivoci, per leggerlo basta usare funzione eval() sull'unica riga del txt
# out_file.write(str(unique_array.tolist()))
# print sorted(artist_dict.iteritems(), key=lambda (k, v): v, reverse=True)[:3]
plot_user_distribution(artist_dict, "../PLOT/artists_distribution_absolute.jpg")
plot_user_distribution(unique_users_artist, "../PLOT/unique_user_artists_distribution.jpg")