import numpy as np
import json
import matplotlib.pyplot as plt

file_path = r"C:\Users\Mayank\OneDrive\Desktop\lats.txt"
with open(file_path, 'r') as file:
    points = json.loads(file.read())

def dist_calc(points, slope, x0, y0):
    l = 1
    m = slope

    vector_norm = (l / (l ** 2 + m ** 2) ** 0.5, m / (l ** 2 + m ** 2) ** 0.5)

    vector_array = np.array([[m], [-l]])
    vector_norm_array = np.array([[vector_norm[1]], [-1 * vector_norm[0]]])

    points_array = np.array(points)

    distance = []
    for point in points_array:
        latitude, longitude = point
        point_given = np.array([latitude, longitude])
        distance.append(np.abs((point_given - np.array([x0, y0])) @ vector_norm_array))

    return np.sum(distance)

def find_optimal_slope(points, x0, y0):
    slopes = np.linspace(-10, 10, 100)  # Reduced to 100 slopes to evaluate
    min_distance = float('inf')
    optimal_slope = None

    for slope in slopes:
        distance = dist_calc(points, slope, x0, y0)
        if distance < min_distance:
            min_distance = distance
            optimal_slope = slope

    return optimal_slope

def find_optimal_shift(points, slope, x0, y0):
    min_distance = float('inf')
    optimal_shift = None
    perp=(1/slope)
    shift_range = 100
    num_shifts = 100
    shift_values = np.linspace(-shift_range, shift_range, num_shifts)

    for shift_x in shift_values:
        distance = dist_calc(points, slope, x0+shift_x, y0+(perp*shift_x))
        if distance < min_distance:
            min_distance = distance
            optimal_shift = shift_x
    return optimal_shift

x0, y0 = 0, 0
for a,b in points:
    x0+=a
    y0+=b
x0/=len(points)
y0/=len(points)


optimal_slope = find_optimal_slope(points, x0, y0)

optimal_shift = find_optimal_shift(points, optimal_slope, x0, y0)

print("Without Shift: ", dist_calc(points, optimal_slope, x0, y0))
print("With Shift: ", dist_calc(points, optimal_slope, x0+optimal_shift, y0+((1/optimal_slope)*optimal_shift)))

x = np.array([point[0] for point in points])
y = np.array([point[1] for point in points])
plt.scatter(x, y, color='red')


plt.plot(x, optimal_slope * (x - x0) + y0, color='blue')

x0=x0+optimal_shift
y0=y0+((1/optimal_slope)*optimal_shift)

plt.plot(x, optimal_slope * (x - x0) + y0, color='green')


plt.scatter(x0, y0, color='blue')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Line with Minimum Distance from Given Point')
plt.grid(True)
plt.show()

print("Optimal Slope:", optimal_slope)
print("Line Passes Through", (x0, y0))
