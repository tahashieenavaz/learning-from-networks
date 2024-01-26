import networkx as nx
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np


# function to get the best k elements of a dict
def get_top_k_nodes(dict, k):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    top_k_elements = [c[0] for c in sorted_dict[:k]]
    return top_k_elements


# function to plot a graph with colored nodes
def plot_colered_graph(G, list, title):
    plt.figure(figsize=(20, 15))
    nx.draw_networkx(G, pos=nx.spring_layout(G, iterations=100, scale=8.0, k=0.2, seed=37),
                     with_labels=True, font_weight='bold', node_color=list, node_size=500, font_size=15)
    plt.title(title)
    plt.show()


# function that analyze a connected component of a graph
def analyze_connected_component(subgraph, component_number):
    print(f"\nAnalyzing Strongly Connected Component {component_number}:")
    print(f"Nodes: {subgraph.nodes()}")
    print(f"Edges: {subgraph.edges()}")

    # Check if the component has more than one node
    if len(subgraph) <= 1:
        print("Single-node component. Skipping analysis.")
        return

    # graph-level features
    diameter = nx.diameter(subgraph)  # diameter
    if nx.is_directed(subgraph):
        avg_degree = (sum(dict(subgraph.out_degree()).values()) / len(subgraph),  # average out-degree
                      sum(dict(subgraph.in_degree()).values()) / len(subgraph))  # average in-degree
    else:
        avg_degree = sum(dict(subgraph.degree()).values()) / len(subgraph)
    avg_clustering_coefficient = nx.average_clustering(subgraph)  # average clustering coefficient
    avg_shortest_path_length = nx.average_shortest_path_length(subgraph)  # average shortest path length

    print("\nGraph Features:")
    print(f"Diameter: {diameter}")
    if nx.is_directed(subgraph):
        print(f"Average Out Degree: {avg_degree[0]:.4f}")
        print(f"Average In Degree: {avg_degree[1]:.4f}")
    else:
        print(f"Average Degree: {avg_degree:.4f}")
    print(f"Average Clustering Coefficient: {avg_clustering_coefficient:.4f}")
    print(f"Average Shortest Path Length: {avg_shortest_path_length:.4f}")

    # node-level features
    degree_centralities = nx.degree_centrality(subgraph)  # degree centrality
    closeness_centralities = nx.closeness_centrality(subgraph)  # closeness centrality
    betweenness_centralities = nx.betweenness_centrality(subgraph)  # betweenness centrality
    clustering_coefficients = nx.clustering(subgraph)  # clustering coeffiecient

    print("\nNode Features:")
    for node in subgraph.nodes:
        print(f"Node {node}: "
              f"Degree Centrality: {degree_centralities[node]:.4f}, "
              f"Closeness Centrality: {closeness_centralities[node]:.4f}, "
              f"Betweenness Centrality: {betweenness_centralities[node]:.4f}, "
              f"Clustering Coefficient: {clustering_coefficients[node]:.4f}")

    k = 20  # set number of k-most important nodes

    # degree centrality
    top_k_degree_nodes = get_top_k_nodes(degree_centralities, k)
    print(f"\nTop {k} nodes with highest degree centrality:")
    for node in top_k_degree_nodes:
        print(f"Node {node}: "
              f"Degree Centrality: {degree_centralities[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['red' if node in top_k_degree_nodes else 'lightblue' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest degree centrality")

    # closeness centrality
    top_k_closeness_nodes = get_top_k_nodes(closeness_centralities, k)
    print(f"\nTop {k} nodes with highest closeness centrality:")
    for node in top_k_closeness_nodes:
        print(f"Node {node}: "
              f"Closeness Centrality: {closeness_centralities[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['red' if node in top_k_closeness_nodes else 'lightblue' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest closeness centrality")

    # betweenness centrality
    top_k_betweenness_nodes = get_top_k_nodes(betweenness_centralities, k)
    print(f"\nTop {k} nodes with highest betweenness centrality:")
    for node in top_k_betweenness_nodes:
        print(f"Node {node}: "
              f"Betweenness Centrality: {betweenness_centralities[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['red' if node in top_k_betweenness_nodes else 'lightblue' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest betweenness centrality")

    # clustering coefficient
    top_k_clustering_nodes = get_top_k_nodes(clustering_coefficients, k)
    print(f"\nTop {k} nodes with highest clustering coefficient:")
    for node in top_k_clustering_nodes:
        print(f"Node {node}: "
              f"Clustering Coefficient: {clustering_coefficients[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['red' if node in top_k_clustering_nodes else 'lightblue' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest clustering coefficient")

    # combination feature
    # normalization min-max of node features
    degree_centralities_normalized = {node: value for node, value in zip(
        subgraph.nodes,
        MinMaxScaler().fit_transform(np.array(list(degree_centralities.values())).reshape(-1, 1)).flatten())}
    closeness_centralities_normalized = {node: value for node, value in zip(
        subgraph.nodes,
        MinMaxScaler().fit_transform(np.array(list(closeness_centralities.values())).reshape(-1, 1)).flatten())}
    betweenness_centralities_normalized = {node: value for node, value in zip(
        subgraph.nodes,
        MinMaxScaler().fit_transform(np.array(list(betweenness_centralities.values())).reshape(-1, 1)).flatten())}
    clustering_coefficients_normalized = {node: value for node, value in zip(
        subgraph.nodes,
        MinMaxScaler().fit_transform(np.array(list(clustering_coefficients.values())).reshape(-1, 1)).flatten())}

    degree_centrality_factor, closeness_centrality_factor, betweenness_centrality_factor, clustering_coefficient_factor = 1, 1, 1, 1  # setting weights for combination method
    combination_node_features = {}
    for node in subgraph.nodes:
        combination_node_features[node] = (degree_centrality_factor * degree_centralities_normalized[node] +
                                           closeness_centrality_factor * closeness_centralities_normalized[node] +
                                           betweenness_centrality_factor * betweenness_centralities_normalized[node] +
                                           clustering_coefficient_factor * clustering_coefficients_normalized[node])

    top_k_combination = get_top_k_nodes(combination_node_features, k)
    print(f"\nTop {k} nodes with highest combination of node features:")
    for node in top_k_combination:
        print(f"Node {node}: "
              f"Combination value: {combination_node_features[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['red' if node in top_k_combination else 'lightblue' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest combination of node features")


# function to calculate graph and node features of a graph
def calculate_analytics(model):
    print("Analysing " + model.NAME + " network\n")
    graph = model.graph
    if nx.is_directed(graph):  # check if it is directed
        if nx.is_strongly_connected(graph):  # check if it is strongly connected
            print('Graph is strongly connected!')
            analyze_connected_component(graph, 1)
        else:
            print("Graph is not strongly connected.")
            components = list(nx.strongly_connected_components(graph))
            print("Connected Components:", components)
            for i, scc in enumerate(components):  # analyze each strongly connected component separately
                subgraph = graph.subgraph(scc)
                analyze_connected_component(subgraph, i + 1)
    else:
        if nx.is_connected(graph):  # check if it is connected
            print('Graph is connected!')
            analyze_connected_component(graph, 1)
        else:
            print("Graph is not connected.")
            components = list(nx.connected_components(graph))
            print("Connected Components:", components)
            for i, scc in enumerate(components):  # analyze each connected component separately
                subgraph = graph.subgraph(scc)
                analyze_connected_component(subgraph, i + 1)

    print("\n\n\n------------------------------------------------------------------\n\n\n")
