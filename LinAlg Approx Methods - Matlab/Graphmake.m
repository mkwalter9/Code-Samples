%Margaret Walter
%ACM 104 Hmwk 6 Problem 2

clear min
clear max
clear index

load('USAirTransportation.mat')
alphamat = [.1,.15,.20];
col1 = ones(500,1);
S = A;

%Form the stochastic matrix where columns sum to 1
for j=1:500
    n = sum(A(:,j));
    for i=1:500
        S(i,j) = A(i,j)/n;
    end
end

values = zeros(3,10);

for j = 1:length(alphamat)
    eiger = alphamat(j) * S + (1-alphamat(j))*A; %L~ in notes

    %switching the adjacency matrix A off to call other function
    Adj = A;
    A = eiger;
    Homework6Problem1Walter


    for i = 1:10
        [M,I] = max(y);
        values(j,i) = I;
        y(I) = 0;
    end

end

ID = values

%Graphing to check connectedness
G = graph(A, 'upper');
h = plot(G,'Layout','force');
