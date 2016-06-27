import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import datetime
import pandas as pd


def main():

    #1 Load and clean listenings_20160403 + write a new csv file
    #clean_listenings()

    #2 Load and clean genre_20160403 + write a new csv file
    #clean_artists()

    #3 Load both files and remove duplicates
    df_listenings = load_csv("listenings_clean.csv")
    df_listenings = df_listenings.drop_duplicates()

    df_genre = load_csv("artist_clean.csv")
    df_genre = df_genre.drop_duplicates()

    #4 Drop track and album columns
    del df_listenings['album']

    #5 Remove missing value from listenings cleaned
    df_listenings = remove_missing_values(df_listenings)

    #6 Remove rows containing wrong timestamps
    wrong_time = datetime.datetime.fromtimestamp(0).strftime("%Y-%m-%d %H:%M:%S")
    df_listenings = df_listenings[df_listenings["date"] != wrong_time]

    #7 Merge cleaned files
    merge(df_listenings, df_genre)

    #8 Describe
    #df = load_csv("listenings_genre_merged.csv")
    #print df.describe()


def load_csv(input_filename):
    return pd.read_csv("../OUTPUT/"+input_filename, skipinitialspace=True, delimiter=",", error_bad_lines=False)


def save_csv(data, filename):
    data.to_csv(filename, index=False)


def clean_listenings():

    out_file = open("../OUTPUT/listenings_clean_2.csv", "w")
    with open('../DATA/listenings_20160403.csv') as fp:
        for line in fp:
            str1 = line
            newStr = str1.replace(", ", "; ")
            lineS = newStr.split(",")
            if lineS[0] == "user_id":
                out_file.write(newStr)
                continue

            line1split = lineS[1].split(";", 1)
            if len(line1split) > 1:
                line1split[0] = datetime.datetime.fromtimestamp(float(line1split[0]) / 1e3)
                line1split[0] = line1split[0].strftime("%Y-%m-%d %H:%M:%S")
                lineS[1] = line1split[0] + "," + line1split[1]
            else:
                lineS[1] = datetime.datetime.fromtimestamp(float(lineS[1]) / 1e3)
                lineS[1] = lineS[1].strftime("%Y-%m-%d %H:%M:%S")

            if lineS[len(lineS)-1] == "\n":
                lineS.remove(lineS[len(lineS)-1])
                lineS[len(lineS)-1] += "\n"

            newStr = ",".join(lineS)
            out_file.write(newStr)

    out_file.close()


def clean_artists():

    out_file = open("../OUTPUT/artist_clean.csv", "w")
    with open('../DATA/genre_20160403.csv') as fp:
        for line in fp:
            newStr = line.replace(", ", "; ")
            out_file.write(newStr)
    out_file.close()



def merge(listenings, artists):

    dataset = pd.merge(listenings, artists, left_on='artist', right_on='artist')
    dataset = dataset[pd.notnull(dataset['artist'])]
    dataset = dataset[pd.notnull(dataset['genre'])]
    print dataset.describe()
    save_csv(dataset, "../OUTPUT/listenings_genre_merged.csv")


def remove_missing_values(df):
    df = df[pd.notnull(df['artist'])]
    df = df[pd.notnull(df['track'])]
    return df


if __name__ == "__main__":
    main()