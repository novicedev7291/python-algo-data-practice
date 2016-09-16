
class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BTree(object):
	def __init__(self, root=None):
		self.root = root

	def add(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			self.__add(value, self.root)

	def __add(self, value, node):
		if value < node.value:
			# New value should be add to left of given node
			if node.left != None:
				self.__add(value, node.left)
			else:
				node.left = Node(value)
		elif value > node.value:
			if node.right != None:
				self.__add(value, node.right)
			else:
				node.right = Node(value)

	def search(self, node):
		if self.root == None:
			return None
		else:
			return self.__search(self.root, node)

	def __search(self, root, node):
		if root.value == node.value:
			return root
		elif node.value > root.value:
			return self.__search(root.right, node)
		else:
			return self.__search(root.left, node)

	def getRoot(self):
		return self.root

	def print_tree(self, node=None):
		if node:
			print(node.value)
			self.print_tree(node.left)
			self.print_tree(node.right)
		else:
			return
