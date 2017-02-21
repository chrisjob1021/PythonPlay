'''
discovered great way to read chunks and split at newlines from http://stupidpythonideas.blogspot.com/2014/07/three-ways-to-read-files.html
get number of log entries between dates
'''

import re

def fetch_chunks(file, chunk_size=4096):
    return iter(lambda: file.read(4096), '')

def sepsplit(chunk, separator):
    buf = type(separator)()

    for portion in chunk:
        buf += portion
        split_portion = buf.split(separator)
        yield split_portion[:-1]
    # if last item does not contain our seprator, make sure we still get it
        buf = split_portion[-1]
    if buf:
        remaining_portion = [ buf ]
        yield remaining_portion

with open("test.log") as f:
    dates_dict = { }
    chunks = fetch_chunks(f)
    for chunk in sepsplit(chunks, "\n"):
        for line in chunk:
            for match in re.findall('([0-9]{2}/[A-Za-z]{3})/[0-9:]+', line):
                try:
                    dates_dict[match] += 1
                except KeyError:
                    dates_dict[match] = 1
f.close()

print dates_dict