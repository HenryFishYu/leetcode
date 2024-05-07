import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = True
        return True
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        self.dict.pop(val)
        return True
    def getRandom(self) -> int:
        return random.choice(list(self.dict.keys()))