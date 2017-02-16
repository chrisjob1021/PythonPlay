'''Write some code to parse an nginx log in chunks
grouping requests by /24 subnet and day
and then give me the top 10 subnets from each day'''

import re
from collections import Counter

for day in range(1,32):
	if len(str(day)) == 1:
		search_day = "0" + str(day)
	else:
		search_day = str(day)

	total_day = Counter()

	with open("test.log") as f:
		for chunk in iter(lambda: f.read(1024 * 1024), ''):
			match = re.findall(".*\[%s/Feb.*\" ([0-9]+\.[0-9]+\.[0-9]+)\.[0-9]+" % search_day, chunk)
			total_day.update(Counter(match))
	f.close()

	print search_day
	print total_day.most_common(10)


