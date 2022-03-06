import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Table


def plot_table(data, fmt='{:.2f}'):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])

    nrows, ncols = data.shape
    width, height = 1.0 / ncols, 1.0 / nrows

    for (i, j), val in np.ndenumerate(data):

        if val == 0.:
            color = 'black'
        elif val == 1:
            color = 'green'
        else:
            color = 'yellow'

        tb.add_cell(i, j, width, height, text=fmt.format(val),
                    loc='center', facecolor=color)

    for i, label in enumerate(data.index):
        tb.add_cell(i, -1, width, height, text=label, loc='right',
                    edgecolor='none', facecolor='none')

    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height / 2, text=label, loc='center',
                    edgecolor='none', facecolor='none')
    ax.add_table(tb)
    return fig
