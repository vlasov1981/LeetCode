class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head):
    prev, current = None, head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev




head = [1, 2, 3, 4, 5]
head = ListNode(head)
print(reverseList(head))