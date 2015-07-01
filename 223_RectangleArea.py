class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        # two sqaure
        S1 = (C - A) * (D - B)
        S2 = (G - E) * (H - F)
        # check if overlap
        overlap = 0
        if E >= C or F >= D or A >=G or B >= H:
            overlap = 0
        else:
            # overlap
            width = max(A, E) - min(C, G)
            height = max(B, F) - min(D, H)
            overlap = width * height
        return S1 + S2 - overlap

if __name__ == "__main__":
    sol = Solution()
    print sol.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
