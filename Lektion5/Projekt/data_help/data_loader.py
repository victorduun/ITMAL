import pandas as pd
import numpy as np

path = r'C:\Users\victo\Aarhus universitet\Test - Dokumenter\Elektronik\Noter Elektronik\Elektronik 6. semester\ITMAL\ITMAL - Exercises\Lektion5\Projekt\housing.csv'


def load_housing_data():
    df = pd.read_csv(path, sep=',')
    data = np.array(df)
    return data


def load_housing_labels():
    df = pd.read_csv(path, header=None, nrows=1)
    labels = np.array(df)
    return labels.ravel()


def get_path():
    return path
