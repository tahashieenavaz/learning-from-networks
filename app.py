from models.Paris import Paris
from models.London import London
from models.SaoPaulo import SaoPaulo


def main():
    paris = Paris()
    london = London()
    saopaulo = SaoPaulo()

    print(paris.graph)
    print(london.graph)
    print(saopaulo.graph)


if __name__ == "__main__":
    main()
