clear all; close all; clc % clear session
addpath('apm') % load APMonitor.com toolkit

s = 'http://byu.apmonitor.com';
a = 'velocity';

% clear prior application
apm(s,a,'clear all');

% load model and data
apm_load(s,a,'ferrari.apm');
csv_load(s,a,'ferrari.csv');

% specify MV / CV
apm_info(s,a,'MV','p');
apm_info(s,a,'CV','v');

% configuration parameters
apm_option(s,a,'nlc.imode',6);
apm_option(s,a,'nlc.nodes',3);

% turn on MV / CV
apm_option(s,a,'v.status',1);
apm_option(s,a,'p.status',1);

% tune controller
apm_option(s,a,'p.lower',0);
apm_option(s,a,'p.upper',100);
apm_option(s,a,'v.tau',5);
apm_option(s,a,'v.sphi',26);
apm_option(s,a,'v.splo',24);

% solve and retrieve results
output = apm(s,a,'solve'); disp(output);
y = apm_sol(s,a); z = y.x; 

% open web-viewer
apm_web(s,a);

% plot results
figure(1)

subplot(2,1,1)
plot(z.time,z.p,'b-','LineWidth',2)
legend('Pedal')
ylabel('Position (%)')
axis([0 30 -5 105])

subplot(2,1,2)
plot(z.time,z.v,'r.-','LineWidth',2)
hold on
plot(z.time,z.vtr_hi,'k-')
plot(z.time,z.vtr_lo,'k-')
axis([0 30 -5 30])
legend('Optimized','SP_{hi}','SP_{lo}')
ylabel('Velocity (m/s)')
xlabel('Time (sec)')