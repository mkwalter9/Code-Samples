% Margaret Walter

load pca_data.mat
dims = size(X);
n = dims(2);
a = mean(X(1,:));
b = mean(X(2,:));

for i=1:n
    X(1,i) = X(1,i) - a;
    X(2,i) = X(2,i) - b;
end


%A: finding covariance matrix
covar = 1/n * X * X';
covar = (covar + covar')/2; %symmetrizing matrix

%B: finding principal components and plotting
[v,d] = eig(covar);
vec1 = v(:,1)/(norm(v(:,1))); %normalizing
vec2 = v(:,2)/(norm(v(:,2)));
mew = mean(X');
m1 = vec1(1)/vec1(2); % calculating slope to graph
m2 = vec2(1)/vec2(2);
scatter(X(1,:)', X(2,:)')
hold on
x = min(X(1,:)):max(X(1,:));
y1 = m1*x + (mew(2) - m1*mew(1)); %Graphing the line
y2 = m2*x + (mew(2) - m2*mew(1));
plot(x,y1,x,y2,'--')

%C: transforming data and then finding new covariance
Y = inv(d) * X;
covy = 1/n * Y * Y';



