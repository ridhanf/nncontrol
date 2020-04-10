# Import needed libraries
import numpy as np
import pandas as pd

# Memasukkan dataset ke dalam program.
data = pd.read_excel('../Data/dataAll.xlsx')

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

# print proportions
print('train: {}% | validation: {}% | test {}%'.format(round(len(y_train)/len(target)*100,2),
                                                       round(len(y_val)/len(target)*100,2),
                                                       round(len(y_test)/len(target)*100,2)))
ask_train = input("Train the model? (y/n):")
if ask_train == 'y':
    # Impor pustaka
    from sklearn.neural_network import MLPRegressor

    # Pembuatan model
    model = MLPRegressor(random_state = 1, hidden_layer_sizes=(91), max_iter = 5000, alpha = 0.0001)
    print("Parameter Model...")
    print(model.get_params)
    print()

    # Melakukan pelatihan (training) menggunakan 'fit'
    print('Training Model JST...')
    model.fit(X_train, y_train)
    print()

    # Prediksi model
    y_pred = model.predict(X_train)
    y_pred = pd.DataFrame(y_pred, columns=['Td_pred','RH_pred'])
    y_target = y_train
    
    # Membuat DataFrame hasil
    y_target = y_target.reset_index()[['Td','RH']]
    training = pd.concat([y_target,y_pred], axis=1)
    training['e_Td'] = training.Td - training.Td_pred
    training['e_RH'] = training.RH - training.RH_pred

    # Menghitung kinerja
    EVar = round(explained_variance_score(y_target, y_pred)*100,2)
    R    = round(r2_score(y_target, y_pred)**0.5*100,2)
    RMSE = round(mean_squared_error(y_target, y_pred)**0.5,2)
    MAE  = round(mean_absolute_error(y_target, y_pred),2)
    
    # Menghitung nilai MAE, RMSE dan STDev
    EVar_Td = round(explained_variance_score(y_train.Td, y_pred.Td_pred)*100,2)
    RMSE_Td = round(mean_squared_error(y_train.Td, y_pred.Td_pred)**0.5,2)
    MAE_Td  = round(mean_absolute_error(y_train.Td, y_pred.Td_pred),2)
    Mean_Td = round(np.mean(training.e_Td),2)
    Std_Td  = round(np.std(training.e_Td),2)
    
    EVar_RH = round(explained_variance_score(y_train.RH, y_pred.RH_pred)*100,2)
    RMSE_RH = round(mean_squared_error(y_train.RH, y_pred.RH_pred)**0.5,2)
    MAE_RH  = round(mean_absolute_error(y_train.RH, y_pred.RH_pred),2)
    Mean_RH = round(np.mean(training.e_RH),2)
    Std_RH  = round(np.std(training.e_RH),2)
    
    # print errors as report
    print('Score = {}% R = {}% RMSE = {} MAE = {}'.format(EVar, R, RMSE, MAE))
    print()
    print('Td : Score = {}% RMSE = {} MAE = {} Mean = {} Std = {}'.format(EVar_Td, RMSE_Td, MAE_Td, Mean_Td, Std_Td))
    print('RH : Score = {}% RMSE = {} MAE = {} Mean = {} Std = {}'.format(EVar_RH, RMSE_RH, MAE_RH, Mean_RH, Std_RH))
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
