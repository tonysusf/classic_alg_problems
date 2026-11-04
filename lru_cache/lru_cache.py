from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            print('get', -1)
            return -1
        # Move key to most recently used position
        self.cache.move_to_end(key)
        print('get', key, self.cache[key])
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lru = LRUCache(3)
lru.put(1, 10)
lru.put(2, 20)
lru.put(3, 30)
assert lru.get(3) == 30
lru.put(4, 40)
assert lru.get(1) == -1