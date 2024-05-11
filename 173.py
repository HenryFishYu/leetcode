from collections import deque
from typing import Optional

from basic_class import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        while root:
            self.arr.append(root)
            root = root.left

    def next(self) -> int:
        res = self.arr.pop()
        temp = res.right
        while temp:
            self.arr.append(temp)
            temp = temp.left
        return res.val
    def hasNext(self) -> bool:
        return self.arr

