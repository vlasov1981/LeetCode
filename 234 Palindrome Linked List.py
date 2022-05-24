class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    left, right = 0, len(nums) - 1
    while right >= left:
        if nums[right] == nums[left]:
            right -= 1
            left += 1
        else:
            return False
    return True


head = [1, 2, 2, 1]
head = ListNode()


print(isPalindrome(head))