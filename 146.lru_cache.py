class ListNode:
    def __init__(self, key=-1, val=-1,nextn=None,pre=None):
        self.key = key
        self.val = val
        self.next = nextn
        self.pre = pre

class LRUCache:
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0

        self.head = self.tail =ListNode(-1,-1)    
        self.cache = dict()
    
    def move_to_end(self, cnode):
        if cnode.next:
            self.tail.next = cnode
            cnode.pre.next = cnode.next
            cnode.next.pre = cnode.pre
            cnode.next = None
            cnode.pre =  self.tail
            self.tail = self.tail.next

    def remove_least(self):
        rm_key = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        self.cache.pop(rm_key,None)

    def get(self, key: int) -> int:
        cnode = self.cache.get(key,-1)        

        if cnode == -1:
            return -1

        self.move_to_end(cnode)
        return cnode.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            cnode = self.cache[key]
            self.move_to_end(cnode)
            cnode.val = value
            return

        self.tail.next = ListNode(key,value,pre=self.tail)
        self.cache[key] = self.tail.next
        self.tail = self.tail.next
        
        if self.size==self.capacity:
            self.remove_least()       
        else:
            self.size += 1
        
# ALTERNATE

import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderDic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.orderDic:
            return -1
        val = self.orderDic[key]
        self.orderDic.move_to_end(key,last=False)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.orderDic:
            self.orderDic.move_to_end(key, last=False)
            self.orderDic[key]=value
        else:
            self.orderDic[key] = value
            self.orderDic.move_to_end(key, last=False)
            while len(self.orderDic) > self.capacity:
                self.orderDic.popitem()
        