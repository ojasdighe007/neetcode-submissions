class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(0,32):
            if n & (1<<i):
                cnt += 1
        return cnt

