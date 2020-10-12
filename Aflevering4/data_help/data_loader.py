import json
import numpy as np
from dataclasses import dataclass

path = r'C:\Users\victo\Aarhus Universitet\Test - Dokumenter\Elektronik\Noter Elektronik\Elektronik 6. semester\ITMAL\ITMAL - Exercises\Aflevering4\ship_data\shipsnet.json'


@dataclass
class ShipsData:
    images: np.array
    labels: np.array
    locations: np.array
    scene_ids: np.array


def load_ship_data() -> ShipsData:
    with open(path) as file:
        dataset = json.load(file)
        # dataset.keys() # - dict_keys(['data', 'labels', 'locations', 'scene_ids'])
        images = np.array(dataset["data"]).astype("uint8")
        labels = np.array(dataset["labels"]).astype("uint8")
        locations = np.array(dataset["locations"]).astype("float")
        scene_ids = np.array(dataset["scene_ids"]).astype("str")
        img_length = 80
        images = images.reshape(-1, 3, img_length, img_length).transpose([0, 2, 3, 1])
    ships = ShipsData(images, labels, locations, scene_ids)
    return ships


def get_path():
    return path
