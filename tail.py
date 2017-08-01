import os
import sys

lines = 100
fname = sys.argv[1]
fsize = os.stat(fname).st_size
buff = 8192
if fsize <= buff:
	buff = fsize

data = [ ]
i = 1

with open(fname) as f:
	while True:
		pos = fsize-(buff*i) 
		f.seek(pos)
		data.extend(f.readlines())
		if len(data) >= lines or f.tell() == 0 or f.tell() > fsize:
			break

		i += 1

print ''.join(data[-lines:]),



