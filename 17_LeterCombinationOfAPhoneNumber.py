class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
            }
        results = []
        for d in digits:
            if d not in mapping:
                return None
            if results:
                newResults = []
                while results:
                    result = results.pop(0)
                    for ch in mapping[d]:
                        newResults.append(result+ch)
                results = newResults
            else:
                results = [ch for ch in mapping[d]]
        return results

if __name__ == "__main__":
    sol = Solution()
    print sol.letterCombinations("22")

