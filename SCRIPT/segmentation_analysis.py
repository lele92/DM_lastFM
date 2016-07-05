__author__ = 'Trappola'


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os


def main():

    df = pd.read_csv("../OUTPUT/segmentation_results_k-means.csv", delimiter=",", skipinitialspace=True)

    # plt.style.use("dark_background")

    k_means_analysis(df)


def k_means_analysis(df):

    out_file_centroid = open("../OUTPUT/k_means_centroid.csv", "w")
    out_file_centroid.write("cluster_number,number_of_element,num_ascolti_totali,settimane_totali,artisti_univoci,indie rock,rock,pop,metal,electronic,hip hop,indie,r&b,punk,folk,altro\n")

    string_df = str(777)+","+str(df["user_id"].count())+","+str(df["num_ascolti_totali"].mean())+","+str(df["settimane_totali"].mean())+","+str(df["artisti_univoci"].mean())+\
                      ","+str(df["indie rock"].mean()*100)+","+str(df["rock"].mean()*100)+","+str(df["pop"].mean()*100)+\
                      ","+str(df["metal"].mean()*100)+","+str(df["electronic"].mean()*100)+","+str(df["hip hop"].mean()*100)+\
                      ","+str(df["indie"].mean()*100)+","+str(df["r&b"].mean()*100)+","+str(df["punk"].mean()*100)+\
                      ","+str(df["folk"].mean()*100)+","+str(df["altro"].mean()*100)+"\n"
    out_file_centroid.write(string_df)
    clusters = df["KMeans"].unique()
    clusters.sort()
    for cluster in clusters:
        data = df[df["KMeans"] == cluster]
        string_data = str(cluster)+","+str(data["user_id"].count())+","+str(data["num_ascolti_totali"].mean())+","+str(data["settimane_totali"].mean())+","+str(data["artisti_univoci"].mean())+\
                      ","+str(data["indie rock"].mean()*100)+","+str(data["rock"].mean()*100)+","+str(data["pop"].mean()*100)+\
                      ","+str(data["metal"].mean()*100)+","+str(data["electronic"].mean()*100)+","+str(data["hip hop"].mean()*100)+\
                      ","+str(data["indie"].mean()*100)+","+str(data["r&b"].mean()*100)+","+str(data["punk"].mean()*100)+\
                      ","+str(data["folk"].mean()*100)+","+str(data["altro"].mean()*100)+"\n"
        out_file_centroid.write(string_data)
        out_file_centroid.flush()
        genres_distr(data, cluster)
        # sex_distr(data, cluster, alg_type)
    out_file_centroid.close()

def genres_distr(df, number):
    element_number = df["user_id"].count()
    # print df["user_id"].count()
    genres_data = {'genre': ['ROCK', 'POP', 'ELECTRONIC', 'METAL', 'HIP HOP', 'INDIE ROCK', 'PUNK', 'FOLK', 'INDIE', 'R&B', 'ALTRO'],
        'percentage listenings': [df["rock"].mean()*100, df["pop"].mean()*100, df["electronic"].mean()*100, df["metal"].mean()*100, df["hip hop"].mean()*100, df["indie rock"].mean()*100,
        df["punk"].mean()*100, df["folk"].mean()*100, df["indie"].mean()*100, df["r&b"].mean()*100, df["altro"].mean()*100]}
    df = pd.DataFrame(genres_data, columns=['genre', 'percentage listenings'])

    pd.pivot_table(df, index=["genre"]).plot(kind="bar", color="b", alpha=0.6)
    ax = plt.gca()
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:.0f}%'.format(x) for x in vals])
    # print df.count()
    plt.title("Genre Distribution Cluster "+str(number)+" composto da: "+str(element_number) +" elementi")
    # plt.show()

    plt.tight_layout()
    path = "../PLOT/CustomerSegmentation"
    if not os.path.exists(path):
        os.makedirs(path)
    filename = path + "/k-means_genre_distribution_cluster_" + str(number)+".png"
    plt.savefig(filename, bbox_inches="tight")
    plt.close()

# def sex_distr(df, number, alg_type):
#
#     df["sesso"] = df["sesso"].replace(0, "UOMINI")
#     df["sesso"] = df["sesso"].replace(1, "DONNE")
#     sex = df["sesso"].value_counts()
#     sex.plot(kind = "bar", width = 0.07)
#     plt.tight_layout()
#     path = "/home/fabrizio/Scrivania/Segmentation_results/" + alg_type + "/Cluster" + str(number)
#     if not os.path.exists(path):
#         os.makedirs(path)
#     filename = path + "/sex.png"
#     plt.savefig(filename, bbox_inches = "tight")
#     plt.close()


if __name__ == "__main__":
	main()