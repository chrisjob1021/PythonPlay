import re
import hashlib
import os
import itertools

# i am assuming test.log is 300gb in size and will not fit entirely into memory

# read file in chunks
# for each chunk, extract ips
# sha256 ip
# put ip in flat file under following directory structure: hash[0]/hash[1]/hash[2-5]
# iterate through files in directory structure reading back ips in chunks
# for each file, place ip in set()
# write set() out to file representing master unique values

root = "/tmp/unique_ips"
uniq_log = "unique.log"
try:
	os.remove(uniq_log)
except:
	pass

def fetchChunks(file, chunk_size=(1024 * 1024)):
	return iter(lambda: file.read(chunk_size), '')

def sepSplit(portion, sep):
	buf = type(sep)()

	for seg in portion:
		buf += seg
		bufsplit = buf.split(sep)
		yield bufsplit[:-1]
		buf = bufsplit[-1]
	if buf:
		yield [buf]

def targetFile(hash):
	return "%s/%s/%s/%s" % (root, hash[0], hash[1], hash[2:5])

def processIPs(l):
	for entry in l:
		ip = re.findall("([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", entry)
		sha256 = hashlib.sha256(ip[-1]).hexdigest()
		target = targetFile(sha256)
		try:
			os.stat(target)
		except:
			os.makedirs(target)

		with open("%s/results.dat" % target, "a+") as f:
			f.write("%s\n" % ip[-1])
		f.close()

def writeUniques():
	x = iter(itertools.product("0123456789abcdef", repeat=5))
	for val in x:
		uniq = set([])

		sha256 = ''.join(val)
		file = targetFile(sha256) + "/results.dat"
		try:
			os.stat(file)
		except:
			pass
		else:
			with open("%s" % file) as f:
				for line in f.readlines():
					uniq.add(line)
			f.close()

			f = open("%s" % uniq_log, "a+")
			for ip in uniq:
				f.write(ip)
			f.close()

with open("test.log") as f:
	chunks = fetchChunks(f)
	for splitchunk in sepSplit(chunks, '\n'):
		processIPs(splitchunk)
f.close()

writeUniques()

