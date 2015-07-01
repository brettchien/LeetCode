class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ROMAN_NUM = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
        result = 0
        for idx in range(0, len(s) - 1):
            if ROMAN_NUM[s[idx]] < ROMAN_NUM[s[idx + 1]]:
                result -= ROMAN_NUM[s[idx]]
            else:
                result += ROMAN_NUM[s[idx]]
        result += ROMAN_NUM[s[-1]]
        return result

    def romanToInt_1st(self, s):
        ROMAN_NUM = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
        ROMAN_SEQ = ["I", "V", "X", "L", "C", "D", "M"]

        result = 0
        prev = None
        for d in reversed(s):
            if prev:
                idx = ROMAN_SEQ.index(d)
                if ROMAN_SEQ.index(d) < ROMAN_SEQ.index(prev):
                    result -= ROMAN_NUM[d]
                else:
                    result += ROMAN_NUM[d]
            else:
                result += ROMAN_NUM[d]
            prev = d
        return result


if __name__ == "__main__":
    sol = Solution()
    # roman: IXI
    print sol.romanToInt("IX")

