## DESIGN AND BUILT ARTIFICITAL NEURAL NETWORK FOR THERMAL ENVIRONMENT CONTROL OF CLIMATE CHAMBER
DISCLAIMER: This research and source code are under development.
<br />


### DATA
- Source     : [data.xlsx](https://github.com/ridhanf/nncontrol/blob/master/Data/data.xlsx)
<br    />

### SYSTEM IDENTIFICATION
#### Method     : NARX (Nonlinear Autoregressive with Exogenous Input)
- Paper   &nbsp;&nbsp;&nbsp;&nbsp; :
- Library &nbsp;&nbsp;&nbsp;       : [fireTS](https://pypi.org/project/fireTS/) (The documentation can be found [here](https://firets.readthedocs.io/en/latest/))
- Notebook                         : [model_NARX](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/model_NARX.ipynb)
- Source  &nbsp;&nbsp;&nbsp;       : [model_training](https://github.com/ridhanf/nncontrol/blob/master/Source/model_training.py)
<br />

### CONTROL DESIGN
#### Method     : Neural Predictive Control (NN-MPC)
Option 1
- Paper   &nbsp;&nbsp;&nbsp;&nbsp; :
- Library &nbsp;&nbsp;&nbsp;       : [APMonitor](https://apmonitor.com/pdc/index.php/Main/ModelPredictiveControl)(Optimization)
- Notebook                         : [MPC-SISO](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/MPC-SISO.ipynb) (_under development_). The result is [here](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/results_0%20(SISO%201%20SP).mp4).
- Source  &nbsp;&nbsp;&nbsp;       : 

Option 2
- Paper   &nbsp;&nbsp;&nbsp;&nbsp; :
- Library &nbsp;&nbsp;&nbsp;       : [CVXPY](https://www.cvxpy.org/)(Optimization). Ex1: [control](https://colab.research.google.com/github/cvxgrp/cvx_short_course/blob/master/intro/control.ipynb) Ex2: [MPC_sample](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/MPC_sample.ipynb)
- Notebook                         : [FeedbackLinearization](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/FeedbackLinearization.ipynb). Optmizer is _under development_.
- Source  &nbsp;&nbsp;&nbsp;       :
<br />

#### Method     : NN as Controller
- Paper   &nbsp;&nbsp;&nbsp;&nbsp; : [NEURAL NETWORK CONTROLLER FOR AN ANTHROPOMORPHIC HAND PROSTHESIS](https://www.researchgate.net/publication/229028417_NEURAL_NETWORK_CONTROLLER_FOR_AN_ANTHROPOMORPHIC_HAND_PROSTHESIS)
- Library &nbsp;&nbsp;&nbsp;       : 
- Notebook                         : [NN_Control](https://github.com/ridhanf/nncontrol/blob/master/Notebooks/NN_Control.ipynb) (_under development_)
- Source  &nbsp;&nbsp;&nbsp;       : 
<br />

For research writing can be found [here](https://github.com/ridhanf/Penulisan-Skripsi/blob/master/Latex/skripsi.pdf) in Bahasa Indonesia.