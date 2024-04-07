# Mesh Generator Program

## Program Description

The Mesh Generator program is designed to generate and manipulate meshes for various engineering and scientific simulations. It allows users to create meshes consisting of triangles or quadrilaterals, save them to files, and load existing meshes for further modification.

## Code Overview

### Node Class

The `Node` class represents a single point in the mesh. It has two attributes, `x` and `y`, which define its coordinates in 2D space.

### Element Class

The `Element` class represents a geometric element in the mesh, such as a triangle or a quadrilateral. It contains a list of node indices that define the vertices of the element.

### Application Class

The `Application` class is the main component of the program. It manages the generation, saving, and loading of meshes. Here's a breakdown of its methods:

- `generate_triangles(n, x0, y0, x1, y1, num_x, num_y)`: Generates a mesh consisting of triangles within the specified rectangular domain defined by `(x0, y0)` and `(x1, y1)` with the given number of elements along the x and y axes.
- `generate_quads(n, x0, y0, x1, y1, num_x, num_y)`: Generates a mesh consisting of quadrilaterals within the specified rectangular domain.
- `save_mesh(filename)`: Saves the generated mesh to a file specified by `filename`.
- `load_mesh(filename)`: Loads a mesh from the file specified by `filename`.
- `run()`: Starts the mesh generation process by prompting the user for input and generating the mesh accordingly.

### Main Function

The `main()` function creates an instance of the `Application` class and provides a simple command-line interface for interacting with the program. It allows users to choose between creating a new mesh, loading an existing mesh, or quitting the program.

## Types of Meshes

### Triangular Mesh

A triangular mesh consists of elements shaped like triangles. Each triangle is defined by three nodes, and neighboring triangles share nodes along their edges. Triangular meshes are commonly used in finite element analysis and computational fluid dynamics.

### Quadrilateral Mesh

A quadrilateral mesh consists of elements shaped like quadrilaterals (or quads). Each quad is defined by four nodes, and neighboring quads share nodes along their edges. Quadrilateral meshes are often used in structural analysis and finite volume methods for solving partial differential equations.

Both types of meshes are widely used in various scientific and engineering simulations due to their simplicity and efficiency in representing complex geometries.

## Author

This project was created by ([MaksKubiczek](https://github.com/MaksKubiczek)).

## License

This project is licensed under the [MIT License]. For more information, see the LICENSE file.