import numpy as np
import json
import matplotlib.pyplot as plt

file_path = r'C:\Users\shank\Downloads\lats.txt'
with open(file_path, 'r') as file:
    points = json.loads(file.read())
    points=np.array(points)

def dist_calc_2(points,slope,x0,y0):
    l=1
    m=slope

    vector_array=np.array([[m],[-l]])
    vector_norm_array=vector_array/((vector_array**2).sum())**0.5

    point_given=(x0,y0)

    distance=(points-point_given)@vector_norm_array


    distance=np.abs(distance)
    return distance.max()

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

def find_optimal_shift(points, slope, x0, y0):
    min_distance = float('inf')
    optimal_shift = None
    perp=(1/slope)
    shift_range = 100
    num_shifts = 10000
    shift_values = np.linspace(-shift_range, shift_range, num_shifts)
    slope_ = None
    for shift_x in shift_values:
        slope_ = find_optimal_slope(points,x0+shift_x, y0+(perp*shift_x))
        perp = 1/slope_
        distance = dist_calc_2(points, slope_, x0+shift_x, y0+(perp*shift_x))
        if distance < min_distance:
            min_distance = distance
            optimal_shift = shift_x
    return optimal_shift, slope_

x0, y0 = 0, 0
for a,b in points:
    x0+=a
    y0+=b
x0/=len(points)
y0/=len(points)


optimal_slope = find_optimal_slope(points, x0, y0)

optimal_shift,slope_ = find_optimal_shift(points, optimal_slope, x0, y0)

print("Without Shift: ", dist_calc_2(points, optimal_slope, x0, y0))
print("With Shift and rotation: ", dist_calc_2(points, slope_, x0+optimal_shift, y0+((1/slope_)*optimal_shift)))

x = np.array([point[0] for point in points])
y = np.array([point[1] for point in points])
plt.scatter(x, y, color='red')


plt.plot(x, optimal_slope * (x - x0) + y0, color='blue')

x0=x0+optimal_shift
y0=y0+((1/slope_)*optimal_shift)

plt.plot(x, slope_ * (x - x0) + y0, color='green')


plt.scatter(x0, y0, color='blue')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Line with Minimum Distance from Given Point')
plt.grid(True)
plt.show()

print("Optimal Slope:", slope_)
print("Line Passes Through", (x0, y0))

