from models.Paris import Paris
from models.London import London
from models.SaoPaulo import SaoPaulo
from helpers.CalculateAnalytics import calculate_analytics


def main():
    # getting models from datasets
    paris = Paris()
    london = London()
    saopaulo = SaoPaulo()

    # calculate analytics
    calculate_analytics(paris)
    calculate_analytics(london)
    calculate_analytics(saopaulo)


if __name__ == "__main__":
    main()
