import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter


class Model:
    """
    This class encapsulates common functionality for loading and drawing graphs.
    """
    def __init__(self):
        self.file = None
        self.graph = None
        self.isDrawn = False

    def setFileLocation(self, location: str):
        self.file = location

    def panic(self, message):
        raise Exception(f"Panic: {message}")

    def panicIfFileNotLoaded(self):
        if not self.file:
            self.panic("Graph file NOT set")

    def draw(self):
        if not self.isDrawn:
            edge_labels = {(u, v): d['weight']
                           for u, v, d in self.graph.edges(data=True)}
            pos = nx.spring_layout(self.graph)
            nx.draw(self.graph, pos, with_labels=True, font_weight='bold',
                    node_size=700, node_color='skyblue', font_size=10)
            nx.draw_networkx_edge_labels(
                self.graph, pos, edge_labels=edge_labels, font_color='red')
            self.isDrawn = True

    def show(self):
        self.draw()
        plt.show()

    def loadGraph(self):
        self.panicIfFileNotLoaded()

        with open(self.file) as handler:
            data = json.loads(handler.read())
            self.graph = nx.DiGraph()
            self.graph.add_nodes_from(
                (node["id"], {"label": node["label"]}) for node in data["nodes"])
            self.graph.add_weighted_edges_from([(edge["source"], edge["target"], edge["weight"])
                                                for edge in data["links"]])
