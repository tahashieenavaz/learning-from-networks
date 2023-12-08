from Model import Model


class SaoPaulo(Model):
    def __init__(self):
        super().__init__()
        self.setFileLocation("./graphs/SaoPaulo.json")
        self.loadGraph()
