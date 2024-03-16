import numpy as np
from time import time
from sklearn.datasets import fetch_california_housing
california_housing = fetch_california_housing(as_frame=True)

import json

lats=list(california_housing.frame['Latitude'])
longs=list(california_housing.frame['Longitude'])
points=np.array([*zip(lats,longs)],dtype=complex)


# xs=[x for x,y in points]
# ys=[y for x,y in points]
# print(min(xs),max(xs))
# print(min(ys),max(ys))
def orthogonal_regression(points):
    centroid_points=points.sum(0)/points.shape[0]
    cx,cy=centroid_points
    new_points=(points-centroid_points)*np.array([[1,1j]])
    new_points=new_points.sum(1)
    new_points**=2
    no=new_points.sum()**0.5
    x,y=np.real(no),np.imag(no)

    slope=y/x
    intercept=slope*-cx+cy

    return slope,intercept


def dist_calc(points,slope,intercept):
    l=1
    m=slope

    vector_array=np.array([[m],[-l]])

    vector_norm_array=vector_array/((vector_array**2).sum())**0.5

    point_given=(0,intercept)



    distance=(points-point_given)@vector_norm_array


    distance=np.abs(distance)


    return (distance.max(),distance.sum())

def dist_calc_2(points,slope,intercept):
    l=1
    m=slope

    vector_array=np.array([[m],[-l]])
    vector_norm_array=vector_array/((vector_array**2).sum())**0.5

    point_given=intercept

    distance=(points-point_given)@vector_norm_array


    distance=np.abs(distance).sum()
    return (distance)
# [(0,0),(1,1),(3,2)]

def gradient_descent(points, learning_rate, slope, intercept):
    ''' '''
    l=1
    m=slope

    # vector_norm=(l/(l**2+m**2)**0.5,m/(l**2+m**2)**0.5)

    vector_array=np.array([[m],[-l]])
    vector_norm_array=vector_array/((vector_array**2).sum())**0.5

    point_given=[0,intercept]

    # print(points[:,0:1])
    gradient_slope=( ((points-point_given)@vector_norm_array)*points[:,0:1] ).sum()

    slope_step=gradient_slope*learning_rate
    gradient_intercept=( ((points-point_given)@vector_norm_array) ).sum()
    intercept_step=gradient_intercept*learning_rate

    return slope_step,intercept_step

iterations=1000
init_slope=-1.11111111
init_intercept=-77.83

not_defined=set([np.inf,np.nan,-np.inf,-np.nan])

print(dist_calc(points,init_slope,init_intercept))

for i in range(iterations):
    sl,inter=gradient_descent(points,10**-12,init_slope,init_intercept)

    # print(dist_calc(points,init_slope,init_intercept))
    init_slope-=sl
    init_intercept-=inter

# print(init_slope,init_intercept,s2-s1)

print(dist_calc(points,init_slope,init_intercept))

oslope,ointer=orthogonal_regression(points)
print(oslope,ointer)
print(dist_calc(points,oslope,ointer))
print(dist_calc_2(points,-0.9090909090909101,(36.64196244420971, -120.6808155684726)))

def optimal_shift(points,slope,intercept):
    range=10
    no=100
    shift_vals=np.hstack([np.linspace(-range,range,no),0])

    k=(slope**2+1)**0.5
    shift_vals*=k
    distances=[(optimal_slope(points,slope,shift+intercept),shift) for shift in shift_vals]
    
    return min(distances)
def optimal_slope(points,slope,intercept):
    range=np.pi
    no=10000
    vals=np.linspace(-range,range,no)

    slopes=np.hstack([np.tan(vals),slope])
    distances=[(dist_calc(points,new_slope,intercept)[1],new_slope) for new_slope in slopes]
    
    return min(distances)

print(optimal_shift(points,oslope,ointer))


cluster_count = 7
xs=[x for x,y in points]
ys=[y for x,y in points]


graph_trend=-1

clusters = [list(i) for i in zip(np.linspace(min(xs),max(xs),cluster),np.linspace(max(ys),min(ys),cluster))]

for i in zip(np.linspace(min(xs),max(xs),cluster),np.linspace(p,q,cluster)):
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
