import networkx as nx
import json


class Model:
    def __init__(self):
        self.file = None
        self.graph = None

    def setFileLocation(self, location: str):
        self.file = location

    def panic(self, message):
        raise Exception(f"Panic: {message}")

    def panicIfFileNotLoaded(self):
        if not self.file:
            self.panic("Graph file NOT set")

    def loadGraph(self):
        self.panicIfFileNotLoaded()

        with open(self.file) as handler:
            data = json.loads(handler.read())
            self.graph = nx.DiGraph()
            self.graph.add_nodes_from(
                (node["id"], {"label": node["label"]}) for node in data["nodes"])
            self.graph.add_edges_from([(edge["source"], edge["target"])
                                       for edge in data["links"]])
