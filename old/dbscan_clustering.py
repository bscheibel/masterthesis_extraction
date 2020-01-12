import numpy as np
import pandas
import csv
import order_bounding_boxes_in_each_block

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

def my_distance(x,y):
    blub = "ddd"
    return blub


def cluster(file_in, file_out):
    # #############################################################################
    data_df = pandas.read_csv("/home/bscheibel/PycharmProjects/engineering_drawings_extraction/temporary/list_to_csv_with_avg_points.csv", sep=";")
    data_df.head(3)
    data = data_df[["xavg_elem","yavg_elem","ausrichtung"]]
    #print(data)
    data = StandardScaler().fit_transform(data)

    # #############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps=0.075, min_samples=1, metric="euclidean").fit(data)
    #core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    #core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    print(data[labels == 0])
    data_df["cluster"] = labels

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(data, labels))

    # #############################################################################
    # Plot result
    """ort matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = data[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        xy = data[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()"""

    #print(data_df.head(3))
    #data_df.to_csv("values_clusteredfromPDF_GV12.csv")
    data_df.groupby('cluster')['element'].apply(' '.join).reset_index().to_csv("values_clusteredfromHTML_layout_LH.csv",sep=";")


def get_average_xy(list_input):
    csv_name = "temporary/list_to_csv_with_avg_points.csv"
    new_list = []
    resultFile = open(csv_name, 'w')
    wr = csv.writer(resultFile, delimiter=";")
    wr.writerow(["element", "xavg_elem","yavg_elem", "ausrichtung"])
    for element in list_input:
        xavg_elem = 0
        yavg_elem = 0
        y_min = 1000000
        y_max = 0
        x_min = 1000000
        x_max = 0
        for blub in element:
            xavg_elem += (float(blub[0]) + float(blub[2]))/2
            yavg_elem += (float(blub[1]) + float(blub[3]))/2
            if float(blub[1]) < y_min:
                y_min = float(blub[1])
                #print("y_min:",y_min)
            if float(blub[0]) < x_min:
                x_min = float(blub[0])
            if float(blub[3]) > y_max:
                y_max = float(blub[3])
            if float(blub[2]) > x_max:
                x_max = float(blub[2])
        if x_max-x_min > y_max-y_min:
            ausrichtung = 0
        else:
            ausrichtung = 1
        xavg_elem = xavg_elem/len(element)
        #print(xavg_elem)
        yavg_elem = yavg_elem/len(element)
        #element.extend([xavg_elem, yavg_elem])
        #print(element)
        #new_list.append(element)
        wr.writerow([element,xavg_elem,yavg_elem, ausrichtung])

    resultFile.close()
    #print(new_list)
    return csv_name


#cluster(33,33)
file = "/home/bscheibel/PycharmProjects/engineering_drawings_extraction/drawings/5152166_Rev04.html"
#file = "/home/bscheibel/PycharmProjects/engineering_drawings_extraction/drawings/5129275_Rev01-GV12.html"
#result = order_bounding_boxes_in_each_block.get_bound_box(file)
#get_average_xy(result)
cluster(33,33)