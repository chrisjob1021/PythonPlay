import sys
import traceback

try:
	akdhakdahda
except:
	lines = traceback.format_exception(*sys.exc_info())
	res = [ ]
	for line in lines:
		res.extend(line.rsplit('\n')[:-1])

	print '\n'.join('!! ' + x for x in res)

	
	#print ''.join('!!' + line for line in res.split('\n'))