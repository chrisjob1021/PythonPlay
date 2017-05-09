import re

uniq = set([])
with open("file.txt") as f:
	for line in f.readlines():
		match = re.search("((\([\d]{3}\)\s|[\d]{3}-|[\d]{3}\s)[\d]{3}(-|\s)[\d]{4})", line).group(0)
		uniq.add(re.sub("[-\s\(\)]", "", match))
print uniq

