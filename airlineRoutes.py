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