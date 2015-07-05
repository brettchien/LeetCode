class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 10 and x > -10:
            return x
        sign = 1
        if x < 0:
            sign = -1
        x = sign * x
        result = 0
        print x
        while x > 0:
            print x, result
            result = result * 10 + x % 10
            x /= 10
        return result * sign
            
if __name__ == "__main__":
    sol = Solution()
    print sol.reverse(123) == 321
    print sol.reverse(-123) == -321
