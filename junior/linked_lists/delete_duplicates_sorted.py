# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
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


class Solution:
    @staticmethod
    def delete_duplicates(head: ListNode) -> ListNode:
        node = head
        while node and node.next:   # using is not None is more space efficient - singleton
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next
        return head


#   Driver code
# Creation of a linked list
list = SingleLinkedList()
list.head = ListNode(1)
#n2 = ListNode(1)
#n3 = ListNode(3)
#n4 = ListNode(3)
#list.head.next = n2
#n2.next = n3
#n3.next = n4

list.list_print()
Solution.delete_duplicates(list.head.next)
list.list_print()
