import pandas as pd
import numpy as np

path = r'C:\Users\victo\Aarhus Universitet\Test - Dokumenter\Elektronik\Noter Elektronik\Elektronik 6. semester\ITMAL\ITMAL - Exercises\Aflevering4\ship_data\shipsnet.json'


def load_ship_data_numpy_array():
    df = pd.read_json(path)
    data = np.array(df)
    return data


def get_path():
    return path


