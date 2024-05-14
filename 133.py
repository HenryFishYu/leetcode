from collections import deque
from typing import Optional

from basic_class import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node: Optional['Node']):
            if node in oldToNew:
                return oldToNew[node]

            new = Node(node.val)
            oldToNew[node] = new
            for n in node.neighbors:
                new.neighbors.append(dfs(n))
            return new

        return dfs(node)


