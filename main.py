import matplotlib.pyplot as plt
import pandas as pd
import plotline

def main():
    # https://gbank.gsj.jp/volcano/Act_Vol/adatara/table/t3_3.htmlより引用
    filename = "adatara.csv"
    df = pd.read_csv(filename, encoding='utf-8', sep=',')
    df = df[df["Unit"] == "箕輪山ユニット（MI）"]
    elements = ["SiO2", "TiO2", "Al2O3", "FeO*", "MnO", "MgO", "CaO", "Na2O",
                "K2O", "P2O5"]
    df = df[elements]
    
    # read csv data and normalize
    def normalize(x):
        return 100 * x / df.sum(axis=1)
        
    norm_df = df.apply(normalize, axis=0)
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotline.tas_diagram(ax)
    ax.plot(norm_df["SiO2"], norm_df["Na2O"] + norm_df["K2O"], "o", mec="r", c="pink", label="MI")
    ax.set_xlabel("SiO$_2$ (wt.%)", fontsize=14)
    ax.set_ylabel("Na$_2$O + K$_2$O (wt.%)", fontsize=14)
    ax.legend(fancybox=False, edgecolor="k")
    fig.savefig('tasplot.jpg', dpi=300, bbox_inches='tight')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotline.kseries(ax)
    ax.plot(norm_df["SiO2"], norm_df["K2O"], "o", mec="r", c="pink", label="MI")
    ax.set_xlabel("SiO$_2$ (wt.%)", fontsize=14)
    ax.set_ylabel("K$_2$O (wt.%)", fontsize=14)
    ax.legend(fancybox=False, edgecolor="k")
    fig.savefig('kseries.jpg', dpi=300, bbox_inches='tight')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotline.kseries_andesite(ax)
    ax.plot(norm_df["SiO2"], norm_df["K2O"], "o", mec="r", c="pink", label="MI")
    ax.set_xlabel("SiO$_2$ (wt.%)", fontsize=14)
    ax.set_ylabel("K$_2$O (wt.%)", fontsize=14)
    ax.legend(fancybox=False, edgecolor="k")
    fig.savefig('kseries_andesite.jpg', dpi=300, bbox_inches='tight')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotline.thca(ax)
    ax.plot(norm_df["SiO2"], norm_df["FeO*"]/norm_df["MgO"], "o", mec="r", c="pink", label="MI")
    ax.set_xlabel("SiO$_2$ (wt.%)", fontsize=14)
    ax.set_ylabel("FeO*/MgO", fontsize=14)
    ax.legend(fancybox=False, edgecolor="k")
    fig.savefig('thca.jpg', dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    main()