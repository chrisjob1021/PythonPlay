import os
import sys

lines = 10
fname = sys.argv[1]
fsize = os.stat(fname).st_size
buff = 8 * 1024 * 1024
if fsize < buff:
	buff = fsize

data = [ ]
i = 1

with open(fname) as f:
	while True:
		pos = fsize - (buff * i)
		if pos < 0:
			pos = 0
		f.seek(pos)

		for line in f:
			data.append(line)

		if len(data) >= lines or pos == 0:
			break

		i += 1

print ''.join(data[-lines:]),
