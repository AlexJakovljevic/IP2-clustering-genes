import preprocessing, sys
from sklearn import cluster
import joblib

_cluster_size = 11

def kmeans_fun(data, filename):
    print("Executing KMeans...")
    model = cluster.KMeans(n_clusters= _cluster_size, random_state=42).fit(data.values)
    cluster_ids = model.labels_
    with open("results/kmeans_" + filename[4:-4] + "_model.txt", "w") as model_output:
        for gene, id in zip(data.index.values, cluster_ids):
            model_output.write(str(gene) + ": " + str(id) + "\n")

    cluster_size = {i: 0 for i in range(_cluster_size)}
    for id in cluster_ids:
        cluster_size[id] += 1

    for cid, csize in cluster_size.items():
        print("Size of " + str(cid) + " is:\t" + str(csize))
    joblib.dump(model, "models/kmeans_" + filename[4:-4] + "_model.sav")


def main():
    if len(sys.argv) != 2:
        print("python3 filename")
        sys.exit(1)
    data = preprocessing.read_data(sys.argv[1])
    kmeans_fun(data, sys.argv[1])


if __name__ == "__main__":
    main()
