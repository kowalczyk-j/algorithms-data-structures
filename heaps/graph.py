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
    integers = [1000, 2000, 5000, 7000, 10000, 20000, 50000, 100000]
    for result in results.items():
        plt.plot(integers, result[1], label=result[0], marker='o')
    plt.title(label)
    plt.xlabel("Number of integers")
    plt.ylabel("Time in us")
    plt.legend()
    plt.savefig(label + '.png')
    plt.clf()


def main():
    data = read_data('results.json')
    results1 = {
        'pushing to binary heap': data[:8],
        'pushing to threeary heap': data[16:24],
        'pushing to fourary heap': data[32:40]
    }
    results2 = {
        'popping off binary heap': data[8:16],
        'popping off threeary heap': data[24:32],
        'popping off fourary heap': data[40:48]
    }
    print(results1, results2)
    plot(results1, "pushing")
    plot(results2, "popping")


if __name__ == '__main__':
    main()
