class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Element:
    def __init__(self, nodes):
        self.nodes = nodes


class Application:
    def __init__(self):
        self.nodes = []
        self.triangles = []
        self.quads = []

    def generate_triangles(self, n: int, x0: float, y0: float, x1: float, y1: float, num_x: int, num_y: int) -> None:
        dx = (x1 - x0) / num_x
        dy = (y1 - y0) / num_y
        node_id = 0
        for j in range(num_y + 1):
            for i in range(num_x + 1):
                x = x0 + i * dx
                y = y0 + j * dy
                self.nodes.append(Node(x, y))
                if i < num_x and j < num_y:
                    n1 = node_id
                    n2 = node_id + 1
                    n3 = node_id + num_x + 1
                    self.triangles.append(Element([n1, n2, n3]))
                    n1 = node_id + 1
                    n2 = node_id + num_x + 2
                    n3 = node_id + num_x + 1
                    self.triangles.append(Element([n1, n2, n3]))
                node_id += 1

    def generate_quads(self, n: int, x0: float, y0: float, x1: float, y1: float, num_x: int, num_y: int) -> None:
        dx = (x1 - x0) / num_x
        dy = (y1 - y0) / num_y
        node_id = 0
        for j in range(num_y + 1):
            for i in range(num_x + 1):
                x = x0 + i * dx
                y = y0 + j * dy
                self.nodes.append(Node(x, y))
                if i < num_x and j < num_y:
                    n1 = node_id
                    n2 = node_id + 1
                    n3 = node_id + num_x + 2
                    n4 = node_id + num_x + 1
                    self.quads.append(Element([n1, n2, n3, n4]))
                node_id += 1

    def save_mesh(self, filename: str) -> None:
        with open(filename, "w") as file:
            file.write(f"{len(self.nodes)} {len(self.quads)}\n")
            for node in self.nodes:
                file.write(f"{node.x} {node.y}\n")
            for quad in self.quads:
                file.write(f"4 {' '.join(str(n) for n in quad.nodes)}\n")

    def load_mesh(self, filename: str) -> None:
        with open(filename, "r") as file:
            num_nodes, num_quads = map(int, file.readline().split())
            self.nodes = [Node(*map(float, file.readline().split())) for _ in range(num_nodes)]
            self.quads = [Element(list(map(int, file.readline().split()[1:]))) for _ in range(num_quads)]
            file.seek(0)  # set file pointer to the beginning
            file_contents = file.read()  # read file contents
            print(file_contents)  # print file contents to the screen

    def run(self):
        print("Welcome to the Mesh Generator!")
        while True:
            try:
                n = int(input("Enter the number of elements: "))
                break
            except ValueError:
                print("Invalid input, please enter an integer.")

        while True:
            try:
                choice = int(input("Choose the type of elements (1. Triangles, 2. Quads): "))
                if choice == 1:
                    self.generate_quads(0, 0, 1, 1, n, n, n)
                    break
                elif choice == 2:
                    self.generate_quads(0, 0, 1, 1, n, n, n)
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input, please enter an integer.")

        filename = input("Enter the filename to save the mesh: ")
        self.save_mesh(filename)
        print(f"Mesh saved to {filename}.")


def main():
    app = Application()
    while True:
        choice = input("Choose an option (1. Create mesh, 2. Load mesh, 3. Quit): ")
        if choice == "1":
            app.run()
        elif choice == "2":
            filename = input("Enter the filename to load the mesh: ")
            app.load_mesh(filename)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
    print("Goodbye!")


if __name__ == "__main__":
    main()
