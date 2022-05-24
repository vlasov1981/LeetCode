
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        answer = []

        def traversial(root):
            if root:
                answer.append(root.val)
                for child in root.children:
                    traversial(child)

        traversial(root)
        return answer


