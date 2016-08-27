class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        start = 0
        substring = {}
        idx = 0
        while idx < len(s):
            if s[i] not in substring:
                substrings[i] = idx 
            else:
                maxLength = max(i - start, maxLength)
                start  = i
                substring = set(s[i])
        print start, maxLength
        return max(len(s) - start, maxLength) 

        
if __name__ == "__main__":
    sol = Solution()
#    print sol.lengthOfLongestSubstring("c")
#    print sol.lengthOfLongestSubstring("abcabcbb")
    print sol.lengthOfLongestSubstring("dvdf")
