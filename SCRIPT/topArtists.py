import pandas as pd
import sys

df = pd.read_csv("../OUTPUT/listenings_genre_merged.csv", skipinitialspace=True, delimiter=",", error_bad_lines=False)
artist_count = df['artist'].value_counts()[:150]
out_file = open("../OUTPUT/top_artists.csv", "w")
count = 1
for key, item  in artist_count.iteritems():
    newStr = str(count) + "," + key + "," + str(item)+"\n"
    out_file.write(newStr)
    count +=1
out_file.close()