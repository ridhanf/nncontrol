# Import needed libraries
import numpy as np
import pandas as pd

# Memasukkan dataset ke dalam jupyter.
data_loc = '../../Data/dataAll.xlsx'
data = pd.read_excel(data_loc)

# Membuang fitur No, Time dan DT.
data.drop(['No','Variation'], axis =1)

# Memisahkan data input dan data target.
# Data Input
X = data[['Heater','AC','DrybulbT','Radiation']]
# Data Target
target = data[['AirT','RH']]

# Memisahkan data pelatihan (training) dan data pengujian (testing).
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Memisahkan 20% menjadi data tes
X_temp, X_test, y_temp, y_test = train_test_split(X, target, test_size=0.2, shuffle=True, random_state=15)

# Memisahkan 20% menjadi data validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, shuffle=False, random_state=2019)

# Menghapus data temporary
del X_temp, y_temp

# print proportions
print('train: {}% | validation: {}% | test {}%'.format(round(len(y_train)/len(target)*100,2),
                                                      round(len(y_val)/len(target)*100,2),
                                                      round(len(y_test)/len(target)*100,2)))

# Impor pustaka
from sklearn.neural_network import MLPRegressor

# Pembuatan model
model_mlp = MLPRegressor(random_state = 1, activation = 'relu', hidden_layer_sizes=(20,13), solver='adam', alpha=0.001, max_iter = 5000)
print(model_mlp.get_params)

# Melakukan pelatihan (training) menggunakan 'fit'
print('Training...')
model_mlp.fit(X_train, y_train)

# Menghitung nilai RMSE
rmse_train = mean_squared_error(y_train, model_mlp.predict(X_train))**0.5
rmse_validation = mean_squared_error(y_val, model_mlp.predict(X_val))**0.5
rmse_test = mean_squared_error(y_test, model_mlp.predict(X_test))**0.5

# Menampilkan nilai MSE dan R^2
# print errors as report
print('train rmse: {:5} | val rmse: {:6} | test rmse: {:7}'.format(round(rmse_train,3), round(rmse_validation,3), round(rmse_test,3)))
