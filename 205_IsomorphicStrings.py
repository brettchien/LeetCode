class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return False
        chmap = {}
        chmap[s[0]] = t[0]
        for idx in range(1, len(s)):
            if s[idx] == s[idx-1]:
                if t[idx] != t[idx-1]:
                    return False
            else:
                if t[idx] == t[idx-1]:
                    return False
                else:
                    if s[idx] in chmap:
                        if t[idx] != chmap[s[idx]]:
                            return False
                    else:
                        chmap[s[idx]] = t[idx]
        return True


    def aisIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return False
        rla = self.runLength(s)
        rlb = self.runLength(t)
        if len(rla) != len(rlb):
            return False
        else:
            chmap = {}
            for idx in range(len(rla)):
                ach, acount = rla[idx]
                bch, bcount = rlb[idx]
                if acount != bcount:
                    return False
                else:
                    if ach not in chmap:
                        chmap[ach] = bch
                    else:
                        if bch != chmap[ach]:
                            return False
            return True

    
    def runLength(self, s):
        result = [[s[0], 1]]
        for idx in range(1, len(s)):
            if s[idx] == s[idx-1]:
                result[-1][1] += 1
            else:
                result.append([s[idx], 1])
        return result
            

if __name__ == "__main__":
    sol = Solution()
    print sol.runLength("abc")
    print sol.runLength("egg")
    print sol.isIsomorphic("abc", "def")
    print sol.isIsomorphic("foo", "bar")
    print sol.isIsomorphic("foo", "egg")
    print sol.isIsomorphic("paper", "title")
    print sol.isIsomorphic("paper", "tidle")
