class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        results = []
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 0
        elif len(s) == 2:
            if s[0] == s[1]:
                return 0
            else:
                return 1
        else:
            # length > 2
            if self.checkPalindrome(s):
                return 0
            start = 0
            while True:
                tmp = s
                result = []
                if start > 0:
 #                   print 'e', tmp[:start]
                    if self.checkPalindrome(tmp[:start]):
                        result.append(tmp[:start])
                        tmp = tmp[start:]
                    else:
                        break
                if len(tmp) == 0:
                    break
 #               print tmp
                while len(tmp) > 0:
                    if self.checkPalindrome(tmp):
                        result.append(tmp)
                        tmp = ""
                        break
                    for idx in range(len(tmp), 0, -1):
                        if self.checkPalindrome(tmp[:idx]):
                            result.append(tmp[:idx])
                            tmp = tmp[idx:]
                            break
                print result
                results.append(len(result) - 1)
                start += 1
        print results
        return min(results)

    def checkPalindrome(self, s):
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        else:
            pivot = len(s) / 2
            first = s[:pivot]
            second = s[-pivot:]
            # reverse second halve 
            second = second[::-1]
            return first == second
    
if __name__ == "__main__":
    sol = Solution()
    print sol.minCut("aab") == 1
#    print sol.checkPalindrome("aa") == True
#    print sol.checkPalindrome("aab") == False
#    print sol.checkPalindrome("aabb") == False
#    print sol.checkPalindrome("abba") == True
#    print sol.checkPalindrome("abcba") == True
#    print sol.checkPalindrome("dcabcbacd") == True
    print sol.minCut("cdd") == 1
    print sol.minCut("abbab") == 1
    print sol.minCut("aaabaa") == 1
    print sol.minCut("fff") == 0
    print sol.minCut("eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj") == 42
