__author__ = 'Trappola'

import pandas as pd


def main():

    # 1 - subgenres to genres aggregation
    genres_substitution("../OUTPUT/listenings_genre_merged.csv")
    # genres_substitution("../OUTPUT/prova.csv")

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


def genres_substitution(filename):
    df = pd.read_csv(filename, skipinitialspace=True, delimiter=",")
    print df.describe()
    trovato = False
    count = 0
    # genres = ["indie rock", "rock", "pop", "metal", "electronic", "hip hop", "indie", "r&b", "punk", "folk", "jazz", "emo", "house", "soul"]
    genres = ["indie rock", "rock", "pop", "metal", "electronic", "hip hop", "indie", "r&b", "punk", "folk"]
    for index, item in df.iterrows():
        trovato = False
        for obj in genres:
            if obj in item["genre"]:
                df.set_value(index, "genre", obj)
                trovato = True
                break
        if not trovato:
            df.set_value(index, "genre", "altro")
            count += 1
    print count

    df.to_csv("../OUTPUT/listenings_genre_merged_substitution_top10.csv", index=False)

if __name__ == "__main__":
    main()