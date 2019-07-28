import pandas as pd, numpy as np
import preprocessing
def main():
    first = preprocessing.read_data("018/first_file_preprocessed.csv")
    second = preprocessing.read_data("019/second_file_preprocessed.csv")

    idx = np.intersect1d(first.index, second.index)
    print(len(idx))

if __name__ == "__main__":
    main()