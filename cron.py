import datetime
import threading
import time
import subprocess

jobs = [ ]
file = 'crontab'

# * 
# */5
# 2,4
# 2,5-6
# 0-6 starting wtih sunday

def registerJobs(s):
	c = s.split()

	if len(c) < 6:
		return False

	d = dict(zip(['minute', 'hour', 'day', 'month', 'isoweekday'], [v for v in c[:5]]))
	d['comm'] = c[5:]

	jobs.append(d)

def validate(dVal, eVal):
	def checkRange(interval):
		ranges = interval.split('-')

		print eVal

		if int(eVal) in xrange(int(ranges[0]), int(ranges[1])+1):
			return True

		return False

	if dVal == '*':
		return True
	elif '/' in dVal:
		interval = dVal.split('/')
		if int(eVal) % int(dVal) == 0:
			return True
	elif ',' in dVal:
		for interval in dVal.split(','):
			if '-' in interval:
				if checkRange(interval):
					return True
			elif int(interval) == int(eVal):
				return True
	elif '-' in dVal:
		if checkRange(dVal):
			return True
	elif int(dVal) == int(eVal):
		return True

	return False

def checkJob(d, now): 
	for field in [k for k in d if k != 'comm']:
		dVal = d[field]
		if field == 'isoweekday':
			eVal = int(getattr(now, field)())
			if eVal == 7:
				eVal = 0
		else:
			eVal = getattr(now, field)

		if validate(dVal, eVal) == False:
			return False

	return True

with open(file) as f:
	map(registerJobs, filter(lambda x: len(x) > 2, f.readlines()))

while True:
	now = datetime.datetime.today()
	
	for job in jobs:
		if checkJob(job, now):
			print "running"
			threading.Thread(target=lambda: subprocess.call(' '.join(job['comm']), shell=True)).start()
		else:
			print 'NOT running'
		print job

	time.sleep(1)
	print threading.enumerate()
	time.sleep(60)
