# Import needed libraries
from fireTS.models import DirectAutoRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score

# Import dataset
data = pd.read_excel('../Data/data.xlsx')

# y = data.loc[:, ['Td','RH'] ]
# X = data.loc[:, ['HT','AC','To','RD'] ]

y = data.loc[:, ['Td','RH'] ]
X = data.loc[:, ['HT','AC'] ]

# Split dataset
# Data test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.05, shuffle=False, random_state=15)
# Data train and Data validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=(15/95), shuffle=False, random_state=2019)

# print proportions
print()
print('Dataset splitting configuration')
print('Train: {}% | Validation: {}% | Test {}%'.format(round(len(y_train)/len(y)*100,2),
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
ask_train = input("Train the model? (y/n):")
if ask_train == 'y':
    # Model design (MLP-NARX)
    MLP_Td = MLPRegressor(random_state = 1, hidden_layer_sizes=(91), max_iter = 5000)
    MLP_RH = MLPRegressor(random_state = 1, hidden_layer_sizes=(91), max_iter = 5000)

    p_value, q_value, d_value = 1, [1]*2, [0]*2
    NARX_Td = DirectAutoRegressor(MLP_Td, auto_order=p_value, exog_order=q_value, exog_delay=d_value, pred_step=1)
    NARX_RH = DirectAutoRegressor(MLP_RH, auto_order=p_value, exog_order=q_value, exog_delay=d_value, pred_step=1)

    # Model Training
    print('Model (Td) training...')
    NARX_Td.fit(X_train, y_train.Td)
    print('Model (RH) training...')
    NARX_RH.fit(X_train, y_train.RH)

    # Prediction
    Td_pred = NARX_Td.predict(X_val, y_val.Td)
    RH_pred = NARX_RH.predict(X_val, y_val.RH)
    print()

    # Td Performance Evaluation
    EVar = round(kinerja(y_val.Td, Td_pred, method='evar')*100, 2)
    R2   = round(kinerja(y_val.Td, Td_pred, method='r2')*100, 2)
    RMSE = round(kinerja(y_val.Td, Td_pred, method='mse')**0.5, 2)
    MAE  = round(kinerja(y_val.Td, Td_pred, method='mae'), 2)
    print("Td Performance evaluation based on Validation Data")
    print("EVar = {}% | R2 = {}% | RMSE = {} | MAE = {}".format(EVar, R2, RMSE, MAE))
    print()

    # RH Performance Evaluation
    EVar = round(kinerja(y_val.RH, RH_pred, method='evar')*100, 2)
    R2   = round(kinerja(y_val.RH, RH_pred, method='r2')*100, 2)
    RMSE = round(kinerja(y_val.RH, RH_pred, method='mse')**0.5, 2)
    MAE  = round(kinerja(y_val.RH, RH_pred, method='mae'), 2)
    print("RH Performance evaluation based on Validation Data")
    print("EVar = {}% | R2 = {}% | RMSE = {} | MAE = {}".format(EVar, R2, RMSE, MAE))
    print()

    ask_simpan = input("Save the model? (y/n):")
    if ask_simpan == 'y':
        print('Saving NARX Model...')
        # Menyimpan model yang sudah dibuat
        import pickle

        with open("model_Td.pkl", 'wb') as file:
            pickle.dump(NARX_Td, file)
            print('NARX model (Td) saved!')

        with open("model_RH.pkl", 'wb') as file:
            pickle.dump(NARX_RH, file)
            print('NARX model (RH) saved!')
    else:
        print('Model not saved.')
else:
    print('Model not trained.')
