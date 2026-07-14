class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.min_el = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        self.size += 1

        if len(self.min_el) == 0:
            self.min_el.append(val)    
        elif self.min_el[len(self.min_el) - 1] > val:
            self.min_el.append(val)
        else:
            self.min_el.append(self.min_el[len(self.min_el) - 1])
        

    def pop(self) -> None:
        val = self.stack[self.size - 1]
        self.stack.pop(self.size - 1)
        self.min_el.pop(self.size - 1)
        self.size -= 1
        

    def top(self) -> int:

        return self.stack[self.size - 1]
        

    def getMin(self) -> int:

        return self.min_el[len(self.min_el) - 1]
        
