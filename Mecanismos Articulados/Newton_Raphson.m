

%DADOS
a = 0.18;
b = 1;
u =1.1;
v = 0.6;
w = 0.22;
r = 0.2;
%w = 100; %isso é a velociade de theta
theta0 = pi*0.6;
vel_theta = -pi*(10/3);

N_it = 10; %numero de iteracoes
e  = 0.001; %máximo admissivel para zero de funcao
Dr = 1 ; % avaliar convergencia da solução
%INTERVALO DE RODAR O PROGRAMA
Tfinal = 60; %60 segundos
dt = 0.1; %frames a cada um segundo
k = 1; % inicializador da iteração
Fx  =1; % inicializador de zero da funcao
%vetores contendo os valores
theta =[];
alpha = [];
beta=[];
xx = [];
y =[];
J = [];
f = [];
S = [];
for i=1:Tfinal/dt
    theta(i)= theta0+vel_theta*i;
    tempo(i) = 0 +dt*i;
    k = 1;
    Fx = 1;
    Dr = 1;
    x = ones(4,1);% chute na ordem x,y,alpha e beta
    while (k <=N_it && Fx>e && Dr > 0.01)
        J = [1,0,-a*sin(x(3)),-b*cos(x(4)); 0,0,-a*cos(x(3)),b*sin(x(4)); 0, -sin(x(4)), -a*sin(x(3)), -x(2)*cos(x(4)); 0, -cos(x(4)), -a*cos(x(3)), x(2)*sin(x(4))];
        f = [(x(1) - b*sin(x(4)) + a*cos(x(3)) - w), (-b*cos(x(4)) - a*sin(x(3)) +u), (r*cos(theta(i)) - x(2)*sin(x(4)) + a*cos(x(3)) -w), (r*sin(theta(i)) - x(2)*cos(x(4)) - a*sin(x(3)) + v)];
        S = -inv(J)*f';
        x = x + S;
        Dr  = norm(S);
        Fx = norm(f);
        k = k+1;
    end
    
    xx(i) = x(1);
    y(i) = x(2);
    alpha(i) = x(3);
    beta(i) = x(4);
end

%-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
%-------------PLOTAR AS BARRAS PARA FAZER UMA ANIMAÇÃO --------------------
M =[];
M(:,1) = xx';
M(:,2) = y';
M(:,3) = alpha';
M(:,4) = beta';
M(:,5) = theta';
