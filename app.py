from models.Paris import Paris
from models.London import London
from models.SaoPaulo import SaoPaulo
from utils.CalculateAnalytics import calculateAnalytics
import matplotlib.pyplot as plt
import networkx as nx


def main():
    paris = Paris()
    london = London()
    saopaulo = SaoPaulo()

    print(paris.graph)
    print(london.graph)
    print(saopaulo.graph)
    nx.draw(paris.graph, with_labels=True)
    plt.show()
    nx.draw(london.graph, with_labels=True)
    plt.show()
    nx.draw(saopaulo.graph, with_labels=True)
    plt.show()

    calculateAnalytics(paris.graph)
    calculateAnalytics(london.graph)
    calculateAnalytics(saopaulo.graph)



if __name__ == "__main__":
    main()
