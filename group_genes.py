import sys

def main():
    with open(sys.argv[1], "r") as model:
        clusters = {i:[] for i in range(11)}
        print(clusters)
        for line in model:
            data = line.split(": ")
            clusters[int(data[1][:-1])].append(data[0])

        for key in clusters.keys():
            print("-------------------" + str(key) + "-------------------")
            print(clusters[key])
if __name__ == "__main__":
    main()