from Model import Model


class SaoPaulo(Model):
    def __init__(self):
        self.setFileLocation("./graphs/SaoPaulo.json")
        self.loadGraph()
