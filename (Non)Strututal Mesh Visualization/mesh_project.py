from tkinter import *
from math import sin
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
import math
import numpy as np
import random
from PIL import ImageTk
import os
from matplotlib.patches import Rectangle

global COLOR
COLOR = "green"


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def draw(self, color: str):
        plt.scatter(self.x, self.y, color=color, s=4)  # plotting single point

    def __str__(self):
        return "{} {}".format(self.x, self.y)


class Line:
    def __init__(self, head: Point, tail: Point):
        self.head = head
        self.tail = tail

    def length(self):
        return math.sqrt(
            math.pow(self.head.x - self.tail.x, 2)
            + math.pow(self.head.y - self.tail.y, 2)
        )

    def draw(self, color):
        if img[self.head.x, self.head.y] == img[self.tail.x, self.tail.y]:
            if img[self.head.x, self.head.y][0] == 0:
                color = "b"
            else:
                color = "g"
        else:
            color = "y"
        ax2.plot(
            [self.head.x, self.tail.x],
            [self.head.y, self.tail.y],
            linestyle="-",
            color=color,
            linewidth=0.5,
        )


class Circle:
    def __init__(self, point, r):
        self.O = point
        self.r = r

    def draw(self):
        angle = np.linspace(0, 2 * np.pi, 150)
        x = self.r * np.cos(angle) + self.O.x
        y = self.r * np.sin(angle) + self.O.y
        plt.plot(x, y)


class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.edges = {Line(self.A, self.B), Line(self.A, self.C), Line(self.B, self.C)}
        self.sides()

    def draw(self):
        if COLOR == True:
            chars = "0123456789ABCDEF"
            color = "#" + "".join(random.sample(chars, 6))
        else:
            color = COLOR
        Line(self.A, self.B).draw(color)
        Line(self.A, self.C).draw(color)
        Line(self.B, self.C).draw(color)

    def sides(self):
        self.a = math.sqrt(
            math.pow(self.B.x - self.C.x, 2) + math.pow(self.B.y - self.C.y, 2)
        )
        self.b = math.sqrt(
            math.pow(self.A.x - self.C.x, 2) + math.pow(self.A.y - self.C.y, 2)
        )
        self.c = math.sqrt(
            math.pow(self.A.x - self.B.x, 2) + math.pow(self.A.y - self.B.y, 2)
        )

    #       | ax-dx, ay-dy, (ax-dx)² + (ay-dy)² |
    # det = | bx-dx, by-dy, (bx-dx)² + (by-dy)² |
    #       | cx-dx, cy-dy, (cx-dx)² + (cy-dy)² |

    # (ax-dx) * (by-dy) * (cx-dx)² + (cy-dy)² +

    def pointInTriangleCircumcircle(self, point):
        matrix = np.array(
            [
                [point.x * point.x + point.y * point.y, point.x, point.y, 1],
                [self.A.x * self.A.x + self.A.y * self.A.y, self.A.x, self.A.y, 1],
                [self.B.x * self.B.x + self.B.y * self.B.y, self.B.x, self.B.y, 1],
                [self.C.x * self.C.x + self.C.y * self.C.y, self.C.x, self.C.y, 1],
            ]
        )
        det = np.linalg.det(matrix)
        if orientation(self.A, self.B, self.C) > 0:
            return det > 0
        else:
            return det < 0

    def centerOfTriangleCircumcircle(self):
        self.angles()
        x = (
            self.A.x * math.sin(2 * self.alpha)
            + self.B.x * math.sin(2 * self.beta)
            + self.C.x * math.sin(2 * self.gamma)
        ) / (
            math.sin(2 * self.alpha)
            + math.sin(2 * self.beta)
            + math.sin(2 * self.gamma)
        )
        y = (
            self.A.y * math.sin(2 * self.alpha)
            + self.B.y * math.sin(2 * self.beta)
            + self.C.y * math.sin(2 * self.gamma)
        ) / (
            math.sin(2 * self.alpha)
            + math.sin(2 * self.beta)
            + math.sin(2 * self.gamma)
        )
        O = Point(x, y)
        O.draw("r")
        Circle(O, Line(O, self.A).length()).draw()
        return O

    def __str__(self):
        return "{} | {} | {} ".format(self.A, self.B, self.C)


def orientation(A, B, C):
    AC = [C.x - A.x, C.y - A.y]
    AB = [B.x - A.x, B.y - A.y]
    v = AC[0] * AB[1] - AB[0] * AC[1]
    return v


def superTriangle(points):
    points.sort(key=lambda p: abs(p.x))
    m = 3
    big = max(max(abs(p.x), abs(p.y)) for p in points)
    p1 = Point(m * big, 0)
    p2 = Point(0, m * big)
    p3 = Point(-1 * m * big, -1 * m * big)

    super_triangle = Triangle(p1, p2, p3)
    return super_triangle


def notShared(edge, triangles):
    count = 0
    for t in triangles:
        for e in t.edges:
            if (e.head == edge.head and e.tail == edge.tail) or (
                e.head == edge.tail and e.tail == edge.head
            ):
                count += 1
    if count == 1:
        return True
    else:
        return False


def BowyerWatson(points, splitLen):
    triangulation = []

    super_triangle = superTriangle(points)
    triangulation.append(super_triangle)

    for p in points:
        badTriangles = []
        for t in triangulation:
            if t.pointInTriangleCircumcircle(p):
                badTriangles.append(t)
        polygon = []
        for t in badTriangles:
            for e in t.edges:
                if notShared(e, badTriangles):
                    polygon.append(e)
        for t in badTriangles:
            triangulation.remove(t)
        for e in polygon:
            newTri = Triangle(e.head, e.tail, p)
            triangulation.append(newTri)

    remove = []

    for t in triangulation:
        if (
            t.A == super_triangle.A
            or t.A == super_triangle.B
            or t.A == super_triangle.C
            or t.B == super_triangle.A
            or t.B == super_triangle.B
            or t.B == super_triangle.C
            or t.C == super_triangle.A
            or t.C == super_triangle.B
            or t.C == super_triangle.C
            or t.a > splitLen
            or t.b > splitLen
            or t.c > splitLen
        ):
            remove.append(t)

    for r in remove:
        triangulation.remove(r)

    for t in triangulation:
        t.draw()


def QuadTree(img, STARTx, ENDx, w, STARTy, ENDy, h):
    MIDx = STARTx + w // 2
    MIDy = STARTy + h // 2
    global P, T
    center = Point(MIDx, MIDy)
    points.append(center)
    P.append(center)

    def check(x1, x2, y1, y2):
        px = [0, 0]
        for y in range(y1, y2):
            for x in range(x1, x2):
                if img[x, y][0] == 0:
                    px[0] += 1
                if img[x, y][0] == 255:
                    px[1] += 1
            if px[0] > 20 and px[1] > 20:
                QuadTree(img, x1, x2, w // 2, y1, y2, h // 2)
                break
            else:
                T.append(
                    Triangle(
                        Point(STARTx, STARTy), Point(STARTx, MIDy), Point(MIDx, STARTy)
                    )
                )
                T.append(
                    Triangle(
                        Point(STARTx, MIDy), Point(MIDx, MIDy), Point(MIDx, STARTy)
                    )
                )

                """
                T.append(
                    Triangle(
                        Point(STARTx, MIDy), Point(MIDx, MIDy), Point(STARTx, ENDy)
                    )
                )
                T.append(
                    Triangle(Point(STARTx, ENDy), Point(MIDx, ENDy), Point(MIDx, MIDy))
                )
                """

                T.append(
                    Triangle(
                        Point(STARTx, STARTy), Point(ENDx, STARTy), Point(STARTx, ENDy)
                    )
                )
                T.append(Point(ENDx, ENDy), Point(ENDx, STARTy), Point(STARTx, ENDy))
                """                
                T.append(
                    Triangle(
                        Point(MIDx, STARTy), Point(MIDx, MIDy), Point(ENDx, STARTy)
                    )
                )
                T.append(
                    Triangle(Point(ENDx, MIDy), Point(MIDx, MIDy), Point(ENDx, STARTy))
                )
                """
                T.append(
                    Triangle(Point(MIDx, MIDy), Point(MIDx, ENDy), Point(ENDx, MIDy))
                )
                T.append(
                    Triangle(Point(ENDx, MIDy), Point(ENDx, ENDy), Point(ENDx, MIDy))
                )
                ax1.plot(
                    [STARTx, ENDx],
                    [ENDy, STARTy],
                    linestyle="-",
                    color="g",
                    linewidth="0.1",
                )
                ax1.plot(
                    [STARTx, MIDx],
                    [MIDy, STARTy],
                    linestyle="-",
                    color="g",
                    linewidth="0.1",
                )
                ax1.plot(
                    [MIDx, ENDx],
                    [ENDy, MIDy],
                    linestyle="-",
                    color="g",
                    linewidth="0.1",
                )

    if w > 40 and h > 40:
        check(STARTx, MIDx, STARTy, MIDy)
        check(MIDx, ENDx, STARTy, MIDy)
        check(STARTx, MIDx, MIDy, ENDy)
        check(MIDx, ENDx, MIDy, ENDy)

    ax1.plot([MIDx, MIDx], [STARTy, ENDy], linestyle="-", color="g", linewidth="0.5")
    ax1.plot([STARTx, ENDx], [MIDy, MIDy], linestyle="-", color="g", linewidth="0.5")


def StructuralMesh(image_path):
    global P, T
    P = []
    T = []
    image = Image.open(image_path, "r")
    # plt.imshow(image)
    img = image.load()
    points.append(Point(0, 0))
    points.append(Point(0, image.size[1] - 1))
    points.append(Point(image.size[0] - 1, 0))
    points.append(Point(image.size[0] - 1, image.size[1] - 1))
    QuadTree(img, 0, image.size[0], image.size[0], 0, image.size[1], image.size[1])


def NonStructuralMesh(image_path, maxSpace, split):
    image = Image.open(image_path, "r")
    global img
    img = image.load()
    points = []
    for x in range(0, image.size[0], maxSpace):
        for y in range(0, image.size[1], maxSpace):
            # if img[x, y][0] == 0:
            points.append(Point(x, y))
    BowyerWatson(points, split)


if __name__ == "__main__":
    image_path = "test.png"
    global points
    points = []
    global ax1, ax2
    fig, (ax1, ax2) = plt.subplots(2)
    image = Image.open(image_path, "r")
    ax1.imshow(image)
    ax2.imshow(image)
    # fig.suptitle('Vertically stacked subplots')

    StructuralMesh(image_path)
    NonStructuralMesh(image_path, 20, 50)

    # plt.rcParams["figure.dpi"] = 200
    plt.show()
