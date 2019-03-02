import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from colour_mapping import test_colors, map_values, max_value

test_colors()


flip = True
max_value = map_values(max_value)


def read_data(filename='data_to_plot.csv'):
    data=np.loadtxt(filename, delimiter=';', dtype='str')

    x_labels = data[0][1:]
    y_labels = []
    for l in data[1:]:
        y_labels.append(l[0])

    #print x_labels
    #print y_labels
    #print data
    #print len(x_labels)
    #print len(y_labels)
    numbers = [[np.nan] * len(x_labels)]*len(y_labels)
    numbers=np.array(numbers)
    #print numbers

    #fix german language specific "," to "." as decimal delimiter
    for row, line in enumerate(data[1:]):
        for col, el in enumerate(line[1:]):
            numbers[row, col] = float(el.replace(",", "."))
    #print numbers
    return x_labels, y_labels, numbers


def show_data_plots():
    for plt_idx,filename in enumerate(['cda', 'chs', 'CA _REST_for HCE Clustering_data']):
        #plt.figure()
        x_labels,y_labels,numbers = read_data("input/"+filename+".csv")

        if flip:
            #flip data
            tmp=x_labels
            x_labels=y_labels
            y_labels=tmp

        numbers = numbers.transpose()

        #mapping
        mapped_numbers = map_values(numbers)


        fig, ax = plt.subplots()
        im = ax.imshow(mapped_numbers, cmap="jet", vmax=max_value,vmin=0)

        # We want to show all ticks...
        ax.set_xticks(np.arange(len(x_labels)))

        ax.set_yticks(np.arange(len(y_labels)))
        # ... and label them with the respective list entries
        ax.set_xticklabels(x_labels)
        ax.set_yticklabels(y_labels)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(y_labels)):
            for j in range(len(x_labels)):
                text = ax.text(j, i, numbers[i, j],
                               ha="center", va="center", color="w")
        #fig.colorbar(im)
        ax.set_title(filename.split(".")[0])
        fig.tight_layout()
        fig.savefig("res/"+filename+".svg")
    plt.show()


# def read_exel(filename="CA _REST_for HCE Clustering.xlsx"):
#     import pandas as pd
#     df=pd.read_excel(filename, header=2)
#     print df
#     print df.keys()


if __name__=="__main__":
    #read_exel()
    show_data_plots()
