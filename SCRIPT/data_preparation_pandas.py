__author__ = 'Trappola'

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_csv(input_filename):
    return pd.read_csv(input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


def load_csv_normally(input_filename):
    f = open(input_filename)
    count = 0
    for l in f:
        count += 1
    print "NUMERO DI RIGHE ORIGINALI = "+str(count)
    # return pd.read_csv(input_filename, skipinitialspace = True, delimiter=",", error_bad_lines=False)


def merge(data, genre_filename):

    df_g = load_csv(genre_filename)
    print df_g.shape
    dataset = pd.merge(data, df_g, left_on='artist', right_on='artist')
    print "DATASET SHAPE: "+str(dataset.shape)
    save_csv(dataset, "../OUTPUT/listenings_genre_merged.csv")


def save_csv(data, filename):

    data.to_csv(filename, index=False)
    print "File successfully saved."


# # 1 - loading listenings' csv file
# df = load_csv("../OUTPUT/Cleaned_col5.csv")
# print df.shape
#
# # 5 - merging with genre dataset
# merge(df, "../OUTPUT/artistClean.txt")

# load_csv_normally("DATA/listenings_20160403.csv")

# loading merged file
df = load_csv("../OUTPUT/listenings_genre_merged.csv")

# basic dataset statistics print
print df.describe()

# 6 - deleting rows with date = 0
# df = load_csv("../OUTPUT/listenings_def.csv")
# df = deleteDateZero(df)

#7 - deleting duplicate rows
df = df.drop_duplicates()

print df.describe()

#save new csv
save_csv(df, "../OUTPUT/listenings_def.csv")
# """