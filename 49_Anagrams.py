class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        groups = {}
        if len(strs) < 2:
            return []
        for phrase in strs:
            sorted_phrase = "".join(sorted(phrase))
            if sorted_phrase not in groups:
                groups[sorted_phrase] = [phrase]
            else:
                groups[sorted_phrase].append(phrase)
        results = []
        for result in groups.values():
            if len(result) > 1:
                results += result
        return results
        
if __name__ == "__main__":
    sol = Solution()
    print sol.anagrams([""])
    print sol.anagrams(["", ""])
