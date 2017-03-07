from random import shuffle

list1 = [1,2,3,4,5,6,10]
list2 = [1,2,3,4,5,6,15]
shuffle(list1)
shuffle(list2)

#time complexity should be O(2*n)
#space should be O(1)

print set(list1) - set(list2)
print [i for i in list1 if i not in list2]