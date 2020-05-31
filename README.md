# DESIGN AND BUILT ARTIFICITAL NEURAL NETWORK FOR THERMAL ENVIRONMENT CONTROL OF CLIMATE CHAMBER



## DATA
Source     : [data.xlsx](https://github.com/ridhanf/nncontrol/blob/master/Data/data.xlsx)



## SYSTEM IDENTIFICATION
### Method     : NARX (Nonlinear Autoregressive with Exogenous Input)
- Library &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : [fireTS](https://pypi.org/project/fireTS/). The documentation can be found [here](https://firets.readthedocs.io/en/latest/)
- Notebook                               : [model_NARX.ipynb](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/model_NARX.ipynb)
- Source  &nbsp;&nbsp;&nbsp;&nbsp;       : [model_training.py](https://github.com/ridhanf/nncontrol/blob/master/Source/model_training.py)



## CONTROL DESIGN
### Method     : Neural Predictive Control (NN-MPC)
Option 1
- Library &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : Optimization menggunakan ([APMonitor](https://apmonitor.com/pdc/index.php/Main/ModelPredictiveControl))
- Notebook                               : [MPC-SISO.ipynb](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/MPC-SISO.ipynb) (Not Done Yet). The result is [here](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/results_0%20(SISO%201%20SP).mp4).
- Source  &nbsp;&nbsp;&nbsp;&nbsp;       : 

Option 2
- Library &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : Optimization menggunakan [CVXPY](https://www.cvxpy.org/)). Example: [MPC_sample.ipynb](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/MPC_sample.ipynb)
- Notebook                               :
- Source  &nbsp;&nbsp;&nbsp;&nbsp;       :

### Method     : NARMA-L2 Control
- Library &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :
- Notebook                               :
- Source  &nbsp;&nbsp;&nbsp;&nbsp;       :