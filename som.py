import minisom, sys, preprocessing
from matplotlib import pyplot as plt
import joblib

def minisom_fun(data, filename):
    print("Executing SOM...")
    model = minisom.MiniSom(17, 17, len(data.values[1]))
    model.random_weights_init(data.values)
    model.train_random(data.values, 100)
    # model.train_batch(data.values, 100)
    plt.pcolor(model.distance_map().T)
    plt.show()
    joblib.dump(model, "models/som_" + filename[4:-4] + "_model.sav")

def main():
    if len(sys.argv) != 2:
        print("python3 filename")
        sys.exit(1)
    data = preprocessing.read_data(sys.argv[1])
    minisom_fun(data, sys.argv[1])

if __name__ == "__main__":
    main()