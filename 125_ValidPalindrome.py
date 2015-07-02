class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.lower()
        if len(s) in [0, 1]:
            return True
        else:
            start = 0
            end = len(s) - 1
            while end - start > 0:
                while not self.isAlphanumeric(s[start]):
                    if start < end:
                        start += 1
                    else:
                        break
                while not self.isAlphanumeric(s[end]):
                    if end > start:
                        end -= 1
                    else:
                        break
                if start == end:
                    break
#                print start, end
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True
            
    def isAlphanumeric(self, ch):
        val = ord(ch)
#        if val >= ord('0') and val <= ord('9'):
        if val >= 0x30 and val <= 0x39:
            return True
#        if val >= ord('a') and val <= ord('z'):
        if val >= 0x61 and val <= 0x7A:
            return True
        return False
        

if __name__ == "__main__":
    sol = Solution()
    print sol.isAlphanumeric("1")
    print sol.isAlphanumeric("2")
    print sol.isPalindrome("a a") == True
    print sol.isPalindrome("ab") == False
    print sol.isPalindrome(",.") == True
    print sol.isPalindrome("1a2") == False

