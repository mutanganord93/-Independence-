from queue import Queue
import BinarySearchT

class SeparateChainingHashST:
    def __init__(self,size):
        self.size = size
        self.array = []
        for i in range(self.size):
            self.array.append(BinarySearchT.BinarySearchTree())

    def hashFunc(self,key):
        return (hash(key) & 0x7fffffff) % self.size

    def put(self,key,val):
        hashval = self.hashFunc(key)
        self.array[hashval].insert(val)

    #changed the find function to search for the values at location
    def find(self,key):
        hashval = self.hashFunc(key)
        return self.array[hashval].walk()
    
    def keys(self):
        for i in range(self.size):
            print(f"{i} {self.array[i].walk()}")






