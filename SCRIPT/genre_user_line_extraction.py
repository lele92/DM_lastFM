__author__ = 'Trappola'

import pandas as pd
import datetime
import sys
import matplotlib.pyplot as plt
from collections import Counter

# genres_aggregator = ["indie rock", "rock", "pop", "metal", "electronic", "hip hop", "indie", "r&b", "punk", "folk", "jazz", "emo", "house", "soul", "altro"]
genres_aggregator = ["indie rock", "rock", "pop", "metal", "electronic", "hip hop", "indie", "r&b", "punk", "folk", "altro"]


def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


# df = load_csv("prova3.csv")
# df = load_csv("listenings_genre_merged_substitution.csv")
df = load_csv("listenings_genre_merged_substitution_top10.csv")
print "######################### File Letto ##################################################################"

out_file_user_listening = open("../OUTPUT/genre_listenings_user_quota_top10.csv", "w")
# out_file_user_listening = open("../OUTPUT/genre_listenings_user_quota_top15.csv", "w")
# out_file_user_listening.write("user_id,num_ascolti_totali,indie rock,rock,pop,metal,electronic,hip hop,indie,r&b,punk,folk,jazz,emo,house,soul,altro\n")
out_file_user_listening.write("user_id,num_ascolti_totali,indie rock,rock,pop,metal,electronic,hip hop,indie,r&b,punk,folk,altro\n")

df_grouped = df.groupby(['user_id'])

for key, value in df_grouped:
    generi = value["genre"].values.tolist()
    counter = Counter(generi)

    listenings_dict = {}
    listenings_dict = dict(counter)
    string_data = key + "," + str(len(generi))
    for genre in genres_aggregator:
        count = 0
        if genre in listenings_dict:
            count = listenings_dict[genre]
        string_data += "," + ("{0:.2f}".format(float(count)/float(len(generi))))
    out_file_user_listening.write(string_data+"\n")
    out_file_user_listening.flush()
    # sys.exit()
out_file_user_listening.close()