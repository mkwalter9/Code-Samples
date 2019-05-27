% Margaret Walter 11/10/16
% ACM104 Problem 5


%%Main Loop
counts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
norms = zeros(length(counts), 2);

for i =1:length(counts)
    n = counts(i);
    v = gs(n);
    u = modgs(n);
    norms(i,1) = norm(v, Inf);
    norms(i,2) = norm(u, Inf);
end

scatter(counts', norms(:,1), 'filled','b')
hold on
scatter(counts', norms(:,2), 'filled','r')
xlabel('n')
ylabel('Infinite norm')

%%%%%%%%%% Functions %%%%%%%%%

%%Gram-Schmidt
function v = gs(c)
h = hilb(c);
v = [];
v(:,1) = h(:,1); 
for k=2:c
    sum = 0;
    for i = 2:(k-1)
        sum = sum + dot(h(:,k),v(:,i)) * v(:,i) / (norm(v(:,i))^2);
    end
    v(:,k) = h(:,k) - sum; %orthog basis only 
    v(:,k) = v(:,k)/(norm(v(:,k))); %normalizing vectors
end
end

%%Modified G-S
function u = modgs(c)
h = hilb(c);
u = [];
w = h(:,:); %malleable vector set
u(:,1) = w(:,1); 
for j=1:c
    u(:,j) = w(:,j)/(norm(w(:,j)));
    for k = (j+1):c %modifying w
        w(:,k) = w(:,k) - dot(w(:,k),u(:,j))*u(:,j);
    end
end
end

