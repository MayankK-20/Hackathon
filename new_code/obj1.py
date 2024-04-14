import numpy as np
from time import time
from sklearn.datasets import fetch_california_housing
california_housing = fetch_california_housing(as_frame=True)

import json

lats=list(california_housing.frame['Latitude'])
longs=list(california_housing.frame['Longitude'])
points=np.array([*zip(lats,longs)])

class Model:
    def __init__(self, points):
        '''Points is a list containing [x cord, ycord]
          for various points'''
        
        self.points=np.array(points)

    def orthogonal_regression(self):
        points=np.array(self.points,dtype=complex)
        centroid_points=points.sum(0)/points.shape[0]
        cx,cy=centroid_points

        new_points=(points-centroid_points)*np.array([[1,1j]])
        new_points=new_points.sum(1)[:,None]
        new_points**=2
        no=(new_points.sum(0)**0.5)[0]
        x,y=np.real(no),np.imag(no)

        if no==0:
            slope=1 #slope can be anything as condition is just that line passes thoruhg centroid

        else:
            if x==0:
                slope=np.inf
            else:
                slope=y/x

        return slope,[np.real(cx),np.real(cy)]
    
    def dist_calc(self,slope,point):
        l=1
        m=slope

        vector_array=np.array([[m],[-l]])

        vector_norm_array=vector_array/(((vector_array**2).sum())**0.5)

        distances=(self.points-point)@vector_norm_array


        distances=np.abs(distances)

        return (distances.sum())

    def gradient_descent(self, learning_rate, slope, intercept):
        ''' Calculates  optimal slope and intercept '''

        l=1
        m=slope

        # vector_norm=(l/(l**2+m**2)**0.5,m/(l**2+m**2)**0.5)

        vector_array=np.array([[m],[-l]])
        vector_norm_array=vector_array/( ((vector_array**2).sum())**0.5)

        point_given=[0,intercept]

        # print(points[:,0:1])
        #batch gradient-descent
        gradient_slope=( ((points-point_given)@vector_norm_array)*points[:,0:1] ).sum() #minimizing cost function using the fact that any hypothesis function give gradient for parameters as (y(i)-htheta(i))*xj(i)

        slope_step=gradient_slope*learning_rate
        gradient_intercept=( ((points-point_given)@vector_norm_array) *1 ).sum()
        intercept_step=gradient_intercept*learning_rate

        return slope_step,intercept_step

    def optimal_shift(self, slope, intercept, no=100):
        range=100
        shift_vals=np.hstack([np.linspace(-range,range,no),0])

        k=(slope**2+1)**0.5 #shifting perp to the line
        shift_vals*=k

        optimal_intercept=intercept
        current_distance=self.dist_calc(slope,[0,intercept]) 

        for i in shift_vals:
            d=self.dist_calc(slope, intercept+i)
            if d< current_distance:
                current_distance=d
                optimal_intercept=intercept+i

        
        return optimal_intercept
    
    def optimal_slope(self,slope,intercept, no=1000):

        range_angles=np.pi

        vals=np.linspace(-range_angles,range_angles,no)
        slopes=np.tan(vals) #slope is tan of angle 

        optimal_slope=slope
        current_distance=self.dist_calc(slope,[0,intercept]) 

        for i in slopes:
            d=self.dist_calc(i, [0, intercept])
            if d<current_distance:
                current_distance=d
                optimal_slope=i

        
        return optimal_slope



# xs=[x for x,y in points]
# ys=[y for x,y in points]
# print(min(xs),max(xs))
# print(min(ys),max(ys))

my_model=Model(points)
slope,point=my_model.orthogonal_regression()
intercept=point[1]+point[0]*-1*slope

for i in range(10):
    slope=my_model.optimal_slope(slope, intercept,1000)
    intercept=my_model.optimal_shift(slope, intercept,100)

    print(my_model.dist_calc(slope, [0, intercept]))




# iterations=1000
# init_slope=-1.11111111
# init_intercept=-77.83


# print(dist_calc(points,init_slope,init_intercept))

# for i in range(iterations):
#     sl,inter=gradient_descent(points,10**-12,init_slope,init_intercept)

#     # print(dist_calc(points,init_slope,init_intercept))
#     init_slope-=sl
#     init_intercept-=inter

# # print(init_slope,init_intercept,s2-s1)

# print(dist_calc(points,init_slope,init_intercept))

# oslope,ointer=orthogonal_regression(points)
# print(oslope,ointer)
# print(dist_calc(points,oslope,ointer))
# print(dist_calc_2(points,-0.9090909090909101,(36.64196244420971, -120.6808155684726)))


# print(optimal_shift(points,oslope,ointer))

