
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfsRecursive(graph, start, visited=None):
	# initialize visited if None initially
	if not visited:
		visited = set()
	# add given vertex to visited list
	visited.add(start)
	# Loop through edges list for given vertex which are not present in visited yet
	for next in graph[start] - visited:
		# when find the next vertex from the given vertex repeat the proccess recursively
		dfsRecursive(graph, next, visited)
	return visited

def dfsUsingStack(graph, start):
	#Initialize visited with empty and add start to stack
	visited, stack = set(), [start]
	# Loop through stack untill true
	while stack:
		# pop top vertex from stack. ie. stack will be updated when we continue visting more vertex
		vertex = stack.pop()
		# check if vertex is already present in visited or not 
		if vertex not in visited:
			# if vertex is not visited yet add to visited
			visited.add(vertex)
			# Now add the vertexes on stack which are not visted yet from given vertex
			stack.extend(graph[vertex] - visited)
	return visited

def graph_paths(graph, start, goal):
	# Add start and path to itself on stack
	stack = [(start,[start])]
	# Loop through stack untill true
	while stack:
		# Pop first one which is obviously initialized above or added later
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			# if next is the destination then just add vertex in path
			if next == goal:
				yield path + [next]
			# else put the vertex and extended path upto this vertex into stack
			else:
				stack.append((next, path + [next]))
				# continue for loop for vertexes left behind in graph[vertex] edges


print(list(graph_paths(graph, 'A', 'F')))