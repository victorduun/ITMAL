import matplotlib.pyplot as plt
from data_help import data_loader

data = data_loader.load_housing_data()


labels = data_loader.load_housing_labels()
median_income = data[:,7]


plt.hist(median_income, 30)

plt.show()

