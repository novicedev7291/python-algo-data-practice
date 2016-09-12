
class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):

	def __init__(self, head=None):
		self.head = head

	def append(self, element):
		current = self.head

		if self.head:
			while current.next:
				current = current.next
			current.next = element
		else:
			self.head = element

	def __str__(self):
		str = '['
		current = self.head
		if self.head:
			while current.next:
				str = str + ',' + current.value
				current = current.next
			str = str + ']'


		return str