import data_loader


def reload():
    #Reload module:
    import importlib
    from data_help import data_loader
    importlib.reload(data_loader)


reload()

ships = data_loader.load_ship_data()

X = ships.images
y = ships.labels

#%%
#Edge detection
from skimage import filters
import matplotlib.pyplot as plt
import numpy as np


#With ship
index_with_ship = np.where(y == 1)[0][0]
image_with_ship = X[index_with_ship]
edges_with_ship = filters.sobel(image_with_ship)

#Without ship
index_no_ship = np.where(y == 0)[0][0]
image_no_ship = X[index_no_ship]
edges_no_ship = filters.sobel(image_no_ship)

#Plot
f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(edges_with_ship)
axarr[0,0].set_title("With ship - sobel edge detection filter")
axarr[0,0].axis("off")


axarr[0,1].imshow(image_with_ship)
axarr[0,1].set_title("With ship - Raw")
axarr[0,1].axis("off")

axarr[1,0].imshow(edges_no_ship)
axarr[1,0].set_title("Without ship - sobel edge detection filter")
axarr[1,0].axis("off")

axarr[1,1].imshow(image_no_ship)
axarr[1,1].set_title("Without ship - Raw")
axarr[1,1].axis("off")

plt.show()
