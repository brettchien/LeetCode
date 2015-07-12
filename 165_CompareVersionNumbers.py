class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        fields1 = version1.split('.')
        fields2 = version2.split('.')
        
        while True:
            num1, num2 = 0, 0
            if len(fields1) == 0 and len(fields2) == 0:
                break
            if len(fields1):
                num1 = int(fields1.pop(0))
            if len(fields2):
                num2 = int(fields2.pop(0))
            if num1 == num2:
                continue
            elif num1 > num2:
                return 1
            else:
                return -1
        return 0    
            
if __name__ == "__main__":
    sol = Solution()
#    print sol.compareVersion("1", "1.1")
#    print sol.compareVersion("01", "1")
    print sol.compareVersion("0.1", "1.0")
