import pandas as pd
import pickle

# Memasukkan dataset ke dalam program.
data_loc = '../Data/dataAll.xlsx'
data = pd.read_excel(data_loc)

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

# Menghitung nilai RMSE dan R^2
rmse_test = mean_squared_error(y_test, y_pred)**0.5
R2_test = r2_score(y_test, y_pred)

# Menampilkan nilai RMSE dan R^2
# print errors as report
print()
print("Hasil Evaluasi Model")
print('Test: RMSE {} | R^2 {}'.format(round(rmse_test,3), round(R2_test,3)))
