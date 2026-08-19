class Solution:
    def countBits(self, n: int) -> List[int]:
        countBitsList: List[int] = []

        for i in range(0,n+1):
            cnt = 0
            for b in range(0,32):
                if i & (1<<b):
                    cnt += 1
            countBitsList.append(cnt)
        return countBitsList