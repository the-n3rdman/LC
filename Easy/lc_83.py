"""
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
""" 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n1 = head
        if head is None:
            return None
        while not head.next == None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return n1
    


if __name__ == '__main__':
    solution = Solution()
    head = [1,1,2,3,3]
    l1 = ListNode(val=1)
    l2 = ListNode(val=1)
    l3 = ListNode(val=2)
    l4 = ListNode(val=3)
    l5 = ListNode(val=3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    
    answer = solution.deleteDuplicates(l1)
    
    while True:
        print(str(answer.val)+'->')
        answer = answer.next
        if answer is None:
            break
