import networkx as nx

def base_stats(graph):
    nodes = len(graph.nodes())
    edges = len(graph.edges())
    density = nx.density(graph)
    c_coefficient = nx.average_clustering(graph)
    avg_degree = 2*float(edges)/float(nodes)
    network_diameter = nx.diameter(graph)
    avg_shortest_path_length = nx.average_shortest_path_length(graph)

    print "avg_degree: " + str(avg_degree)
    print "nodes: " + str(nodes) + "\n" + \
          "edges: " + str(edges) + "\n" +\
          "density: " + str(density) + "\n" +\
           "network_diameter: " + str(network_diameter) + "\n" +\
          "c_coefficient: " + str(c_coefficient) + "\n" +\
          "avg_shortest_path_length: " + str(avg_shortest_path_length)


def get_neighbors_avg_listenings(node_neighbors, users_listenings):
    if len(node_neighbors) == 0:
        return 0

    neighbors_listenings_sum = 0

    for n in node_neighbors:
        # print n
        if (n in users_listenings):
            neighbors_listenings_sum += int(users_listenings[n]['num_ascolti_totali'])

    return float(neighbors_listenings_sum)/float(len(node_neighbors))


def get_neighbors_avg_artist_listenings(node_neighbors, users_listenings):
    if len(node_neighbors) == 0:
        return 0

    neighbors_artist_listenings_sum = 0

    for n in node_neighbors:
        if (n in users_listenings):
            neighbors_artist_listenings_sum += int(users_listenings[n]['num_ascolti_artista'])

    return float(neighbors_artist_listenings_sum) / float(len(node_neighbors))


def get_neighbors_avg_weeks(node_neighbors, users_listenings):
    if len(node_neighbors) == 0:
        return 0

    neighbors_weeks_sum = 0

    for n in node_neighbors:
        if (n in users_listenings):
            neighbors_weeks_sum += int(users_listenings[n]['settimane_totali'])

    return float(neighbors_weeks_sum) / float(len(node_neighbors))


def get_neighbors_avg_artist_weeks(node_neighbors, users_listenings):
    if len(node_neighbors) == 0:
        return 0

    neighbors_artist_weeks_sum = 0

    for n in node_neighbors:
        if (n in users_listenings):
            neighbors_artist_weeks_sum += int(users_listenings[n]['settimane_artista'])

    return float(neighbors_artist_weeks_sum) / float(len(node_neighbors))


def load_users_listenings(path):
    users_listenings_file = open(path)
    users_listenings = {}

    count = 0
    for l in users_listenings_file:
        if count > 0:
            splitted_line = l.rstrip().split(",")
            # print splitted_line
            users_listenings[splitted_line[0]] = {}
            users_listenings[splitted_line[0]]['num_ascolti_totali'] = splitted_line[1]
            users_listenings[splitted_line[0]]['num_ascolti_artista'] = splitted_line[2]
            users_listenings[splitted_line[0]]['settimane_totali'] = splitted_line[3]
            users_listenings[splitted_line[0]]['settimane_artista'] = splitted_line[4]
        count += 1

    # print users_listenings
    return users_listenings


def create_nodes_info(nodes, users_listenings):
    nodes_info = {}
    for node in nodes:
        nodes_info[node] = {}
        node_neighbors = network.neighbors(node)

        nodes_info[node]['degree'] = len(node_neighbors)
        nodes_info[node]['neighbors_avg_listenings'] = get_neighbors_avg_listenings(node_neighbors, users_listenings)
        nodes_info[node]['neighbors_avg_artist_listenings'] = get_neighbors_avg_artist_listenings(node_neighbors, users_listenings)
        nodes_info[node]['neighbors_avg_week_listenings'] = get_neighbors_avg_weeks(node_neighbors, users_listenings)
        nodes_info[node]['neighbors_avg_artist_weeks'] = get_neighbors_avg_artist_weeks(node_neighbors, users_listenings)
        # print nodes_info[node]
    return nodes_info

def write_nodes_info(node_info, users_listenings_with_frindes_path):
    out_file = open(users_listenings_with_frindes_path, "w")
    out_file.write("user_id,num_amici,friends_num_ascolti_totali,friends_num_ascolti_artista,friends_settimane_totali,friends_settimane_artista\n")
    for i in node_info:
        node = node_info[i]
        str1 = str(i)+","+str(node['degree'])+","+str(node['neighbors_avg_listenings'])+","+str(node['neighbors_avg_artist_listenings'])+","+str(node['neighbors_avg_week_listenings'])+","+str(node['neighbors_avg_artist_weeks'])+"\n"
        out_file.write(str1)
    out_file.close

network_path = "../OUTPUT/network_cleaned.csv"
users_listenings_path = "../OUTPUT/users_listenings.csv"
users_listenings_with_frindes_path = "../OUTPUT/users_listenings_with_friends.csv"

network_file = open(network_path)
network = nx.read_edgelist(network_file, delimiter=',', nodetype=str)
nodes = network.nodes()

users_listenings = load_users_listenings(users_listenings_path)
nodes_info = create_nodes_info(nodes, users_listenings)
write_nodes_info(nodes_info, users_listenings_with_frindes_path)


# print nodes_info

