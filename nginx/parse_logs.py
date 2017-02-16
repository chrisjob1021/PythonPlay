'''Write some code to parse an nginx log in chunks
grouping requests by /24 subnet and day
and then give me the top 10 subnets from each day'''

from subprocess import call
import re
from collections import Counter

for day in range(1, 32):
    if len(str(day)) == 1:
        search_day = "0" + str(day)
    else:
        search_day = str(day)

    search_day += "/Feb"

    print search_day
    subnet_dict = Counter()

    with open("test.log") as f:
        i=0
        for chunk in iter( : f.read(1024 * 1024), ''):
            match = re.findall(".*\[%s.*\" ([0-9]+\.[0-9]+\.[0-9]+)\.[0-9]+ [0-9\.]+" % search_day, chunk)
            i += 1
            #print "processing chunk %d" % i
            if len(match) > 0:
                subnet_dict_chunk = Counter(match)

                #print "got a match in chunk %d" % i
                #print subnet_dict_chunk
                subnet_dict.update(subnet_dict_chunk)

    print subnet_dict.most_common(10)