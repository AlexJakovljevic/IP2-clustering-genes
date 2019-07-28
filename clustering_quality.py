import sys, preprocessing
from sklearn import metrics
def get_labels(filepath):
    with open(filepath, "r") as model:
        labels = []
        for line in model:
            data = line.split(": ")
            labels.append(data[1])

    return labels

def main():
    if len(sys.argv) != 3:
        print("python clustering_quality.py filename labelsfilename")
        sys.exit(1)

    labels = get_labels(sys.argv[2])
    data = preprocessing.read_data(sys.argv[1])
    print(metrics.cluster.silhouette_score(X=data.values, labels=labels, metric='euclidean'))
if __name__ == "__main__":
    main()