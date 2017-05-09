'''
https://leetcode.com/problems/merge-k-sorted-lists/?tab=Description

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import imp
import heapq

sorted_linked_list = imp.load_source('LinkedList', '/Users/chris/Documents/Development/My Repos/PrivatePythonPlay/leetcode/my/sorted_linked_list.py')

list1 = sorted_linked_list.SortedLinkedList()
for x in [14, 6, 11, 8, 5]:
    list1.add(x)
print "printing list",
list1.print_list()

list2 = sorted_linked_list.SortedLinkedList()
for x in [12, 14, 6, 3, 19]:
    list2.add(x)
print "printing list",
list2.print_list()

list3 = sorted_linked_list.SortedLinkedList()
for x in [12, 19, 1, 2, 3]:
    list3.add(x)
print "printing list",
list3.print_list()

class Solution(object):
    def test(self, lists):
        heap = []
        for n in lists:
            current = n.head
            while current is not None:
                heapq.heappush(heap, current.data)
                current = current.next
        return [ heapq.heappop(heap) for i in range(len(heap)) ]

print Solution().test([list1, list2])
