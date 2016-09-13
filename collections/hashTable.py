
class HashTable(object):
 	def __init__(self):
 		self.arr = [None] * 100

 	def put(self,key, value):
 		index = HashTable.hashFunction(key)
 		vList = HashTable.get(self, key)

 		if vList:
 			vList.append(value)
 		else:
 			vList = list()
 			vList.append(value)

 		self.arr[index] = vList

 	def get(self,key):
 		index = HashTable.hashFunction(key)
 		if index:
 			return self.arr[index]

 	def hashFunction(key):
 		hashValue = HashTable.hash(key)
 		index = ((hashValue % 100) % 10)
 		return index

 	def hash(key):
 		#chars = list(key)
 		hashValue = ord(key[0])*100 + ord(key[1])
 		return hashValue