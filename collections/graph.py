class Vertex:
	def __init__(self, 	value):
		self.value = value
		self.neighbors = list()

	def add_neighbor(self, vertex):
		if vertex not in self.neighbors:
			self.neighbors.append(vertex)
			#self.neighbors.sort()

	def __str__(self):
		return self.value

	def __repr__(self):
		return self.value

class Graph:
	vertices = {}
	visited = {}

	def add_vertex(self, v):
		if isinstance(v, Vertex) and v not in self.vertices:
			self.vertices[v.value] = v
			return True
		else:
			return False
		
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(self.vertices[v])
			self.vertices[v].add_neighbor(self.vertices[u])
			return True
		else:
			return False

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))

	def dfsSearch(self, start):
		for key in self.vertices.keys():
			self.visited[key] = False

		self.__dfsSearch(start)

	def __dfsSearch(self, start):
		if self.visited[start] == True:
			return
		self.visited[start] = True
		for neighbor in self.vertices[start].neighbors:
			self.__dfsSearch(neighbor.value)

	def print_dfs(self):
		print(self.visited)


g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.print_graph()
g.dfsSearch('C')
g.print_dfs()