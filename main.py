from collections.list import Element, LinkedList

if __name__ == '__main__':
	ele1 = Element('kuldeep')
	ele2 = Element('Manish')
	ele3 = Element('Jatin')
	ele4 = Element('Kunal')
	ele5 = Element('Vishal')
	linkedList = LinkedList(None)

	linkedList.append(ele1)
	linkedList.append(ele2)
	linkedList.append(ele3)
	linkedList.append(ele4)
	linkedList.append(ele5)

print(linkedList)
