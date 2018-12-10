import brml.*
load BearBullproblem

disp(pbear);

bear = 1;
bull = 2;

V = 1:100;

T = length(p);

%DEMOHMMROCKPAPERSCISSORS another HMM inference demo
close all
import brml.*
H = 2; % number of Hidden states
V = 100; % number of Visible states
T = 200; % length of the time-series
    
% Do filtering in the HMM to estimate the strategy the human is playing
ph1 = condp(ones(H,1)); % could be any strategy at timestep 1
for t=1:(T+1)
    phghm(bear, bear,t) = 0.8;
    phghm(bear, bull,t) = 0.2;
    phghm(bull, bear,t) = 0.3;
    phghm(bull, bull,t) = 0.7;
    pvgh(:,:,t)=zeros(V,H)+10e-10; 
    if t>1
        pvgh(:,bear,t)=pbear(:,p(1,t-1)); % random play strategy
        pvgh(:,bull,t)=pbull(:,p(1,t-1)); % do what you did last time % do different to human or computer
    end
end
t=T+1;
[alpha,loglik]=HMMforwardTimeDependent(p(1,1:T),phghm(:,:,1:T),ph1,pvgh(:,:,1:T));
pvtplus1_final = pvgh(:,:,t)*phghm(:,:,t)*alpha(:,t-1);% most likely next move by the human

values = 1:100
expected_revenue = sum((values - p(1,T))' .* pvtplus1_final);

    
    

