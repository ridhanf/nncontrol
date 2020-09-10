from apm import *

s = 'http://byu.apmonitor.com'
a = 'velocity'

# clear prior application
apm(s,a,'clear all')

# load model and data
apm_load(s,a,'ferrari.apm')
csv_load(s,a,'ferrari.csv')

# specify MV / CV
apm_info(s,a,'MV','p')
apm_info(s,a,'CV','v')

# configuration parameters
apm_option(s,a,'nlc.imode',6)
apm_option(s,a,'nlc.nodes',3)

# turn on MV / CV
apm_option(s,a,'v.status',1)
apm_option(s,a,'p.status',1)

# tune controller
apm_option(s,a,'p.lower',0)
apm_option(s,a,'p.upper',100)
apm_option(s,a,'v.tau',5)
apm_option(s,a,'v.sphi',26)
apm_option(s,a,'v.splo',24)

# solve and retrieve results
output = apm(s,a,'solve')
print(output)

# open web-viewer
apm_web(s,a)
