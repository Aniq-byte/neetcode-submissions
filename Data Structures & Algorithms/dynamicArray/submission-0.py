class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0 for i in range(self.capacity)]
        self.size = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        if self.array[i] == 0:
            self.size += 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size < self.capacity:
            self.array[self.size] = n
            self.size += 1
        else:
            self.resize()
            self.array[self.size] = n
            self.size += 1


    def popback(self) -> int:
        popped = self.array[self.size - 1]
        self.size -= 1
        return popped
 

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0 for i in range(self.capacity)]

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
