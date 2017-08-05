'''

Reprint just unique lines from file in order

1500=test3
0=test1
1000=test2
0=test1
1500=test3
2000=test4

so expected:

0=test1
1000=test2
1500=test3
2000=test4

'''

d = { }

with open('testfile') as f:
	for line in f:
		l = line.rstrip().split('=')
		print l[0]
		d[l[0]] = l[1]

for k in sorted(d):
	print k + '=' + d[k]
