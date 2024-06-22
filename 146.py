class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:
    # left leste used
    # right last used
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Node) -> None:
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            delete_node = self.left.next
            self.remove(delete_node)
            delete_key = delete_node.key
            del self.cache[delete_key]

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
