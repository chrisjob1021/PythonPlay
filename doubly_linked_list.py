class Node(object):
	def __init__(self, val):
		self.next = None
		self.prev = None
		self.val = val

class DoublyLinkedList(object):
	def __init__(self):
		self.head = None

	def append(self, val):
		if self.head == None:
			self.head = Node(val)
		else:
			current = self.head		

			previous = None	
			while current:
				previous = current
				current = current.next

			new_node = Node(val)
			previous.next = new_node
			new_node.prev = previous

	def push(self, val):
		if self.head == None:
			self.head = Node(val)
		else:
			prev_head = self.head
			self.head = prev_head.prev = new_node = Node(val)
			new_node.next = prev_head

	def reverse(self):
		self._reverse(self.head, None)

	def _reverse(self, node, previous):
		if node:
			next_node = node.next

			node.next = previous

			if next_node: 
				node.prev = next_node
				self._reverse(next_node, node)
			else:
				self.head = node
				node.prev = None

	def remove(self, val):
		return self._remove(val, self.head)

	def _remove(self, val, node):
		return_val = False

		if node:
			if node.val == val:
				node_next = node.next
				node_prev = node.prev

				if node_prev == None:
					self.head = node_next
				else:
					node_prev.next = node_next
				node_next.prev = node_prev

				return_val = True
			else:
				return_val = self._remove(val, node.next)

		return return_val

	def get(self, val):
		node = self.head
		while node:
			if node.val == val:
				return node
			else:
				node = node.next
		return False

	def printList(self):
		current = self.head
		while current:
			print "Node: %s Value: %d Prev: %s Next: %s" % (str(current), current.val, str(current.prev), str(current.next))
			current = current.next

ll = DoublyLinkedList()

#test push
ll.push(5)
ll.push(10)
ll.push(6)
ll.push(9)
ll.push(12)
ll.printList()
print "\n\n"

#test append
ll.append(15)
ll.printList()
print "\n\n"

#test recursive reverse
ll.reverse()
ll.printList()
print "\n\n"

#test remove
print ll.remove(100)
print ll.remove(9)
ll.printList()
print "\n\n"

print ll.remove(15)
ll.printList()
print "\n\n"

#test get

print ll.get(5)
print ll.get(5).val

