import random
import matplotlib.pyplot as plt


# function for generating random points
def generate_points(n):
    points = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        points.append((x, y))
    return points

# helper function to check the orientation of a point relative to a line
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

# function implementing Jarvis' algorithm
def jarvis(points):
    # find the point with the lowest y-coordinate (if there are multiple, choose the one with the lowest x-coordinate)
    n = len(points)
    ymin = points[0][1]
    min_idx = 0
    for i in range(1, n):
        y = points[i][1]
        if (y < ymin) or (ymin == y and points[i][0] < points[min_idx][0]):
            ymin = y
            min_idx = i

    # create an empty stack and add the first point to it
    hull = []
    hull.append(points[min_idx])

    # iterate through the remaining points and add them to the convex hull
    p = min_idx
    while True:
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == min_idx:
            break
        hull.append(points[p])

    return hull

# generate 10 random points and compute the convex hull for them
points = generate_points(100)
hull = jarvis(points)

# create a plot and draw the points and the convex hull
fig, ax = plt.subplots()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.scatter([p[0] for p in points], [p[1] for p in points], color='blue')
ax.plot([p[0] for p in hull] + [hull[0][0]], [p[1] for p in hull] + [hull[0][1]], color='red')

plt.show()
