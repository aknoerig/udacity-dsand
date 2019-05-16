from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}                           # dict for holding values
        self.capacity = capacity
        self.history = deque([], self.capacity)   # deque to keep track of usage (left is oldest)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache.keys():    
            # cache hit: update history
            self.history.remove(key) # This is O(n) - no idea how to make this O(1)...
            self.history.append(key)
            return self.cache[key]
        # cache miss
        return -1 

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        cache_keys = self.cache.keys()
        if key not in cache_keys:
            if len(cache_keys) == self.capacity:
                # remove oldest entry from cache (and history)
                self.cache.pop( self.history.popleft() )
            self.history.append(key)
        self.cache[key] = value

    def print(self):
        # print cache by usage order (oldest first)
        print('{ ', sep='', end='')
        for key in self.history:
            print(key, self.cache[key], sep=':', end=', ')
        print(' }', sep='', end='')

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.get(1)
our_cache.get(2)
our_cache.get(3)
our_cache.print() # prints 4, 5, 1, 2, 3

our_cache.set(6, 6)
our_cache.set(7, 7)
our_cache.set(8, 8)
our_cache.print() # prints 2, 3, 6, 7, 8
