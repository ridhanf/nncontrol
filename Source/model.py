import pandas as pd
import pickle

# Memasukkan dataset ke dalam program.
data = pd.read_excel('dataAll.xlsx')

# Memisahkan data input dan data target.
# Data Input
X = data[['Heater','AC','To','Radiation']]
# Data Target
target = data[['Td','RH']]

# Memisahkan data pelatihan (training), data validasi (validation), dan data pengujian (testing).
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score

# Memisahkan 20% menjadi data tes
X_temp, X_test, y_temp, y_test = train_test_split(X, target, test_size=0.05, shuffle=True, random_state=15)

# Memisahkan 20% menjadi data validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=(15/95), shuffle=True, random_state=2019)

# Menghapus data temporary
del X_temp, y_temp

# Load from file
print("Memuat model JST...")
pkl_filename = "trained_model.pkl"
with open(pkl_filename, 'rb') as file:
    saved_model = pickle.load(file)
    print("Model JST berhasil dimuat!")

# Memprediksi
y_pred = saved_model.predict(X_test)
y_target = y_test

# Menghitung kinerja
EVar = round(explained_variance_score(y_target, y_pred)*100,2)
R    = round(r2_score(y_target, y_pred)**0.5*100,2)
RMSE = round(mean_squared_error(y_target, y_pred)**0.5,2)
MAE  = round(mean_absolute_error(y_target, y_pred),2)

# print errors as report
print('Score = {}% R = {}% RMSE = {} MAE = {}'.format(EVar, R, RMSE, MAE))
print()
print('Td : Score = {}% RMSE = {} MAE = {} Mean = {} Std = {}'.format(EVar_Td, RMSE_Td, MAE_Td, Mean_Td, Std_Td))
print('RH : Score = {}% RMSE = {} MAE = {} Mean = {} Std = {}'.format(EVar_RH, RMSE_RH, MAE_RH, Mean_RH, Std_RH))
print()