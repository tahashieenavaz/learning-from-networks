import networkx as nx
import matplotlib.pyplot as plt


def analyzeConnectedComponent(subgraph, component_number):
    print(f"\nAnalyzing Strongly Connected Component {component_number}:")
    print(f"Nodes: {subgraph.nodes()}")
    print(f"Edges: {subgraph.edges()}")

    # Check if the component has more than one node
    if len(subgraph) > 1:
        closeness_centralities = nx.closeness_centrality(subgraph)
        betweenness_centralities = nx.betweenness_centrality(subgraph)
        clustering_coefficients = nx.clustering(subgraph)
        diameter = nx.diameter(subgraph)
        avg_clustering_coefficient = nx.average_clustering(subgraph)
        avg_shortest_path_length = nx.average_shortest_path_length(subgraph)

        print(f"Diameter: {diameter}")
        print(f"Average Clustering Coefficient: {avg_clustering_coefficient:.4f}")
        print(f"Average Shortest Path Length: {avg_shortest_path_length:.4f}")

        # Additional analysis incorporating centrality measures
        print("\nNode Centrality Measures:")
        for node in subgraph.nodes:
            print(f"Node {node}: "
                  f"Closeness Centrality: {closeness_centralities[node]:.4f}, "
                  f"Betweenness Centrality: {betweenness_centralities[node]:.4f}, "
                  f"Clustering Coefficient: {clustering_coefficients[node]:.4f}")

        # Define thresholds for centrality measures
        closeness_threshold = 0.6  # Adjust as needed
        betweenness_threshold = 0.05  # Adjust as needed

        # Alternative 1: Degree-based
        degree_threshold = 10  # Adjust as needed
        good_investments = [node for node, degree in subgraph.degree() if degree > degree_threshold]
        bad_investments = [node for node, degree in subgraph.degree() if degree < degree_threshold]
        print("\nNeighborhoods for Investment based on the Degree of a node:")
        print(f"Good Investments: {good_investments}")
        print(f"Bad Investments: {bad_investments}")

        # Alternative 2: Clustering Coefficient-based
        clustering_coefficient_threshold = 0.7  # Adjust as needed
        good_investments = [node for node, cc in nx.clustering(subgraph).items() if cc > clustering_coefficient_threshold]
        bad_investments = [node for node, cc in nx.clustering(subgraph).items() if cc < clustering_coefficient_threshold]
        print("\nNeighborhoods for Investment based on Clustering Coefficient:")
        print(f"Good Investments: {good_investments}")
        print(f"Bad Investments: {bad_investments}")

        # Alternative 3: Clustering Coefficient-based
        degree_threshold = 10  # Adjust as needed
        clustering_coefficient_threshold = 0.7  # Adjust as needed

        # Unpack the tuples and extract degree and clustering coefficient
        good_investments = [node for node, (node_degree, cc) in zip(subgraph.nodes, subgraph.degree()) if
                            int(node_degree) > degree_threshold and cc > clustering_coefficient_threshold]
        bad_investments = [node for node, (node_degree, cc) in zip(subgraph.nodes, subgraph.degree()) if
                           int(node_degree) < degree_threshold or cc < clustering_coefficient_threshold]

        print("\nNeighborhoods for Investment based on a Combination:")
        print(f"Good Investments: {good_investments}")
        print(f"Bad Investments: {bad_investments}")

        plt.figure()
        nx.draw(subgraph, with_labels=True, font_weight='bold')
        plt.title(f"Strongly Connected Component {component_number}")
        plt.show()


    else:
        print("Single-node component. Skipping analysis.")


def calculateAnalytics(graph):
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

    print("________")
