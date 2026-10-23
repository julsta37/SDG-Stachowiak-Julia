import matplotlib.pyplot as plt

from src.data_service import get_layer


def show_layer():
    layer = get_layer()

    if layer is None:
        return

    layer.plot()
    plt.show()