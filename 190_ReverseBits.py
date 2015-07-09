class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for count in range(32):
            print "{0:b} {1:b}".format(n, result)
            result <<= 1
            result |= n & 1
            n >>= 1
        return result 

    def areverseBits(self, n):
        result = 0
        for count in range(32):
            print "{0:b} {1:b}".format(n, result)
            result <<= 1
            result += n % 2
            n /= 2
        return result 

if __name__ == "__main__":
    sol = Solution()
    print sol.reverseBits(43261596) == 964176192
