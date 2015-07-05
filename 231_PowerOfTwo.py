class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n -1) == 0)
        
    def aisPowerOfTwo(self, n):
        if n == 0:
            return False
        target = "{0:b}".format(n)
        for idx in range(1, len(target)):
            if target[idx] == '1':
                return False
        return True
            
