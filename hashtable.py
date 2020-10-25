class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        index = self.calculate_hash_value(string)
        
        if index != None:
          if self.table[index] == None:
            self.table[index] = [string]
          else:
            self.table[index].append(string)
        return -1

    def lookup(self, string):
        index = self.calculate_hash_value(string)

        if index != None:
          if self.table[index] != None:
            if string in self.table[index]:
              return index
        return -1
