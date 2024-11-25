from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adjs ={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
        puzzle = "".join([str(column) for row in board for column in row])
        queue = deque([(puzzle.index("0"),puzzle,0)])
        visited = set(puzzle)

        while queue:
            indexOfZero,puzzle,moves = queue.popleft()
            if puzzle in visited:
                continue
            visited.add(puzzle)
            if puzzle=="123450":
                return moves

            puzzle_arr = list(puzzle)
            for adjIndex in adjs[indexOfZero]:
                new_puzzle_arr = puzzle_arr.copy()
                new_puzzle_arr[indexOfZero],new_puzzle_arr[adjIndex] = puzzle_arr[adjIndex],puzzle_arr[indexOfZero]
                new_puzzle = "".join(new_puzzle_arr)
                queue.append((new_puzzle.index("0"),new_puzzle,moves+1))
        return -1

