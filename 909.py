from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        int_to_position = {}
        r_len = len(board)
        c_len = len(board[0])
        total = r_len*c_len

        key = 1
        count_r=0
        for r in range(r_len-1,-1,-1):
            if count_r%2==0:
                for c in range(c_len):
                    int_to_position[key] = board[r][c] if board[r][c]!=-1 else key
                    key+=1
            else:
                for c in range(c_len-1,-1,-1):
                    int_to_position[key] = board[r][c] if board[r][c]!=-1 else key
                    key+=1

            count_r+=1

        queue.append((0, 1))
        visited.add(int_to_position[1])

        while queue:
            times,end_position = queue.popleft()
            if end_position==total:
                return times
            if end_position<total:
                for i in range(1,7):
                    if end_position+i in int_to_position and int_to_position[end_position+i] not in visited:
                        queue.append((times+1, int_to_position[end_position+i]))
                        visited.add(int_to_position[end_position+i])

        return -1



print(Solution().snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))



