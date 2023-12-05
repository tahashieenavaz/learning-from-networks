from Model import Model


class London(Model):
    def __init__(self):
        self.setFileLocation("./graphs/London.json")
        self.loadGraph()
