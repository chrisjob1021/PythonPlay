'''
https://leetcode.com/problems/merge-two-sorted-lists/?tab=Description

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

'''

import imp
sorted_linked_list = imp.load_source('SortedLinkedList', '/Users/chris/Documents/Development/My Repos/PrivatePythonPlay/leetcode/my/sorted_linked_list.py')

list1 = sorted_linked_list.SortedLinkedList()
for x in [5, 11, 14, 17, 12]:
    list1.add(x)
print "printing list",
list1.print_list()

list2 = sorted_linked_list.SortedLinkedList()
for x in [6, 10, 18, 4, 9]:
    list2.add(x)
print "printing list",
list2.print_list()

list3 = sorted_linked_list.SortedLinkedList()
list3.mergeTwoListsRecursively(list1, list2)
list3.print_list()

list1.mergeTwoLists(list1, list2)
list1.print_list()