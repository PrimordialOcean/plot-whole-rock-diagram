import matplotlib.pyplot as plt
import numpy as np

def tas_diagram(ax):
    # Ref: Le Bas et al. (1986) J. Petrol., 27: 745-750.
    # [x, y, name]
    names = [
        [43, 10, "Foidite"],
        [43, 2, "Picro-\nbasalt"],
        [44, 6.5, "Tephrite\nBasanite"],
        [49, 9.5, "Phono-\ntephrite"],
        [53, 11.5, "Tephri-\nphonolite"],
        [57.5, 14, "Phonolite"],
        [49, 5.5, "Trachy-\nbasalt"],
        [53, 6.7, "Basaltic\ntrachy-\nandesite"],
        [57.5, 8.5, "Trachy-\nandesite"],
        [63, 11, "Trachyte"],
        [65.5, 8.5, "Trachydacite"],
        [48.5, 2.5, "Basalt"],
        [54.5, 3.5, "Basaltic\nandesite"],
        [60, 4, "Andesite"],
        [67, 4.5, "Dacite"],
        [73.5, 8, "Rhyolite"]
    ]

    for name in names:
        ax.text(*name, c="grey",
                horizontalalignment="center", verticalalignment="center",
                fontsize=7)

    # [[x1, x2], [y1, y2]]
    lines = [
        [[41, 41], [0, 7]],
        [[41, 52.5], [7, 14]],
        [[41, 45], [3, 3]],
        [[45, 49.4], [9.4, 7.3]],
        [[48.4, 53], [11.5, 9.3]],
        [[49, 57.6], [15.6, 11.7]],
        [[45, 45], [0, 5]],
        [[45, 63], [5, 14.6]],
        [[49.4, 52], [7.3, 5]],
        [[53, 57], [9.3, 5.9]],
        [[57.6, 63], [11.7, 7]],
        [[69, 69], [8, 13]],
        [[45, 52], [5, 5]],
        [[52, 69], [5, 8]],
        [[52, 52], [0, 5]],
        [[57, 57], [0, 5.9]],
        [[63, 63], [0, 7]], 
        [[69, 77], [8, 0]]
    ]

    for line in lines:
        ax.plot(*line, "-", c="grey", lw=0.5)

def kseries(ax):
    # Peccerillo&Taylor 1976
    # [x, y, name]
    names = [
        [50, 0.15, "Low-K\ntholeiite"],
        [54, 0.25, "Low-K\nbasaltic\nandesite"],
        [59.5, 0.2, "Low-K andesite"],
        [66.5, 0.3, "Low-K dacite"],
        [74, 0.4, "Low-K rhyolite"],
        [50, 0.9, "basalt"],
        [54, 1.1, "basaltic\nandesite"],
        [59.5, 1.5, "andesite"],
        [66.5, 2.2, "dacite"],
        [74, 2.3, "rhyolite"],
        [54, 2.0, "High-K\nbasaltic\nandesite"],
        [59.5, 2.7, "High-K andesite"],
        [66.5, 3.4, "High-K dacite"],
        [50, 2.7, "absarokite"],
        [54, 3.3, "shoshonite"],
        [58, 3.7, "banakite"]
    ]

    for name in names:
        ax.text(*name, c="grey",
                horizontalalignment="center", verticalalignment="center",
                fontsize=7)
    # [[x1, x2], [y1, y2]]
    lines = [
        [[52, 52], [0, 4.0]],
        [[56, 56], [0, 4.0]],
        [[63, 63], [0, 4.0]],
        [[70, 70], [0, 4.0]],
        [[48, 52], [0.3, 0.5]],
        [[52, 56], [0.5, 0.7]],
        [[56, 63], [0.7, 1.0]],
        [[63, 70], [1.0, 1.3]],
        [[70, 78], [1.3, 1.6]],
        [[48, 52], [1.2, 1.5]],
        [[52, 56], [1.5, 1.8]],
        [[56, 63], [1.8, 2.4]],
        [[63, 70], [2.4, 3.0]],
        [[48, 52], [1.6, 2.4]],
        [[52, 56], [2.4, 3.2]],
        [[56, 63], [3.2, 4.0]],
    ]
    for line in lines:
        if line == [[48, 52], [1.2, 1.5]]:
            ax.plot(*line, "--", c="grey", lw=0.5)
        else:
            ax.plot(*line, "-", c="grey", lw=0.5)

def kseries_andesite(ax):
    # Gill 1981
    # [x, y, name]
    names = [
        [57, 0.3, "low-K"],
        [57, 1.3, "medium-K"],
        [57, 2.5, "high-K"],
    ]
    for name in names:
        ax.text(*name, c="grey",
                horizontalalignment="center", verticalalignment="center",
                fontsize=12)
    # lines
    x = np.arange(53, 64)
    lm = 0.04545 * x - 1.864
    mh = 0.0818 * x - 2.754
    hs = 0.145 * x - 5.135
    lines = [
        [x, lm],
        [x, mh],
        [x, hs],
        [[53, 53], [0, 0.145 * 53 - 5.135]],
        [[57, 57], [0, 0.145 * 57 - 5.135]],
        [[63, 63], [0, 0.145 * 63 - 5.135]]
    ]
    for line in lines:
        ax.plot(*line, "-", c="grey", lw=0.5)

def thca(ax):
    # Miyashiro 1974
    # [x, y, name]
    names = [
        [70, 4.5, "TH"],
        [70, 4.0, "CA"],
    ]
    for name in names:
        ax.text(*name, c="grey",
                horizontalalignment="center", verticalalignment="center",
                fontsize=12)
    x = np.arange(48, 73)
    y = ( x - 42.8 ) / 6.4
    ax.plot(x, y, "-", c="grey", lw=0.5)


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #tas_diagram(ax)
    kseries(ax)
    #thca(ax)
    #kseries_andesite(ax)
    #ax.set_xlim(48, 78)
    ax.set_ylim(0, )
    ax.set_xlabel("SiO$_2$ (wt.%)", fontsize=14)
    ax.set_ylabel("FeO*/MgO", fontsize=14)
    fig.savefig('sampleimage.jpg', dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    main()