class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity=capacity
        self.cache={}
        self.li=[] #list to check the oldest item
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cache.get(key)==None:
            return -1
        else:
            return self.cache.get(key)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity==0:
            print("Can't perform operations on 0 capacity cache")
        else:
            if self.cache.get(key)==None:
                if len(self.cache)>=self.capacity:
                    x=self.li.pop(0)
                    self.cache.pop(x)
                    self.cache[key]=value
                    self.li.append(key)
                else:
                    self.cache[key]=value
                    self.li.append(key)
            else:
                self.cache[key]=value
                self.li.remove(key)
                self.li.append(key)
        
            

# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1
