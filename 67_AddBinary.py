class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        result = ""
        if len(b) > len(a):
            a, b = b, a
        carry = False
        while len(a):
            x = a[-1]
            a = a[:-1]
            y = '0'
            if len(b):
                y = b[-1]
                b = b[:-1]
            digit = '0'
            if carry:
                if x == '1' and y == '1':
                    digit = '1'
                elif x == '0' and y == '0':
                    digit = '1'
                    carry = False
                else:
                    digit = '0'
            else:
                if x == '1' and y == '1':
                    digit = '0'
                    carry = True
                elif x == '0' and y == '0':
                    digit = '0'
                else:
                    digit = '1'
            result = digit + result
        if carry:
            result = "1" + result
        return result
            
       
if __name__ == "__main__":
    sol = Solution()
#    print sol.addBinary("1010", "1011")
    print sol.addBinary("11", "1")

