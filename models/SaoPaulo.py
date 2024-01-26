from Model import Model


class SaoPaulo(Model):
    NAME = "Sao Paulo"

    def __init__(self):
        super().__init__()
        self.setFileLocation("./graphs/SaoPaulo.json")
        self.loadGraph()
