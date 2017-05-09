'''
https://leetcode.com/problems/reverse-linked-list/?tab=Description

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/

Write a function to reverse a linked list
Given pointer to the head node of a linked list, the task is to reverse the linked list.

Examples:

Input : Head of following linked list  
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL

Input : Head of following linked list  
       1->2->3->4->5->NULL
Output : Linked list should be changed to,
       5->4->3->2->1->NULL

Input : NULL
Output : NULL

Input  : 1->NULL
Output : 1->NULL

Recursive Method:

   1) Divide the list in two parts - first node and rest of the linked list.
   2) Call reverse for the rest of the linked list.
   3) Link rest to first.
   4) Fix head pointer

'''
# Simple and tail recursive Python program to 
# reverse a linked list
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
 
    def reverseUtil(self, curr, prev):
         
        # If last node mark it head
        if curr.next is None :
            self.head = curr 
             
            # Update next to prev node
            curr.next = prev
            return
         
        # Save curr.next node for recursive call
        next = curr.next
 
        # And update next 
        curr.next = prev
     
        self.reverseUtil(next, curr) 
 
 
    # This function mainly calls reverseUtil()
    # with previous as None
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
 
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
 
print "Given linked list"
llist.printList()
 
llist.reverse()
 
print "\nReverse linked list"
llist.printList()
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)