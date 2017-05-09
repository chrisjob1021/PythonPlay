'''
https://careercup.com/question?id=17877682

You are given a UNIX path with dot (current) and two dots (parent). Convert this to an absolute path 

E.g. $/home/abc/.././def/./ghi/../. 
becomes $/home/ghi/

'''

path = '$/home/abc/.././def/./ghi/../.'

def joiner(acc, next):
    if next == '.' or next == '':
        return acc
    if next == '..':
        return acc[:-1]
    print "acc = %s + next = %s" % (str(acc), str([next]))
    return acc + [next]

print path.split('/')
nice = reduce(joiner, path.split('/'), [])
res = '/'.join(nice)
print res