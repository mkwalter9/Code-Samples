%Margaret Walter
%ACM 104 Hmwk 6 Problem 5

clear min
clear max
clear index

%Creating matrix
a = ones(20);
b = ones(30);
c = blkdiag(a,b) - eye(50);
c(1,21) = 1;
c(2,22) = 1;
c(3,23) = 1;
c(21,1) = 1;
c(22,2) = 1;
c(23,3) = 1;
A = c;

%Creating degree matrix
D = zeros(50);
for i =1:50
    D(i,i) = sum(c(i,:));
end

%Getting Laplacian
L = D - A;

%Getting Fiedler vector
[v,d] = eigs(L,2,'sm');
F = v(:,1);
sp = F;
S = F;
sm = F;
%Finding s+ and s-
for i=1:20
    [M,I] = max(F);
    sp(I) = 1;
    F(I) = min(F);
end

for i = 1:50
    if sp(i) ~= 1
        sp(i) = -1;
    end
end

for i=1:20
    [M,I] = min(S);
    sm(I) = 1;
    S(I) = max(S);
end

for i = 1:50
    if sm(i) ~= 1
        sm(i) = -1;
    end
end

%Choosing the smaller partition
if (sm'*L*sm) < (sp'*L*sp)
    part = (sm'*L*sm)/4;
else
    part = (sp'*L*sp)/4;
end

disp('min cut: ')
disp(part)

%Graphing
G = graph(A, 'upper');
h = plot(G,'Layout','force');
highlight(h, [1,21],'Edgecolor','g')
highlight(h, [2,22],'Edgecolor','g')
highlight(h, [3,23],'Edgecolor','g')



