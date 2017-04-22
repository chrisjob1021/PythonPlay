class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

#first in first out
class Queue(object):
	def __init__(self):
		self.top = None
		self.bottom = None

	def add(self, data):
		new = Node(data)

		if self.bottom:
			self.bottom.next = new

		self.bottom = new

		if self.top == None:
			self.top = new

	def remove(self):
		current = self.top
		self.top = current.next

		return current.data

	def isEmpty(self):
		return self.top == None

	def peek(self):
		if self.top:
			return self.top.data

		return None

	def printQueue(self):
		current = self.top
		while current:
			print current.data,
			current = current.next
		print

vals = [ 82, 18, 47, 67, 18, 72, 19, 87, 21, 84 ]

queue = Queue()

print queue.isEmpty()

for val in vals:
	queue.add(val)

queue.printQueue()

print queue.isEmpty()
print queue.peek()
print queue.remove()

queue.printQueue()

# pythonic way

from collections import deque

queue = deque()

#isEmpty
print len(queue) == 0

for val in vals:
	queue.append(val)

print queue

#isEmpty
print len(queue) == 0

#peek
print queue[0]

print queue.popleft()

print queue

