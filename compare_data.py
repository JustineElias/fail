import pandas as pd
import matplotlib.pyplot as plt

path_predicted_data = "data/che_sulfates_nocomp_trees"
predicted_data_df = pd.read_csv(path_predicted_data, sep=";")

path_real_data = "data/data_DataGEN.csv"
real_data_df = pd.read_csv(path_real_data, sep=";")

col_real = "che_sulfates"
print(real_data_df[col_real].describe())

col_predicted = "che_sulfates_nocomp_trees"
print(predicted_data_df[col_predicted].describe())

real_data_df[col_real].plot(kind='hist')
# plt.scatter([1, 2], [1, 2])
plt.show()
