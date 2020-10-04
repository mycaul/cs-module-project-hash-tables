class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def insert(self, key, value):
    
        if not self.key:
            self.key = key
            self.value = value

        elif self.key == key:
            self.value = value

        else:
            if not self.next:
                self.next = HashTableEntry(key, value)
            else:
                self.next.insert(key,value)


    def find(self, key):

        if self.key == key:
            return self.value
        else:
            if self.next:
                return self.next.find(key)
            else:
                return None
    def delete(self, key):

        if self.key == key: 
            if not self.next:
                self.key = None
                self.value = None
                return "deleted"
            else:
                self.key = self.next.key
                self.value = self.next.value
                self.next = self.next.next
                return "deleted"
        else:
            if self.next:
                self.next.delete(key)
            else:
                return "Key does not exist"

    def rehashValues(self, ht):

        if self.key:
            ht.put(self.key, self.value, True)
        
        if self.next:
            self.next.rehashValues(ht)
        

    def __len__(self, count = 0):

        if(self.key): count += 1

        if(self.next): count = self.next.__len__(count)

        return count



    def __str__(self):
        return f"({self.key} -- {self.value} -- {self.next.__repr__()}) \n"
    
    def __repr__(self):
        return f"({self.key} -- {self.value} -- {self.next.__repr__()}) \n"

 


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        
        self.capacity = capacity if capacity > MIN_CAPACITY else MIN_CAPACITY;
        self.table = [None] * capacity;

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here

        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here

        numberOfItems = 0

        for i in self.table:
            if i:
                numberOfItems += len(i)
        print(numberOfItems / len(self.table))
        return numberOfItems / len(self.table)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """

        hash = 5381
        
        for c in key:
            hash = (( hash << 5) + hash + ord(c))

        return hash

        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity

        return self.djb2(key) % self.capacity

    def put(self, key, value, rehashing = False):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
    
        if not self.table[index]:
            
            self.table[index] = HashTableEntry(key,value)
        else:

            self.table[index].insert(key,value)
      
        if not rehashing:
            if self.get_load_factor() > .7:
                
                self.resize(self.capacity * 2)
            elif self.get_load_factor() < .2 and self.capacity > MIN_CAPACITY:

                self.resize(self.capacity // 2 if self.capacity // 2 > MIN_CAPACITY else MIN_CAPACITY)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
       
        return self.table[index].delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here

        index = self.hash_index(key)

        return self.table[index].find(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        tempList = []

        [tempList.append(llist) for llist in self.table if llist];
    
        self.table = [None] * new_capacity if new_capacity > MIN_CAPACITY else [None] * MIN_CAPACITY
        self.capacity = new_capacity if new_capacity > MIN_CAPACITY else MIN_CAPACITY
        for ll in tempList:

            ll.rehashValues(self)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    
    print(ht.get_load_factor())

    print("")