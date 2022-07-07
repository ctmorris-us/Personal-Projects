% h = .01;
% k = 1;
% m = 1;
% 
% numx = 1000;
% 
% x = zeros(1,numx);
% x(1) = 2;
% x(2) = 2.1;
% 
% for i = [2:numx-1]
%     x(i+1) = (2 - (h^2*k)/m) * x(i) - x(i-1);
% end
% 
% t = [0:h:1000*h - h];
% 
% plot(t, x)
% 

dtheta = .01;
numphi = 5000;
numtheta = numphi;

r = 5;
theta0 = pi/2;

phi = zeros(1, numphi);
theta = [theta0:dtheta:theta0 + dtheta*(numtheta-1)];

phi(1) = pi;
phi(2) = phi(1) + .001;

phip = phi(1);
phic = phi(2);
thetap = theta(1);
thetac = theta(2);

syms phi1 phi2 phi3 theta1 theta2

halfLagrange = symfun(r.*dtheta.*((sin(theta1).^2 .* 2 .* (phi2 - phi1) ./ dtheta.^2) ./ (1 + sin(theta1).^2 .* ((phi2 - phi1) ./ dtheta).^2)), [phi1, phi2, theta1]);
fullLagrange = symfun(halfLagrange(phi1, phi2, theta1) - halfLagrange(phi2, phi3, theta2), [phi1, phi2, phi3, theta1, theta2]);
FunctiontoMinimize = symfun(fullLagrange(phip, phic, phi3, thetap, thetac), [phi3]);

for i = [2:numtheta - 1]
    phip = phi(i-1);
    phic = phi(i);
    thetap = theta(i-1);
    thetac = theta(i);
    
    phif = fzero(FunctiontoMinimize, phic);
    phi(i+1) = phif;
    
end

x = r .* sin(theta) .* cos(phi);
y = r .* sin(theta) .* sin(phi);
z = r .* cos(theta);

plot3(x,y,z);
axis([-r, r, -r, r, -r, r]);