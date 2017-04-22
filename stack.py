class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack(object):
	def __init__(self):
		self.top = None

	def push(self, data):
		n = Node(data)
		if self.top:
			n.next = self.top

		self.top = n

	def pop(self):
		current = self.top
		if current:
			self.top = current.next
			return current.data
		else:
			return None

	def peek(self):
		if self.top == None:
			return None

		return self.top.data

	def isEmpty(self):
		return self.top == None

	def printStack(self):
		current = self.top
		while current:
			print current.data,
			current = current.next
		print

class MinStack(Stack):
	def __init__(self):
		self.top = None
		self.s2 = Stack()

	def min(self):
		return self.s2.peek()

	def push(self, data):
		minval = self.min()
		if minval == None or data < self.min():
			self.s2.push(data)

		super(MinStack, self).push(data)

	def pop(self):
		if self.top.data == self.min():
			self.s2.pop()
		super(MinStack, self).pop()


vals = [ 82, 18, 47, 67, 18, 72, 19, 87, 21, 84 ]

stack = Stack()

print stack.isEmpty()

for val in vals:
	stack.push(val)

stack.printStack()

print stack.isEmpty()
print stack.peek()
print stack.pop()

stack.printStack()

minstack = MinStack()
print dir(minstack)
minstack.push(2)
print minstack.min()
minstack.pop()
print minstack.min()

vals = [ 82, 18, 47, 67, 18, 72, 19, 87, 21, 84 ]

stack = MinStack()

print stack.isEmpty()

for val in vals:
	stack.push(val)

stack.printStack()

print stack.isEmpty()
print stack.peek()
print stack.pop()
print stack.min()

stack.printStack()

# pythonic way

class PythonStack(object):
	def __init__(self):
		self.stack = [ ]

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def isEmpty(self):
		return len(self.stack) == 0



vals = [ 82, 18, 47, 67, 18, 72, 19, 87, 21, 84 ]

stack = Stack()

print stack.isEmpty()

for val in vals:
	stack.push(val)

print stack.isEmpty()
print stack.peek()
print stack.pop()
print stack.peek()




