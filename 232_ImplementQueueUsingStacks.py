class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    # @param x, an integer
    # @return nothing
    def push(self, x):
        # push on stack
        self.stack.append(x)

    # @return nothing
    def pop(self):
        # pop all elements to another stack
        if self.size() == 0:
            return None
        tmp = []
        length = self.size()
        for i in range(length - 1):
            tmp.append(self.stack.pop(-1))
        ans = self.stack.pop(-1)
        for i in range(length - 1):
            self.stack.append(tmp.pop(-1))
        return ans

    # @return an integer
    def peek(self):
        if self.size() == 0:
            return None
        tmp = []
        length = self.size()
        for i in range(length - 1):
            tmp.append(self.stack.pop(-1))
        ans = self.stack.pop(-1)
        self.stack.append(ans)
        for i in range(length - 1):
            self.stack.append(tmp.pop(-1))
        return ans
        
    # @return an boolean
    def empty(self):
        return self.size() == 0
