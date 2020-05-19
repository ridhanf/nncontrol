# Import needed library
import pandas as pd
import pickle
from scipy.optimize import minimize

# Import dataset
data = pd.read_excel('modelData.xlsx')

y = data.loc[:, ['Td','RH'] ]
X = data.loc[:, ['HT','AC','To','RD'] ]

# Load from file
print("Memuat model JST...")
pkl_filename = "model.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)
    print()
    print("Model JST berhasil dimuat!")

# Optimization Variables
ym = model.predict(X, y.Td, step=1) # network model response
yr = data.loc[:, ['Td_SP'] ]        # desired response
u0 = X                              # initial control signal
rho = 0.3                           # rho

# Performance Criterion Function
def J(u_):
    f = (yr - ym)**2 + rho * (u_)**2
    return f

res = minimize(J, u0, method='BFGS', options={'gtol': 1e-6, 'disp': True})

print("res.x =",res.x)

print(res.message)

print("res.ess_inv =",res.hess_inv)

print()
print(res)
