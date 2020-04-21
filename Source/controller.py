# Import needed libraries
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score

## Import dataset
data = pd.read_excel('newData.xlsx')

y = data.loc[:, ['HT','AC'] ]
X = data.loc[:, ['To','RD','Td','RH'] ]

# Split dataset
# Data test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.05, shuffle=False, random_state=15)
# delete temporary data
del X_temp, y_temp

# Load from file
print("Memuat controller...")
pkl_filename = "controller.pkl"
with open(pkl_filename, 'rb') as file:
    controller = pickle.load(file)
    print()
    print("Controller berhasil dimuat!")

# Prediction
y_pred = controller.predict(X_test, y_test.AC, step=1)

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

# Performance Evaluation
EVar = round(kinerja(y_test.AC, y_pred, method='evar')*100, 2)
R2   = round(kinerja(y_test.AC, y_pred, method='r2')*100, 2)
RMSE = round(kinerja(y_test.AC, y_pred, method='mse')**0.5, 2)
MAE  = round(kinerja(y_test.AC, y_pred, method='mae'), 2)
print("Performance evaluation based on Test Data")
print("EVar = {}% | R2 = {}% | RMSE = {} | MAE = {}".format(EVar, R2, RMSE, MAE))
print()
