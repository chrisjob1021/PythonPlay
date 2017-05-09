class MinStack(object):
	def __init__(self):
		self.stack = []

	def push(self, value):
		min_value = self.get_min()
		if min_value == None or value < min_value:
			min_value = value
		self.stack.append((value, min_value))

	def pop(self):
		self.stack.pop()

	def top(self):
		if len(self.stack) == 0:
			return None
		else:
			return self.stack[-1][0]

	def get_min(self):
		if len(self.stack) == 0:
			return None
		else:
			return self.stack[-1][1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print "expect -3"
print minStack.get_min() # returns -3
minStack.pop()
print "expect 0"
print minStack.top() # returns 0
print "expect -2"
print minStack.get_min() # returns -2