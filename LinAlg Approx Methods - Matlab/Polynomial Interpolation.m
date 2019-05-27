% Margaret Walter 11/10/16
% ACM104 Problem 4



%%Plotting
figure;
subplot(4,2,1);
imshow(polys(1,3));
title('a = 1, n = 3');
subplot(4,2,2);
imshow(polys(1,5));
title('a = 1, n = 5');
subplot(4,2,3);
imshow(polys(1,10));
title('a = 1, n = 10');
subplot(4,2,4);
imshow(polys(1,15));
title('a = 1, n = 15');


%%defining functions
function img = polys(a, n)
x1 = linspace(-a,a);
f = [];
for i=1:length(x1) %Populating f
    f(i) = cos(x1(i))/(cosh(x1(i)));
end
p = polyfit(x1,f,(n-1));
y = polyval(p, x1); %interpolation points

%plotting
xmin = min(x1);
xmax = max(x1);
img = scatter(x1, f);
hold on
scatter(x1, y, 5, 'filled')
hold off
end