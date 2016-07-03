__author__ = 'Trappola'

import networkx as nx
import matplotlib.pyplot as plt
import sys
import copy


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


def load_users_listenings(path):
    users_listenings_file = open(path)
    users_listenings = {}

    count = 0
    for l in users_listenings_file:
        if count > 0:
            splitted_line = l.rstrip().split(",")
            # print splitted_line
            users_listenings[splitted_line[0]] = None

        count += 1

    # print users_listenings
    return users_listenings


users_listenings_path = "../OUTPUT/muse/user_listenings_single_row_muse.csv"
unique_id = load_users_listenings(users_listenings_path)

print len(unique_id)
# sys.exit()

artist_name = "Muse"
artist_name_without_string = "muse_v2"

# ho tolto l'header dal file della network per semplicita nella lettura con networkx
path_network_file = "../DATA/network_20160403_without_header.txt"
# path_network_file = "../DATA/network_small.csv"
input_random_network = open(path_network_file)
graph = nx.read_edgelist(input_random_network, delimiter=',', nodetype=str) #create_using=nx.DiGraph()
print len(graph.nodes())

# out_file_degree = open("../OUTPUT/"+artist_name_without_string+"/network_degree_"+artist_name_without_string+".csv", "w")
# out_file_degree.write("user_id,degree_initial_network\n")
# plot_user_distribution(graph.degree(), "../PLOT/user_distribution_10.jpg")
# for node, degree in graph.degree().iteritems():
#     # print node
#     # print degree
#     if node in unique_id:
#         out_file_degree.write(node+","+str(degree)+"\n")
#         out_file_degree.flush()
#
# out_file_degree.close()


new_graph = copy.deepcopy(graph)


for node in graph.nodes():
    # print node
    # print degree
    if node not in unique_id:
        new_graph.remove_node(node)

# write network on file
out_file = open("../OUTPUT/network_cleaned_final.csv", "w")
# nx.write_edgelist(graph, out_file, delimiter=",", data=True)
nx.write_edgelist(new_graph, out_file, delimiter=",", data=False)
print len(new_graph.nodes())



