class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res<<1) | (n&1)
            n>>=1
        return res
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_s = format(n, '032b')
        s = bin_s[::-1]
        return int(s,2)
"""