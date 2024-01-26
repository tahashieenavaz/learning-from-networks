from Model import Model


class Paris(Model):
    NAME = "Paris"

    def __init__(self):
        super().__init__()
        self.setFileLocation("./graphs/Paris.json")
        self.loadGraph()
