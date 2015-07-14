class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end >= 0:
            if s[end] == ' ':
                end -= 1
            else:
                break
        if end < 0:
            return 0
        start = end - 1
        while start > 0:
            if s[start] != ' ':
                start -= 1
            else:
                break
        return end - start

if __name__ == "__main__":
    sol = Solution()
#    print sol.lengthOfLastWord("b a ")
#    print sol.lengthOfLastWord("a ")
    print sol.lengthOfLastWord("a")
