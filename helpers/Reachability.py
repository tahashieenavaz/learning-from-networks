import networkx as nx


def nonReachableNodes(graph):
    if nx.is_strongly_connected(graph):
        raise Exception("The graph is fully reachable")

    strongly_connected_components = list(
        nx.strongly_connected_components(graph))
    non_reachable_nodes = set(graph.nodes()) - \
        set.union(*strongly_connected_components)
    return non_reachable_nodes
