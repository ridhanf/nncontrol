# Import needed libraries
from fireTS.models import NARX
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score

# Import dataset
data = pd.read_excel('newData.xlsx')

y = data.loc[:, ['HT','AC'] ]
X = data.loc[:, ['To','RD','Td','RH'] ]

# Split dataset
# Data test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.05, shuffle=False, random_state=15)
# Data train and Data validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=(15/95), shuffle=False, random_state=2019)
# delete temporary data
del X_temp, y_temp

# print proportions
print()
print('train: {}% | validation: {}% | test {}%'.format(round(len(y_train)/len(y)*100,2),
                                                        round(len(y_val)/len(y)*100,2),
                                                        round(len(y_test)/len(y)*100,2)))
print()

# score function
def kinerja(y_target, y_pred, method="evar"):
    mask = np.isnan(y_target) | np.isnan(y_pred)
    if method == "evar":
        return explained_variance_score(y_target[~mask], y_pred[~mask])
    elif method == "r2":
        return r2_score(y_target[~mask], y_pred[~mask])
    elif method == "mse":
        return mean_squared_error(y_target[~mask], y_pred[~mask])
    elif method == "mae":
        return mean_absolute_error(y_target[~mask], y_pred[~mask])

# Main Program
ask_train = input("Train the controller? (y/n):")
if ask_train == 'y':
    # Control design (MLP-NARX)
    mdl_MLP = MLPRegressor(random_state = 1, hidden_layer_sizes=(91), max_iter = 5000)

    p_value, q_value, d_value = 1, [3]*4, [0]*4
    mdl_NARX = NARX(mdl_MLP, auto_order=p_value, exog_order=q_value, exog_delay=d_value)

    # Controller Training
    print('Training of Controller...')
    mdl_NARX.fit(X_train, y_train.AC)

    # Prediction
    y_pred = mdl_NARX.predict(X_val, y_val.AC, step=1)
    
    # Performance Evaluation
    EVar = round(kinerja(y_val.AC, y_pred, method='evar')*100, 2)
    R2   = round(kinerja(y_val.AC, y_pred, method='r2')*100, 2)
    RMSE = round(kinerja(y_val.AC, y_pred, method='mse')**0.5, 2)
    MAE  = round(kinerja(y_val.AC, y_pred, method='mae'), 2)
    print("Performance evaluation based on Validation Data")
    print("EVar = {}% | R2 = {}% | RMSE = {} | MAE = {}".format(EVar, R2, RMSE, MAE))
    print()

    ask_simpan = input("Simpan controller? (y/n):")
    if ask_simpan == 'y':
        print('Menyimpan controller...')
        # Menyimpan controller yang sudah dibuat
        import pickle

        pkl_filename = "controller.pkl"
        with open(pkl_filename, 'wb') as file:
            pickle.dump(mdl_NARX, file)
            print('Controller tersimpan!')
    else:
        print('Controller tidak disimpan.')
