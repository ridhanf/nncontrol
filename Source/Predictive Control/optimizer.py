# Import needed library
import numpy as np
from scipy.optimize import minimize

yr  = 24 # desired response
ym  = 23 # network model response
# u_  = 0.5 # tentative control signal
rho = 0.3 # the contribution that the sum of the squares of the control increments

u0 = 0.5

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
