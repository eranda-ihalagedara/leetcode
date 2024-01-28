

# Optimized
class RandomizedSet:
    def __init__(self):
        self.val_set = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.val_set.append(val)
        self.indices[val] = len(self.val_set)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        i = self.indices[val]

        self.indices[self.val_set[-1]] = i
        self.val_set[i] = self.val_set[-1]
        
        self.indices.pop(val)
        self.val_set.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.val_set)