from sklearn import cluster
import preprocessing, sys
import joblib

_cluster_size = 10


def birch_clustering(data, filename):
    print("Executing birch...")
    model = cluster.Birch(n_clusters=_cluster_size).fit(data.values)
    cluster_ids = model.labels_
    with open("results/birch_" + filename[4:-4] + "_model.txt", "w") as model_output:
        for gene, id in zip(data.index.values, cluster_ids):
            model_output.write(str(gene) + ": " + str(id) + "\n")
    print("Counting cluster size...")
    cluster_size = {i: 0 for i in range(_cluster_size)}
    for id in cluster_ids:
        cluster_size[id] += 1
    print("Final results...")
    for cid, csize in cluster_size.items():
        print("Size of " + str(cid) + " is:\t" + str(csize))

    joblib.dump(model, "models/birch_" + filename[4:-4] + "_model.sav")
    return

def main():
    if len(sys.argv) != 2:
        print("python3 filepath")
        sys.exit(1)
    data = preprocessing.read_data(sys.argv[1])
    birch_clustering(data, sys.argv[1])
    return

if __name__ == "__main__":
    main()