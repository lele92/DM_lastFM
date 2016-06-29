__author__ = 'Trappola'

import networkx as nx
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


# ho tolto l'header dal file della network per semplicita nella lettura con networkx
path_network_file = "../DATA/network_20160403_without_header.txt"
# path_network_file = "../DATA/network_small.csv"
input_random_network = open(path_network_file)
graph = nx.read_edgelist(input_random_network, delimiter=',', nodetype=str) #create_using=nx.DiGraph()

plot_user_distribution(graph.degree(), "../PLOT/user_distribution_10.jpg")


