import matplotlib.pyplot as plt
import json


def read_data(path):
    times = []
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)['benchmarks']
        for item in data:
            time_in_ms = round(item['stats']['mean'], 3)
            times.append(time_in_ms)
    return times


def plot(results, label):
    integers = [1000, 2000, 5000, 7000, 10000]
    for result in results.items():
        plt.plot(integers, result[1], label=result[0])
    plt.title(label)
    plt.xlabel("Number of integers")
    plt.ylabel("Time in us")
    plt.xticks(integers)
    plt.legend()
    plt.savefig(label + '.png')
    plt.clf()


def main():

    data = read_data('results.json')
    results1 = {
        'creating BST': data[:5],
        'creating AVL': data[5:10]
    }
    results2 = {
        'finding BST': data[10:15],
        'finding AVL': data[15:20]
    }
    results3 = {
        'deleting BST': data[20:25],
        'deleting AVL': data[25:30]
    }
    plot(results1, "creating trees")
    plot(results2, "finding in trees")
    plot(results3, "deleting in trees")


if __name__ == '__main__':
    main()
