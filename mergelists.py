import itertools

a = [92, 61, 1, 38, 73]
b = [7, 99, 70, 69, 18]
c = [52, 39, 87, 26, 55]


# Time O(nm logn)
# Space O(n+k) where k is length of original lists and n is the new sorted() list
print sorted(list(itertools.chain.from_iterable(itertools.izip(a, b, c))))

a.extend(b)
a.extend(c)
print sorted(a)