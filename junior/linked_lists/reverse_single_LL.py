# Reverse a single linked list when the head of the list is given
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val                   # self is like this in java.
        self.next = next                 # used to access the variable associated with the current instance


class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def list_print(self):
        curr_node = self.head
        while curr_node:                   # while curr_node is not None
            print(curr_node.val, end=' ')  # printing on same line using end
            curr_node = curr_node.next
        print('\n')


# head -> 1 -> 2 -> 3 -> 4 -> None          prev -> None <- 1 <- 2 <- 3 <- 4   None <- curr
class Solution(object):
    @staticmethod
    def reverse_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next_ = curr.next  # secure the rest of the list node
            curr.next = prev   # make the current node point to previous
            prev = curr        # current node becomes previous
            curr = next_       # set the next node to current and loop to next iteration
        return prev            # prev now points to the last node which is the new head


#   Driver code
# Creation of a linked list
list = SingleLinkedList()
list.head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
list.head.next = n2
n2.next = n3
n3.next = n4

list.list_print()
reversed_list = SingleLinkedList()
reversed_list.head = Solution.reverse_list(list.head)  # use static method when calling from the outside
reversed_list.list_print()

# What is a static method?
#
# Static methods, much like class methods, are methods that are bound to a class rather than its object.
# They do not require a class instance creation. So, they are not dependent on the state of the object.
#
# The difference between a static method and a class method is:
#
# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.

