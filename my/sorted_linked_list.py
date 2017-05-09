import sys

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class SortedLinkedList(object):
	def __init__(self):
		self.head = None

	def add(self, data):
		current = self.head
		previous = None

		while current is not None and current.data <= data:
			previous = current
			current = current.next

		new_node = Node(data)

		try: 
			new_node.next = current
		except AttributeError:
			pass

		try: 
			previous.next = new_node
		except AttributeError:
			self.head = new_node

		return new_node

	def get_node(self, data):
		current = self.head
		while current is not None:
			if current.data == data:
				return current
			previous = current
			current = current.next

	def remove(self, data):
		found = False
		current = self.head

		previous = None
		while current is not None:
			if current.data == data:
				found = True
				break
			else:
				previous = current
				current = current.next

		if found == True:
			if previous == None:
				self.head = current.next
			else:
				previous.next = current.next

		return found

	def print_list(self):
		current = self.head
		while current is not None:
			print current.data,
			current = current.next
		print "\r"

	'''
	https://leetcode.com/problems/merge-two-sorted-lists/?tab=Description

	Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

	'''

	# recursively    
	def mergeTwoListsRecursively(self, l1, l2):
	    if not l1 or not l2:
	        return l1 or l2

	    for l in [l1, l2]:
	    	l.next = l.head
	    	while l.next:
	    		l.next = self.recurseMergeTwoLists(l.next)

	def recurseMergeTwoLists(self, node):
		self.add(node.data)
		return node.next
	        
	# in-place, iteratively        
	def mergeTwoLists(self, l1, l2):
	    # if one of the lists are empty, return just the one that is not
	    list1 = l1
	    list2 = l2
	    if None in (l1, l2):
	        return l1 or l2
	    current = l2.head    
	    while current:
	    	l1.add(current.data)
	    	current = current.next

