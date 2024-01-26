import networkx as nx
import matplotlib.pyplot as plt


# function to get the best k elements of a dict
def getTopKNodes(dict, k):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    top_k_elements = [c[0] for c in sorted_dict[:k]]
    return top_k_elements


# function to plot a graph with colored nodes
def plot_colered_graph(G, list, title):
    plt.figure()
    nx.draw_networkx(G, pos=nx.spring_layout(G, iterations=50, scale=4.0, k=0.2, seed=37), with_labels=True,
                     font_weight='bold', node_color=list)
    plt.title(title)
    plt.show()


def analyzeConnectedComponent(subgraph, component_number):
    print(f"\nAnalyzing Strongly Connected Component {component_number}:")
    print(f"Nodes: {subgraph.nodes()}")
    print(f"Edges: {subgraph.edges()}")

    # Check if the component has more than one node
    if len(subgraph) <= 1:
        print("Single-node component. Skipping analysis.")
        return

    # node-level features
    degree_centralities = nx.degree_centrality(subgraph)
    closeness_centralities = nx.closeness_centrality(subgraph)
    betweenness_centralities = nx.betweenness_centrality(subgraph)
    clustering_coefficients = nx.clustering(subgraph)

    # graph-level features
    diameter = nx.diameter(subgraph)
    if nx.is_directed(subgraph):
        avg_degree = (sum(dict(subgraph.out_degree()).values()) / len(subgraph),
                      sum(dict(subgraph.in_degree()).values()) / len(subgraph))
    else:
        avg_degree = sum(dict(subgraph.degree()).values()) / len(subgraph)
    avg_clustering_coefficient = nx.average_clustering(subgraph)
    avg_shortest_path_length = nx.average_shortest_path_length(subgraph)

    print("\nGraph Features:")
    print(f"Diameter: {diameter}")
    if nx.is_directed(subgraph):
        print(f"Average Out Degree: {avg_degree[0]:.4f}")
        print(f"Average In Degree: {avg_degree[1]:.4f}")
    else:
        print(f"Average Degree: {avg_degree:.4f}")
    print(f"Average Clustering Coefficient: {avg_clustering_coefficient:.4f}")
    print(f"Average Shortest Path Length: {avg_shortest_path_length:.4f}")

    print("\nNode Features:")
    for node in subgraph.nodes:
        print(f"Node {node}: "
              f"Degree Centrality: {degree_centralities[node]:.4f}, "
              f"Closeness Centrality: {closeness_centralities[node]:.4f}, "
              f"Betweenness Centrality: {betweenness_centralities[node]:.4f}, "
              f"Clustering Coefficient: {clustering_coefficients[node]:.4f}")

    k = 10

    top_k_degree_nodes = getTopKNodes(degree_centralities, k)
    print(f"\nTop {k} nodes with highest degree centrality:")
    for node in top_k_degree_nodes:
        print(f"Node {node}: "
              f"Degree Centrality: {degree_centralities[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['blue' if node in top_k_degree_nodes else 'green' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest degree centrality")

    top_k_closeness_nodes = getTopKNodes(closeness_centralities, k)
    print(f"\nTop {k} nodes with highest closeness centrality:")
    for node in top_k_closeness_nodes:
        print(f"Node {node}: "
              f"Closeness Centrality: {closeness_centralities[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['blue' if node in top_k_closeness_nodes else 'green' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest closeness centrality")

    top_k_betweenness_nodes = getTopKNodes(betweenness_centralities, k)
    print(f"\nTop {k} nodes with highest betweenness centrality:")
    for node in top_k_betweenness_nodes:
        print(f"Node {node}: "
              f"Betweenness Centrality: {betweenness_centralities[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['blue' if node in top_k_betweenness_nodes else 'green' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest betweenness centrality")

    top_k_clustering_nodes = getTopKNodes(clustering_coefficients, k)
    print(f"\nTop {k} nodes with highest clustering coefficient:")
    for node in top_k_clustering_nodes:
        print(f"Node {node}: "
              f"Clustering Coefficient: {clustering_coefficients[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['blue' if node in top_k_clustering_nodes else 'green' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest clustering coefficient")

    a, b, c, d = 1, 1, 1, 1
    combination_node_features = {}
    for node in subgraph.nodes:
        combination_node_features[node] = (a * degree_centralities[node] + b * closeness_centralities[node] +
                                           c * betweenness_centralities[node] + d * clustering_coefficients[node])
    top_k_combination = getTopKNodes(combination_node_features, k)
    print(f"\nTop {k} nodes with highest combination of node features:")
    for node in top_k_combination:
        print(f"Node {node}: "
              f"Clustering Coefficient: {combination_node_features[node]:.4f}, "
              f"Node Label: {subgraph.nodes[node]['label']}")
    node_colors = ['blue' if node in top_k_combination else 'green' for node in subgraph.nodes]
    plot_colered_graph(subgraph, node_colors, f"\nTop {k} nodes with highest combination of node features")

    # # Define thresholds for centrality measures
    # closeness_threshold = 0.6  # Adjust as needed
    # betweenness_threshold = 0.05  # Adjust as needed
    #
    # # Alternative 1: Degree-based
    # degree_threshold = 10  # Adjust as needed
    # good_investments = [node for node, degree in subgraph.degree() if degree > degree_threshold]
    # bad_investments = [node for node, degree in subgraph.degree() if degree < degree_threshold]
    # print("\nNeighborhoods for Investment based on the Degree of a node:")
    # print(f"Good Investments: {good_investments}")
    # print(f"Bad Investments: {bad_investments}")
    #
    # # Alternative 2: Clustering Coefficient-based
    # clustering_coefficient_threshold = 0.7  # Adjust as needed
    # good_investments = [node for node, cc in nx.clustering(subgraph).items() if cc > clustering_coefficient_threshold]
    # bad_investments = [node for node, cc in nx.clustering(subgraph).items() if cc < clustering_coefficient_threshold]
    # print("\nNeighborhoods for Investment based on Clustering Coefficient:")
    # print(f"Good Investments: {good_investments}")
    # print(f"Bad Investments: {bad_investments}")
    #
    # # Alternative 3: Clustering Coefficient-based
    # degree_threshold = 10  # Adjust as needed
    # clustering_coefficient_threshold = 0.7  # Adjust as needed
    #
    # # Unpack the tuples and extract degree and clustering coefficient
    # good_investments = [node for node, (node_degree, cc) in zip(subgraph.nodes, subgraph.degree()) if
    #                     int(node_degree) > degree_threshold and cc > clustering_coefficient_threshold]
    # bad_investments = [node for node, (node_degree, cc) in zip(subgraph.nodes, subgraph.degree()) if
    #                    int(node_degree) < degree_threshold or cc < clustering_coefficient_threshold]
    #
    # print("\nNeighborhoods for Investment based on a Combination:")
    # print(f"Good Investments: {good_investments}")
    # print(f"Bad Investments: {bad_investments}")
    #
    # plt.figure()
    # nx.draw(subgraph, with_labels=True, font_weight='bold')
    # plt.title(f"Strongly Connected Component {component_number}")
    # plt.show()


def calculateAnalytics(model):
    print("Analysing " + model.NAME + " network\n")
    graph = model.graph
    if nx.is_directed(graph):
        if nx.is_strongly_connected(graph):
            print('Graph is strongly connected!')
            analyzeConnectedComponent(graph, 1)
        else:
            print("Graph is not strongly connected.")
            components = list(nx.strongly_connected_components(graph))
            print("Connected Components:", components)
            # Analyze each strongly connected component separately
            for i, scc in enumerate(components):
                subgraph = graph.subgraph(scc)
                analyzeConnectedComponent(subgraph, i + 1)
    else:
        if nx.is_connected(graph):
            print('Graph is connected!')
            analyzeConnectedComponent(graph, 1)
        else:
            print("Graph is not connected.")
            components = list(nx.connected_components(graph))
            print("Connected Components:", components)
            # Analyze each strongly connected component separately
            for i, scc in enumerate(components):
                subgraph = graph.subgraph(scc)
                analyzeConnectedComponent(subgraph, i + 1)

    print("\n\n\n------------------------------------------------------------------\n\n\n")
