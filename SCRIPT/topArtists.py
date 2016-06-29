import pandas as pd
import numpy as np
import sys

df = pd.read_csv("../OUTPUT/prova.csv", skipinitialspace=True, delimiter=",", error_bad_lines=False)
# df = pd.read_csv("../OUTPUT/listenings_genre_merged.csv", skipinitialspace=True, delimiter=",", error_bad_lines=False)
groupby_artisti = df.groupby(df['artist'])
groupby_artisti = sorted(groupby_artisti, key=lambda x: len(x[1]), reverse=True)  # reverse the sort i.e. largest first
# print groupby_artisti
# out_file = open("../OUTPUT/top_artists_user.csv", "w")
count = 1
count_unique = 0
array_user = []
for key, item in groupby_artisti:
    unique_user = len(item['user_id'].unique())
    newStr = str(count) + "," + key + "," + str(len(item))+"," + str(unique_user) + "\n"
    # out_file.write(newStr)
    if "florance" in key.lower():
        print key
        print unique_user
        for index, row in item.iterrows():
            array_user.append(row["user_id"])
        count_unique += unique_user

    # print key
    # print item
    # sys.exit()
    count += 1
# out_file.close()
print len(array_user)
print array_user
np_array = np.array(array_user)
unique_array = np.unique(np_array)
print unique_array
print count_unique