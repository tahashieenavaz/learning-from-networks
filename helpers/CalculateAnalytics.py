import networkx as nx


def calculateAnalytics(graph):
    # node analytics
    print(nx.closeness_centrality(graph))
    print(nx.betweenness_centrality(graph))
    print(nx.clustering(graph))

    # graph analytics
    print(sum(dict(graph.degree()).values()) / len(dict(graph.degree())))
    if (nx.is_strongly_connected(graph)):
        print(nx.diameter(graph))
        print(nx.average_clustering(graph))
        print(nx.average_shortest_path_length(graph))
    else:
        print("graph is not strongly connected")
    print("________")
