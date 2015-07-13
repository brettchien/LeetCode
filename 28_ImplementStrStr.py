class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        idx = 0
        while idx <= len(haystack) - len(needle):
            if haystack[idx] != needle[0]:
                pass
            else:
                match = True
                for i in range(1, len(needle)):
                    if haystack[idx+i] != needle[i]:
                        match = False
                        break
                if match:
                    return idx
            idx += 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.strStr("mississippi", "mississippi")
