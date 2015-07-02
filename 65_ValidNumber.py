class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        # remove head and tail spaces
        s = s.strip().lower()
        if len(s) == 0:
            return False
        elif len(s) == 1:
            val = ord(s)
            # digit checking
            if val >= ord('0') and val <= ord('9'):
                return True
            else:
                return False
        else:
            # len >= 2
            # no alphabets except 'e', '.', '+', '-'
            for ch in s:
                val = ord(ch)
                if val >= ord('0') and val <= ord('9'):
                    continue
                elif ch in ['e', '.', '+', '-']:
                    continue
                else:
                    return False
            # last char cannot be 'e'
            if s[-1] == 'e':
                return False
            # first char cannot be 'e'
            if s[0] == 'e':
                return False
            # no space in middle
            if ' ' in s:
                return False
            # check scientific notation
            if 'e' in s:
                fields = s.split("e")
                # only one 'e'
                if len(fields) > 2:
                    return False
                # second half cannot have dot
                if '.' in fields[1]:
                    return False
                if not self.isValidNumber(fields[0]):
                    return False
                if not self.isValidNumber(fields[1]):
                    return False
            else:
                if not self.isValidNumber(s):
                    return False
        return True

    def isValidNumber(self, s):
        if len(s) == 0:
            return False
        elif len(s) == 1:
            val = ord(s)
            if val >= ord('0') and val <= ord('9'):
                return True
            else:
                return False
        else:
            # should have at least one digit
            has_digit = False
            for ch in s:
                val = ord(ch)
                if val >= ord('0') and val <= ord('9'):
                    has_digit = True
                    break
            if not has_digit:
                return False
        # '+', '-' can only be first, cannot be multiple
        if ('+' in s):
            if s.index('+') > 0:
                return False
            if len(s.split('+')) > 2:
                return False
        if ('-' in s):
            if s.index('-') > 0:
                return False
            if len(s.split('-')) > 2:
                return False
        # no multiple dots
        if len(s.split('.')) > 2:
            return False
        return True

        
if __name__ == "__main__":
    sol = Solution()
    print sol.isNumber("") == False
    print sol.isNumber(" 0.1") == True
    print sol.isNumber("abc") == False
    print sol.isNumber("1 a") == False
    print sol.isNumber("2e10") == True
    print sol.isNumber("2e1e0") == False
    print sol.isNumber("2e1E0") == False
    print sol.isNumber("2e0") == True
    print sol.isNumber("3.") == True
    print sol.isNumber(".2") == True
    print sol.isNumber("..") == False
    print sol.isNumber(". 1") == False
    print sol.isNumber(".e1") == False
    print sol.isNumber("-1.") == True
    print sol.isNumber("3-2") == False
    print sol.isNumber("3+2") == False
    print sol.isNumber("+.8") == True
    print sol.isNumber("+++") == False
    print sol.isNumber(" -.") == False
