from typing import Optional, List

from basic_class import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        temp = [root]
        while temp:
            res.append(self.get_avg(temp))
            for _ in range(len(temp)):
                cur = temp.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
        return res

    def get_avg(self,node_list = []):
        return sum([k.val for k in node_list])/len(node_list)

