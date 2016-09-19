
class MaxHeap:
	"""docstring for MaxHeap"""
	def __init__(self, items=[]):
		super().__init__()
		self.heap = [0]
		for i in items:
			self.heap.append(i)
			self._floatup(len(self.heap)-1)

	def push(self, data):
		self.heap.append(data)
		self._floatup(len(self.heap)-1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return false

	def pop(self):
		if len(self.heap) > 2:
			self._swap(1, len(self.heap)-1)
			max = self.heap.pop()
			self._bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			max = False
		return max

	def _swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
		
	def _floatup(self, index):
		parent = index//2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self._swap(index, parent)
			self._floatup(index)

	def _bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self._swap(largest, index)
			self._bubbleDown(index)


m = MaxHeap([95, 23, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))