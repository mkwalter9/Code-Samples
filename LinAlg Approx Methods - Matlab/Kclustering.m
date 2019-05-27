% Margaret Walter 10/24/16
% ACM104 Set 3, Problem 3
% K-means clustering problem


%%%%% INITIALIZATIONS + LOADING DATA %%%%%

data = load('clustering_data.mat');
data = struct2cell(data);
data = cell2mat(data); %there has to be a more elegant way
rng(2016); %seeding the rng for reproducability
r1 = [20*rand(1)-10,16*rand(1)-4]; %the starting cluster centers, K=3 case
r2 = [20*rand(1)-10,16*rand(1)-4];
r3 = [20*rand(1)-10,16*rand(1)-4];
c1 = [];
c2 = [];
c3 = [];
dim = size(data);
loopnum = 25; %num of iterations of K-means algorithm


%%%%% MAIN %%%%%


for i = 1:loopnum
    distances1 = dist1(data, r1);
    distances2 = dist1(data, r2);
    distances3 = dist1(data, r3);
    for i = 1:dim(1)
        if distances1(i) < distances2(i) && distances1(i) < distances3(i)
            c1 = [c1; data(i,:)];
        elseif distances2(i) < distances3(i) %if distances1 not min then who?
            c2 = [c2; data(i,:)];
        else
            c3 = [c3; data(i,:)];
        end
    end
    r1 = rdjust(c1);
    r2 = rdjust(c2);
    r3 = rdjust(c3);
    scatter(c1(:,1),c1(:,2),25,'r')
    hold on;
    scatter(c2(:,1),c2(:,2),25,'g')
    hold on;
    scatter(c3(:,1),c3(:,2),25,'b')
end

    

%%%%% FUNCTIONS %%%%%

function dist = dist1(coords, r)
%Iterates through a list and computes distance 
dim = size(coords); %how many elem to iterate
dist = zeros(dim(1)); %matrix of zeroes to store distances
for i = 1:dim(1)
    %std distance formula
    dist(i) = sqrt((r(1) - coords(i,1))^2 + (r(2) - coords(i,2))^2);
end
end

function newr = rdjust(c)
%Finds a new center/r1 based on average of current cluster points
sumx = 0;
sumy = 0;
dim = size(c);
for i = 1:dim(1)
    sumx = sumx + c(i,1);
    sumy = sumy + c(i,2);
end
newr = [(sumx/dim(1)), (sumy/dim(1))];
end 



