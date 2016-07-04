__author__ = 'Trappola'

import pandas as pd
from collections import Counter
import sys


def main():

    # 1 - subgenres to genres aggregation
    # extract_active_users("../OUTPUT/prova.csv")
    extract_active_users("../OUTPUT/listenings_genre_merged.csv")


    # # loading dataset obtained
    # df = pd.read_csv("listenings_subst_genres.csv", delimiter = ",", skipinitialspace = True)
    #
    # #2 - Saving datasets of the first five genres
    # first_genres = ["rock", "pop", "electronic", "metal", "hip hop"]
    # for item in first_genres:
    #     extract_dataset(df, item)



def extract_dataset(data, genre):
    data = data[data["genre"] == genre]
    data.to_csv(genre + ".csv", index=False)


def extract_active_users(filename):
    df = pd.read_csv(filename, skipinitialspace=True, delimiter=",")
    print df.describe()

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    print "######################### DATE refactoring ##################################################################"

    year_to_test = 2016
    active_threshold = 100

    out_active_user = open("../OUTPUT/active_user_2016_"+str(active_threshold)+"_ascolti.csv", "w")
    out_active_user.write("user_id\n")

    df_grouped = df.groupby(['user_id'])

    for key, value in df_grouped:
        years = value["year"].values.tolist()
        counter = Counter(years)

        year_dict = {}
        year_dict = dict(counter)
        # print year_dict
        if year_to_test in year_dict and year_dict[year_to_test] >= active_threshold:
            out_active_user.write(key+"\n")
            out_active_user.flush()
        # sys.exit()

    out_active_user.close()

if __name__ == "__main__":
    main()