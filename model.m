%% Parâmetros do modelo: (Variáveis de seleção da Interface)
P0 = csvread('p0.csv');
Y = csvread('y0.csv');
% I0
I = Y(1:50,1:100);
for i = 1:50
    I(i,1) = I(i,1)*P0(i);
end
X = csvread('x0.csv');
% S0
S = X(1:50,1:100);
for i = 1:50
    S(i,1) = S(i,1)*P0(i);
end
beta = csvread('beta.csv');
mi = csvread('mi.csv');
gamma = 1.0/14.0;
%disp(beta);

tmax = 99;
amax = 50;

for t = 1:tmax % iterando o tempo de 1 até 150 dias
    S(1,t) = P0(1);
    I(1,t) = 0;
    for a = 2:amax
        lambda = 0.0;
        for s = 1:amax
            value = beta(s,a)*I(s,t);
            lambda = lambda + value;
        end
        if P0(a) > 0
            lambda = lambda/P0(a);
        else
            lambda = 0;
        end
        % vacinas
        if (t<20) && (a<11)
%             v = 111 + 100/a;
%             v=S(a,t)/15;
%             v=0;
            v=22000 + 0.72*P0(a);
        else
%             v = 111 + 100/a;
%             v=0;
           v=22000 + 0.72*P0(a);
        end
        f = -1*(lambda + mi(a)+ v) *S(a,t);
        S(a,t+1) = f + (S(a,t)-S(a,t+1))/365.0 + S(a,t);
        if S(a,t+1)<0
            S(a,t+1)=0;
        end
        g = (lambda)*S(a,t) - (mi(a) + gamma)*I(a,t);
        I(a,t+1) = g + (I(a,t)-I(a,t+1))/365.0 + I(a,t);
        if I(a,t+1)<0
            I(a,t+1)=0;
        end
    end
end

imagesc(I);
c = colorbar;
c.Label.String = 'Infected(a,t)';
xlabel('t');
ylabel('a');
