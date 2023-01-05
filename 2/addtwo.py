from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # make it printable    
    def __str__(self):
        return f'{self.val} -> {self.next}'
    
    # make it iterable
    def __iter__(self):
        yield self.val
        if self.next:
            yield from self.next


class Solution:
     
    # using iterator, not accepted because cannot modify the Class ListNode
    def add2Numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        for a, b in zip(l1, l2):
            carry, val = divmod(a + b + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return head.next

    # using  divmod, accepted
    def add22Numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            carry, val = divmod(a + b + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

    # using ternary operator and carry sum, accepted
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            sum = a + b + carry
            carry = 0
            if sum > 9:
                carry = 1
                sum -= 10
            curr.next = ListNode(sum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


if __name__ == '__main__':

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    ls = Solution().addTwoNumbers(l1, l2)
    
    
    print(ls)