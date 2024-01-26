from models.Paris import Paris
from models.London import London
from models.SaoPaulo import SaoPaulo
from helpers.CalculateAnalytics import calculateAnalytics


def main():
    paris = Paris()
    london = London()
    saopaulo = SaoPaulo()

    calculateAnalytics(paris)
    calculateAnalytics(london)
    calculateAnalytics(saopaulo)


if __name__ == "__main__":
    main()
