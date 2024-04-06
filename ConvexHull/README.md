# Convex Hull Computation Project

## Overview

This Python project aims to compute the convex hull of a set of randomly generated points using Jarvis' algorithm. The convex hull is the smallest convex polygon that encloses all the points in a given set. Jarvis' algorithm, also known as the gift wrapping algorithm, is a simple and efficient method for finding the convex hull of a finite set of points.

## Project Components

### 1. Random Points Generation

- Random points are generated within the range [-1, 1] for both x and y coordinates.

### 2. Jarvis' Algorithm Implementation

- **Orientation Function:** Determines the orientation of three points relative to each other.
- **Jarvis' Algorithm Function:** Computes the convex hull of the generated points using Jarvis' algorithm.

### 3. Plotting

- A plot is created using Matplotlib to visualize the randomly generated points and their convex hull.

## How it Works

1. Random points are generated within the range [-1, 1] for both x and y coordinates.
2. Jarvis' algorithm is applied to compute the convex hull of the generated points.
3. The generated points and their convex hull are plotted on a graph.

## Usage

1. Run the Python script to generate random points and compute their convex hull.
2. View the generated plot to visualize the convex hull.

## Example

```python
# Python code for generating random points and computing the convex hull
import random
import matplotlib.pyplot as plt

# function for generating random points
def generate_points(n):
    # code for generating random points

# helper function to check the orientation of a point relative to a line
def orientation(p, q, r):
    # code for orientation function

# function implementing Jarvis' algorithm
def jarvis(points):
    # code for Jarvis' algorithm

# generate random points and compute the convex hull
points = generate_points(100)
hull = jarvis(points)

# create a plot and draw the points and the convex hull
fig, ax = plt.subplots()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.scatter([p[0] for p in points], [p[1] for p in points], color='blue')
ax.plot([p[0] for p in hull] + [hull[0][0]], [p[1] for p in hull] + [hull[0][1]], color='red')

plt.show()

```

![Example](EXAMPLE.png)

## Author

This project was created by [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.