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


def main():
    data = read_data('results.json')
    words = [1000, 2000, 5000, 10000]
    results = {
        'selection sort': data[:4],
        'quicksort': data[4:8],
        'bubble sort': data[8:12],
        'merge sort': data[12:]
    }
    for result in results.items():
        print(result)
        plt.plot(words, result[1], label=result[0])
    plt.title(label='Comparison of sort times')
    plt.xlabel("Number of words")
    plt.ylabel("Time in ns")
    plt.xticks(words)
    plt.legend()
    plt.savefig('sorting times.png')
    plt.show()


if __name__ == '__main__':
    main()
