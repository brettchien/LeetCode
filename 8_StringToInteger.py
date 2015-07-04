class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        positive = True
        signAllowed = True
        spaceAllowed = True
        value = 0
        for ch in str:
            if ch == ' ':
                if spaceAllowed:
                    continue
                else:
                    break
            elif ch == '+':
                if signAllowed:
                    spaceAllowed = False
                    signAllowed = False
                else:
                    return 0
            elif ch == '-':
                if signAllowed:
                    spaceAllowed = False
                    signAllowed = False
                    positive = False
                else:
                    return 0
            elif ch in "0123456789":
                spaceAllowed = False
                digit = ord(ch) - ord('0')
                if value > 214748364 or (value == 214748364 and digit > 7):
                    if positive:
                        return 2147483647
                    else:
                        return -2147483648
                value = value * 10 + digit
            else:
                break
        if not positive:
            value = value * -1
        return value

if __name__ == "__main__":
    sol = Solution()
    print sol.myAtoi("-123") == -123
