import json
import networkx as nx
import matplotlib.pyplot as plt


class Model:
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
            nx.draw(self.graph, with_labels=True)
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
            self.graph.add_edges_from([(edge["source"], edge["target"])
                                       for edge in data["links"]])
