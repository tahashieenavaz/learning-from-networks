from models.Paris import Paris
from models.London import London
from models.SaoPaulo import SaoPaulo
from helpers.CalculateAnalytics import calculateAnalytics
import matplotlib.pyplot as plt
import networkx as nx


def main():
    paris = Paris()
    london = London()
    saopaulo = SaoPaulo()

    print(paris.graph)
    print(london.graph)
    print(saopaulo.graph)

    # paris.show()
    # saopaulo.show()
    london.show()

    # calculateAnalytics(paris.graph)
    # calculateAnalytics(saopaulo.graph)
    calculateAnalytics(london.graph)


if __name__ == "__main__":
    main()
