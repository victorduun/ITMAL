import json
import numpy as np
import inspect
import os
from dataclasses import dataclass
dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) #Current folder

datapath = os.path.join(dirname, '../../data/raw/shipsnet.json') 



@dataclass
class ShipsData:
    images: np.array
    labels: np.array
    locations: np.array
    scene_ids: np.array


def load_ship_data() -> ShipsData:
    print("Loading ship data from path: " + datapath)
    with open(datapath) as file:
        dataset = json.load(file)
        # dataset.keys() # - dict_keys(['data', 'labels', 'locations', 'scene_ids'])
        images = np.array(dataset["data"]).astype("uint8")
        labels = np.array(dataset["labels"]).astype("uint8")
        locations = np.array(dataset["locations"]).astype("float")
        scene_ids = np.array(dataset["scene_ids"]).astype("str")
        img_length = 80
        images = images.reshape(-1, 3, img_length, img_length).transpose([0, 2, 3, 1])
    ships = ShipsData(images, labels, locations, scene_ids)
    print("Ship data loaded")
    return ships


def load_ship_data_normalized() -> ShipsData:
    ships_data = load_ship_data()
    ships_data.images = ships_data.images/255
    return ships_data


def get_path():
    return datapath
