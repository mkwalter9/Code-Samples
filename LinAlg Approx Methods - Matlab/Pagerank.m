% Margaret Walter 
% ACM 104 Hmwk 6 Problem 1

%Uncomment lines below when running alone!

%A = input('Matrix: ');
lim = .00005;
%lim = input('limit: ');

n = size(A);
y = randi([0,1],[n(2),1]); % randomize & set for matrix dim
x = randi([0,1],[n(2),1]);
iter = 0;

while norm(x - y, inf) > lim %Power iteration code
    x = y;
    y = (A*x)/(norm(A*x, inf));
    iter = iter + 1;
end

eigenval = (A*y)\y; 