function p = ctrl_apm(v)

persistent s a icount

if (isempty(icount)),
    % -------------------------------------------
    % Setting up APMonitor
    % For any tutorials see 
    % http://apmonitor.com/wiki/index.php/Main/MATLAB
    % -------------------------------------------
    
    % Add path to APM libraries
    addpath('apm');
    
    % Select server and application name
    %s = 'http://byu.apmonitor.com';
    s = 'http://localhost';
    a = 'controller';
    
    % Clear previous application
    apm(s,a,'clear all');
    
    % load model variables and equations
    apm_load(s,a,'ferrari.apm');
    
    % load data
    csv_load(s,a,'ferrari10.csv');
    
    %  APM Variable Classification
    apm_info(s,a,'FV','k');
    apm_info(s,a,'FV','b');
    apm_info(s,a,'MV','p');
    apm_info(s,a,'CV','v');
    
    % Options
    apm_option(s,a,'nlc.imode',6);
    apm_option(s,a,'nlc.nodes',3);
    apm_option(s,a,'nlc.reqctrlmode',3);
    % Bounds on pedal position
    apm_option(s,a,'p.lower',0);
    apm_option(s,a,'p.upper',100);
    % Turn on parameters to control
    apm_option(s,a,'p.status',1);
    apm_option(s,a,'p.dmax',25);
    apm_option(s,a,'p.fstatus',0);
    apm_option(s,a,'v.status',1);
    apm_option(s,a,'v.fstatus',1);
    apm_option(s,a,'v.tau',5);
    
    % Initialize counter
    icount = 0;
end

icount = icount + 1;

% Input setpoint and measurements
apm_option(s,a,'v.sphi',v(1)+1);
apm_option(s,a,'v.splo',v(1)-1);
apm_meas(s,a,'v',v(2));

% Solve
output = apm(s,a,'solve');

% Output parameters
p(1) = apm_tag(s,a,'p.newval');

if (icount==5),
    % open web-viewer
    apm_web(s,a);
end

end
