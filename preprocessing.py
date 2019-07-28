import pandas as pd
import sys

def preprocessing(data):
    print("Preprocessing data...")
    return data.loc[(data != 0).any(axis=1)]

def read_data(filepath):
    print("Loading data...")
    with open(filepath) as file:
        data = pd.read_csv(file,
                           index_col='Name',
                           header=0,
                           delimiter=',')
    print("Data loaded.")
    return data

def write_data(data, filepath):
    print("Writing preprocessed data...")
    data.to_csv(filepath[:-4] + "_preprocessed.csv", index_col='Name', header=True)

def main():
    if len(sys.argv) != 2:
        print("python3 preprocessing.py filename")
        sys.exit(1)
    data = read_data(sys.argv[1])
    print(data)
    data = preprocessing(data)
    write_data(data, sys.argv[1])
    write_data(data.transpose(), sys.argv[1][:-4] + "_transposed")


if __name__ == "__main__":
    main()
