
import sys

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		return new_node

	# iterative
	def reverse(self):
		previous = None
		current = self.head
		while current is not None:
			next = current.next
			current.next = previous
			previous = current
			current = next
		self.head = previous

	def recursive_reverse_util(self, current, previous):
		if current.next == None:
			self.head = current
			current.next = previous
			return

		next = current.next
		current.next = previous

		self.recursive_reverse_util(next, current)

	# recursive
	def recursive_reverse(self):
		if self.head == None:
			return
		self.recursive_reverse_util(self.head, None)

	def append(self, data, next_node=None):
		current = self.head
		if current == None:
			return self.push(data)
		else:
			while current is not None:
				previous = current
				current = current.next

			new_node = Node(data)
			new_node.next = next_node
			previous.next = new_node

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
	http://stackoverflow.com/questions/2663115/how-to-detect-a-loop-in-a-linked-list
	You can make use of Floyd's cycle-finding algorithm, also know as tortoise and hare algorithm.

	The idea is to have two references to the list and move them at different speeds. Move one forward by 1 node and the other by 2 nodes.

	If the linked list has a loop they will definitely meet.
	Else either of the two references(or their next) will become null.

	https://leetcode.com/problems/linked-list-cycle/?tab=Description

	Given a linked list, determine if it has a cycle in it.

	'''
	def has_cycle(self):
		try:
			slow = self.head
			fast = self.head.next
			while slow is not fast:
				slow = slow.next
				fast = fast.next.next
			return True
		except:
			return False
	'''
	https://leetcode.com/problems/add-two-numbers/?tab=Description

	You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

	You may assume the two numbers do not contain any leading zero, except the number 0 itself.

	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	'''
	def combine_lists(self, list1, list2):
		carry = 0
		new_list = LinkedList()
		list1 = list1.head
		list2 = list2.head
		while list1:
			v1 = list1.data
			list1 = list1.next

			v2 = list2.data
			list2 = list2.next

			print "v1: %d v2: %d carry: %d" % (v1, v2, carry)
			print (v1+v2+carry) // 10
			print (v1+v2+carry) % 10
			carry, value = divmod(v1+v2+carry, 10)
			new_list.append(value)

		return new_list

'''
ll = LinkedList()
ll.push(35)
ll.push(150)
ll.push(75)
ll.push(23)
ll.append(95)
ll.print_list()

ll.reverse()
ll.print_list()

ll.recursive_reverse()
ll.print_list()

print ll.remove(2)
print ll.remove(23)
ll.print_list()

print ll.has_cycle()

next_node = ll.get_node(35)
ll.append(1000, next_node)

print ll.has_cycle()

ll1 = LinkedList()
ll1.push(2)
ll1.push(4)
ll1.push(3)
ll1.print_list()

ll2 = LinkedList()
ll2.push(5)
ll2.push(6)
ll2.push(4)
ll2.print_list()

combined_list = LinkedList().combine_lists(ll1,ll2)
combined_list.print_list()

ll1 = LinkedList()
ll1.push(5)
ll1.push(4)
ll1.push(3)
ll1.print_list()

ll2 = LinkedList()
ll2.push(5)
ll2.push(6)
ll2.push(4)
ll2.print_list()

combined_list = LinkedList().combine_lists(ll1,ll2)
combined_list.print_list()
'''
