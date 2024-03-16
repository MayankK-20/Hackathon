import numpy as np
import json 
import matplotlib.pyplot as plt

def dist(point,centroids):
    x,y = point
    min = 0
    dist = 10**12
    for i in range(len(centroids)):
        temp = ((x-centroids[i][0])**2+(y-centroids[i][1])**2)**0.5
        if temp < dist:
            min = i
            dist = temp
    return min

def centroid(points):
    temp = points.sum(0)
    x,y = temp[0]/points.shape[0],temp[1]/points.shape[0]
    return x,y

def orthogonal_regression(points):
    centroid_points=points.sum(0)/points.shape[0]
    cx,cy=centroid_points
    new_points=(points-centroid_points)*np.array([[1,1j]])
    new_points=new_points.sum(1)
    new_points**=2
    no=new_points.sum()**0.5
    x,y=np.real(no),np.imag(no)

    slope=y/x
    intercept=slope*(-cx)+cy

    return slope,intercept

with open(r'C:\Users\shank\Downloads\lats.txt') as f:
    point = json.loads(f.read())

minx = min([x[0] for x in point])
maxx = max([x[0] for x in point])
miny = min([x[1] for x in point])
maxy = max([x[1] for x in point])
cluster = 7
range_ = np.linspace(minx,maxx,cluster)
cluster_count = []
for i in zip(np.linspace(minx,maxx,cluster),np.linspace(maxy,miny,cluster)):
    cluster_count.append(list(i))
line_set = []
print(cluster_count)
for a in range(20):
    clusters = [[] for _ in range(len(cluster_count))]
    x = 0; y = 0
    for i in point:
        temp = dist(i,cluster_count)
        clusters[temp].append(i)
    for i in range(len(clusters)): 
        if clusters[i] != []:     
            temp = np.array(clusters[i])
            x,y = centroid(temp)
            cluster_count[i] = [x,y]


    

# print(cluster_count)

for i in clusters:
    temp = np.array(i)
    slope, intercept = orthogonal_regression(temp)
    line_set.append((slope,intercept))

   
print("slopes and intercepts of the required k lines:")    
print(line_set)

