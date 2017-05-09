nums = range(2,50)

for i in range(2,8):
	nums = filter(lambda x: x == i or x % i, nums)

print nums

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x*2 + 10, foo)
print reduce(lambda x, y: x + y, foo)

d = { "y": 1, "x": 2, "z": 3 }
print {k: v for k,v in d.items() if v == 1}
