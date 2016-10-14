
class Node:
	def __init__(self, value, edge):
		self.value = value
		self.edge = edge

	def __hash__(self):
		return hash(self.value)

	def __lt__(self, other):
		if isinstance(other, Node):
			return self.value < other.value
		elif isinstance(other, (chr)):
			return self.value < other
		else:
			return False

	def __gt__(self, other):
		if isinstance(other, Node):
			return self.value > other.value
		elif isinstance(other, (chr)):
			return self.value > other
		else:
			return NotImplemented

	def __eq__(self, other):
		if isinstance(other, Node):
			return self.value == other.value
		elif isinstance(other, (chr)):
			return self.value == other
		else:
			return NotImplemented

	def __ne__(self, other):
		return not(self == other)

	def __str__(self):
		return '(' + str(self.value) + str(self.edge) + ')'

	def __repr__(self):
		return '(' + str(self.value) + str(self.edge) + ')'


class Dijikstra:
	def __init__(self, graph=None):
		if not graph:
			self.graph = {Node('A',-1):set([Node('B', 3), Node('C', 4)]),
					Node('B', -1):set([Node('A', 3), Node('D', 2), Node('E', 5)]),
					Node('C', -1):set([Node('A', 4), Node('F', 6)]),
					Node('D', -1):set([Node('B',2)]),
					Node('E', -1):set([Node('B', 5), Node('F', 8)]),
					Node('F', -1):set([Node('C',6), Node('E', 8)])}
		else:
			self.graph = graph

	def dijikstraPath(self, start, goal):
		queue = [(start, [start])]

		while queue:
			(vertex, path) = queue.pop(0)
			for next in self.graph[vertex] - set(path):
				if next == goal:
					return path + [next]
				else:
					queue.append((next, path + [next]))

		return None


d = Dijikstra(None)
print(d.dijikstraPath(Node('A', -1), Node('F', -1)))