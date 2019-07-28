from preprocessing import read_data
import sys
from sklearn import cluster

def kmeans(data):
    for i in range(2,15):
        model = cluster.KMeans(n_clusters=i, random_state=42).fit(data.values)
        print("Sum of squared distances for k = " + str(i) + ": "+ str(model.inertia_))

def main():
    if len(sys.argv) != 2:
        print("python3 kmeans_ssd.py filename")
        sys.exit(1)

    data = read_data(sys.argv[1])
    kmeans(data)


if __name__ == "__main__":
    main()