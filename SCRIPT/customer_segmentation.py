__author__ = 'Trappola'

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import pdist
from collections import Counter
from sklearn.neighbors import kneighbors_graph
import numpy as np
import sys


def main():

    # loading dataset
    df = pd.read_csv("../OUTPUT/users_for_segmentation_final.csv", delimiter=",", skipinitialspace=True)
    df_final = pd.read_csv("../OUTPUT/users_for_segmentation_final.csv", delimiter=",", skipinitialspace=True)
    print df.describe()

    print "########################### Dataframe Letti ##############################################"

    # sys.exit()
    # user_id column drop
    df = df.drop("user_id", 1)
    # df = df.drop("data_reg", 1)
    # df_final = df_final.drop("data_reg", 1)

    # normalization
    df = ((df - df.mean()) / (df.max() - df.min()))

    print "########################### Perform Clustering ##############################################"

    KMeans_clusters = k_means(df)

    print "########################### Clustering Done ##############################################"

    df_final['KMeans'] = pd.Series(KMeans_clusters, index=df.index)
    df_final.to_csv("../OUTPUT/segmentation_results_k-means.csv", index=False)


def k_means(df):

    # maxS = 0
    # for clusters in range(2,100):
    #     kmeans = KMeans(init='k-means++', n_clusters=clusters, n_init=10, max_iter=100).fit(df.values)
    #     silhouette = silhouette_score(df.values,kmeans.labels_)
    #     clusters_final = clusters
    #     if silhouette > maxS:
    #         maxS = silhouette
    #         clusters_final = clusters
    #     print(maxS, clusters_final)
    # print("Risultato: ",maxS, clusters_final)

    kmeans = KMeans(init='k-means++', n_clusters=10, n_init=100, max_iter=300).fit(df.values)

    percent_clusters(kmeans.labels_)

    return kmeans.labels_


def percent_clusters(clusters):
    num_class = Counter(clusters)

    print("\nPercentuale elementi nel cluster")
    for key in num_class:
        print("Cluster ", key, ": %.2f (%d elementi)" % (((num_class[key]*100)/len(clusters)), num_class[key]))

if __name__ == "__main__":
    main()
