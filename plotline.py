import matplotlib.pyplot as plt

def tas_diagram(ax):
    # Ref: Le Bas et al. (1986) J. Petrol., 27: 745-750.
    # [x, y, name]
    names = [
                [39, 9, "Foidite"],
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

    for name in names:
        ax.text(*name, c="grey",
                horizontalalignment="center", verticalalignment="center",
                fontsize=8)


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    tas_diagram(ax)
    ax.set_xlim(35, 78)
    ax.set_ylim(0, 16)
    ax.set_xlabel("SiO$_2$ (wt.%)", fontsize=14)
    ax.set_ylabel("Na$_2$O + K$_2$O (wt.%)", fontsize=14)
    fig.savefig('sampleimage.jpg', dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    main()