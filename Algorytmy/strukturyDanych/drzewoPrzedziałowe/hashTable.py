class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self.hash_function(key)
        step = 0
        while self.table[hash_value] is not None and self.table[hash_value]!='deleted' :
            hash_value = (hash_value + 1) % self.size
            step += 1
        self.table[hash_value] = (key, value)

    def search(self, key):
        hash_value = self.hash_function(key)
        step = 0
        while self.table[hash_value] is not None:
            if self.table[hash_value] != 'deleted' and self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            hash_value = (hash_value + 1) % self.size
            step += 1
        return None

    def delete(self, key):
        hash_value = self.hash_function(key)
        step = 0
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                self.table[hash_value] = 'deleted'
                return True
            hash_value = (hash_value + 1) % self.size
            step += 1
        return False
    
myAssoc=HashTable()
myAssoc.insert('wojciech',10000)
myAssoc.insert('Dawid',100)
myAssoc.delete('wojciech')
print(myAssoc.search('wojciech'))
myAssoc.insert('adam',10000)
myAssoc.insert('kasia',1023)
myAssoc.insert('basia',10000)
myAssoc.insert('Dawidex',100)
print(myAssoc.search('kasia'))
print(myAssoc.search('Dawid'))


