
class BinarySearch(object):
	def __init__(self, arr=None):
		self.arr = arr

	def search(self, eleToFind):
		return BinarySearch.binarySearch(self, eleToFind, 0, len(self.arr)-1)

	def binarySearch(self, eleToFind, start, end):
		if end >= start:
			mid = int(start + ((end - start)/2));
			if self.arr[mid] == eleToFind:
				return mid
			elif eleToFind > self.arr[mid]:
				return BinarySearch.binarySearch(self, eleToFind, mid+1, end)
			else:
				return BinarySearch.binarySearch(self, eleToFind, start, mid-1)


class BubbleSort(object):
	def __init__(self, arr):
		self.arr = arr

	def sort(self):
		end = len(self.arr) - 1
		for i in range(end):
			for j in range(0, end):
				if self.arr[j] > self.arr[j+1]:
					BubbleSort.swap(self,j, j+1)
		return self.arr

	def swap(self, i, j):
		temp = self.arr[i]
		self.arr[i] = self.arr[j]
		self.arr[j] = temp
