from Model import Model


class Paris(Model):
    def __init__(self):
        self.setFileLocation("./graphs/Paris.json")
        self.loadGraph()
