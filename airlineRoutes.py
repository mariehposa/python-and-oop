from collections import defaultdict

class AirlineRoutes:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add(self, key, value):
        self.graph[key].append(value)
        # print(self.graph[key])

    def printPathsHelper(self, start, destination, visited, path):
        visited[start] = True
        path.append(start)
        # print(self.graph[start])

        if start == destination:
            print(path)
        else:
            for i in self.graph[start]:
                if visited[i] == False:
                    self.printPathsHelper(i, destination, visited, path)

        path.pop()
        visited[start] = False

    def printPaths(self, start, destination):
        visited = [False] * self.vertices
        path = []

        self.printPathsHelper(start, destination, visited, path)


test = AirlineRoutes(5)
test.add(0, 1)
test.add(0, 2)
test.add(1, 3)
test.add(3, 4)
test.add(2, 4)
test.add(0, 4)
test.printPaths(0, 4)