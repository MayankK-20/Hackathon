import numpy as np
import json 
import matplotlib.pyplot as plt

def dist_calc_2(points,slope,x0,y0):
    l=1
    m=slope

    vector_array=np.array([[m],[-l]])
    vector_norm_array=vector_array/((vector_array**2).sum())**0.5

    point_given=(x0,y0)

    distance=(points-point_given)@vector_norm_array


    distance=np.abs(distance)
    return distance.sum()

def find_optimal_slope(points, x0, y0):
    slopes = np.linspace(-10, 10, 10)  
    min_distance = float('inf')
    optimal_slope = None

    for slope in slopes:
        distance = dist_calc_2(points, slope, x0, y0)
        if distance < min_distance:
            min_distance = distance
            optimal_slope = slope

    return optimal_slope


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
x0, y0 = 0, 0
for a,b in point:
    x0+=a
    y0+=b
x0/=len(point)
y0/=len(point)
slope = find_optimal_slope(np.array(point),x0,y0)
graph_trend = slope/abs(slope)
cluster = 7
range_ = np.linspace(minx,maxx,cluster)
cluster_count = []
p = maxy if graph_trend < 0 else miny
q = maxy if p == miny else miny
for i in zip(np.linspace(minx,maxx,cluster),np.linspace(p,q,cluster)):
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

