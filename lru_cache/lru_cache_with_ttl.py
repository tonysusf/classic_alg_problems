from collections import OrderedDict
import time

class LRUCacheTTL:
    def __init__(self, capacity, ttl):
        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return None
        value, expires_at = self.cache[key]
        # Check expiration
        if time.time() >= expires_at:
            del self.cache[key]
            return None
        # Mark this key as recently used
        self.cache.move_to_end(key)
        print('get', key, value)
        return value

    def put(self, key, value):
        now = time.time()
        items = list(self.cache.items())
        for k, (v, expires_at) in items:
            if now >= expires_at:
                del self.cache[k]

        self.cache[key] = (value, now + self.ttl)
        self.cache.move_to_end(key)
        while len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        print('put', key, value)

capacity = 3
ttl = 1
lru = LRUCacheTTL(capacity, ttl)

lru.put(1, 10)
lru.put(2, 20)
lru.put(3, 30)
assert lru.get(3) == 30
lru.put(4, 40)
assert lru.get(1) == None
assert len(lru.cache) == 3
time.sleep(1)
lru.put(5, 50)
assert len(lru.cache) == 1
