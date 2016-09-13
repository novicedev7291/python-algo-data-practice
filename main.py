from collections.list import Element, LinkedList
from collections.hashTable import HashTable
from utils.sort import BinarySearch, BubbleSort

if __name__ == '__main__':
	hTable = HashTable()

	hTable.put('UDACITY','UDACITY')
	hTable.put('UDAVITY','Ramayan')

	print(hTable.get('UDACITY'))

