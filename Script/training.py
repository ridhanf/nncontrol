# Import needed libraries
import numpy as np
import pandas as pd

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

# Memisahkan 20% menjadi data validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, shuffle=True, random_state=2019)

# Menghapus data temporary
del X_temp, y_temp

# print proportions
print("Pembagian data")
print('train: {}% | validation: {}% | test {}%'.format(round(len(y_train)/len(target)*100,2),
                                                        round(len(y_val)/len(target)*100,2),
                                                        round(len(y_test)/len(target)*100,2)))

ask_train = input("Train the model? (y/n):")
if ask_train == 'y':
    # Impor pustaka
    from sklearn.neural_network import MLPRegressor

    # Pembuatan model
    model = MLPRegressor(random_state = 1, activation = 'relu', hidden_layer_sizes=(14,20), solver='adam', alpha=0.001, max_iter = 5000)
    print("Parameter Model...")
    print(model.get_params)
    print()

    # Melakukan pelatihan (training) menggunakan 'fit'
    print('Training Model JST...')
    model.fit(X_train, y_train)
    print()

    # Menghitung nilai RMSE dan R^2
    y_pred_train = model.predict(X_train)
    y_pred_val   =  model.predict(X_val)

    rmse_train = mean_squared_error(y_train, y_pred_train)**0.5
    rmse_validation = mean_squared_error(y_val, y_pred_val)**0.5
    
    R2_train = r2_score(y_train, y_pred_train)
    R2_validation = r2_score(y_val, y_pred_val)

    # Menampilkan nilai RMSE dan R^2
    # print errors as report
    print("Hasil Evaluasi Model")
    print('Train: RMSE {} | R2 {}'.format(round(rmse_train,3), round(R2_train,3)))
    print('Validation: RMSE {} | R2 {}'.format(round(rmse_validation,3), round(R2_validation,3)))
    print()

    ask_simpan = input("Simpan model? (y/n):")
    if ask_simpan == 'y':
        print('Menyimpan model JST...')
        # Menyimpan model yang sudah dibuat
        import pickle

        pkl_filename = "trained_model.pkl"
        with open(pkl_filename, 'wb') as file:
            pickle.dump(model, file)
            print('Model JST tersimpan!')
