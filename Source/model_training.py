# Import needed libraries
from fireTS.models import NARX
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

# Import dataset
data = pd.read_excel('dataAll.xlsx')

y = data.loc[:, ['Td','RH'] ]
X = data.loc[:, ['HT','AC','To','RD','Td','RH'] ]

# Split dataset
# Data test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.05, shuffle=False, random_state=15)
# Data train and Data validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=(15/95), shuffle=False, random_state=2019)
# delete temporary data
del X_temp, y_temp

# print proportions
print('train: {}% | validation: {}% | test {}%'.format(round(len(y_train)/len(target)*100,2),
                                                        round(len(y_val)/len(target)*100,2),
                                                        round(len(y_test)/len(target)*100,2)))

ask_train = input("Train the model? (y/n):")
if ask_train == 'y':
    # Model design (MLP-NARX)
    mdl_MLP = MLPRegressor(random_state = 1, hidden_layer_sizes=(91), max_iter = 5000)

    p_value, q_value, d_value = 1, [3]*6, [0]*6
    mdl_NARX = NARX(mdl_MLP, auto_order=p_value, exog_order=q_value, exog_delay=d_value)

    # Model Training
    print('Training Model JST...')
    mdl_NARX.fit(X_train, y_train.Td)
    print()

    # Prediction
    y_pred = mdl_NARX.predict(X_val, y_val.Td, step=1)
    
    # Performance Evaluation
    R2 = mdl_NARX.score(X_val, y_val.Td, method='r2')
    RMSE = mdl_NARX.score(X_val, y_val.Td, method='mse')**0.5
    print("R2 = {} | RMSE = {}".format(R2,RMSE))

    ask_simpan = input("Simpan model? (y/n):")
    if ask_simpan == 'y':
        print('Menyimpan model JST...')
        # Menyimpan model yang sudah dibuat
        import pickle

        pkl_filename = "trained_model.pkl"
        with open(pkl_filename, 'wb') as file:
            pickle.dump(model, file)
            print('Model JST tersimpan!')
