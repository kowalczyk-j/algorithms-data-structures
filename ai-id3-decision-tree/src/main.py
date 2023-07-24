import pandas as pd
import numpy as np
from id3 import ID3
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def load_data(path):
    """Wczytuje dane z pliku csv, dyskretyzuje wartości ciągłe na 3 przedziały"""
    data = pd.read_csv(path, sep=';')
    data.drop('id', inplace=True, axis=1)
    mapping = {'age': [50*365, 50*365+1, 57*365, 57*365+1],
            'height': [160, 161, 169, 170],
            'weight': [67, 68, 79, 80],
            'ap_hi': [119, 120, 120, 121],
            'ap_lo': [79, 80, 80, 81]}
    for key, value in mapping.items():
        data[key] = np.where(data[key] <= value[0], 1, data[key])
        data[key] = np.where(data[key].between(value[1],value[2]), 2, data[key])
        data[key] = np.where(data[key] >= value[3], 3, data[key])
    return data

def split_data(data):
    """Zwraca dane podzielone na zbiór treningowy, walidacyjny, oraz testowy"""
    train, test_val = train_test_split(data, test_size=0.2)
    test, val = train_test_split(test_val, test_size=0.5)
    train_x, train_y = train.iloc[:, 0:-1], train.iloc[:, -1]
    val_x, val_y = val.iloc[:, 0:-1], val.iloc[:, -1]
    test_x, test_y = test.iloc[:, 0:-1], test.iloc[:, -1]
    return train_x, train_y, val_x, val_y, test_x, test_y

def plotter(data, n_attributes=12):
    """Tworzy wykres kolumnowy: procent dokładności predykcji dla każdego z 3 zbiorów"""
    fig, ax = plt.subplots()
    labels = ["zbiór treningowy", "zbiór walidacyjny", "zbiór testowy"]
    sets = split_data(data)

    for j in range(0, len(sets), 2):
        accuracy = []

        for i in range(n_attributes):
            tree = ID3(max_depth=i)
            tree.fit(sets[0], sets[1])
            result = tree.predict(sets[j])
            result['is_equal'] = np.where(result[sets[j+1].name] == sets[j+1], 1, 0)
            corectness = (result.sum(axis=0).loc['is_equal']/len(result.loc[:,'is_equal']))*100
            accuracy.append(corectness)
        
        ax.bar(np.arange(n_attributes) - 0.2+0.2*(j//2), accuracy, width=0.2, label=labels[j//2])

    plt.xlabel('Głębokość drzewa ID3')
    plt.ylabel('% poprawnie przewidzianych klas')
    plt.grid(True)
    plt.legend()
    plt.show()

def print_statistics(data, depth=9, set_type=4):
    outputs = []
    for i in range(15):
        sets = split_data(data)
        tree = ID3(max_depth=depth)
        tree.fit(sets[0], sets[1])
        result = tree.predict(sets[set_type])
        result['is_equal'] = np.where(result[sets[set_type+1].name] == sets[set_type+1], 1, 0)
        corectness = (result.sum(axis=0).loc['is_equal']/len(result.loc[:,'is_equal']))*100
        outputs.append(corectness)
    print(pd.Series(outputs).describe())

if __name__ == "__main__":
    data = load_data('data/cardio_train.csv')
    sets = split_data(data)
    #plotter(data)
    print_statistics(data)

    tree = ID3(sets[0], sets[1], max_depth=6)
    tree.fit()
    tree.predict(sets[2])

