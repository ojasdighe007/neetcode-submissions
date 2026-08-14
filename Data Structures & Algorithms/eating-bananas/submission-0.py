import math
class Solution:
    def calcHoursGivenSpeed(self, piles: List[int], k: int) -> int:
        hours_taken = 0
        for val in piles:
            hours_taken += math.ceil(val/k)
        return hours_taken

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile_value = 0
        for val in piles:
            max_pile_value = max(max_pile_value, val)
        
        low = 1
        high = max_pile_value

        answer = max_pile_value

        #print(self.calcHoursGivenSpeed(piles, 2))
        while low <= high:
            mid = int((low + high)/2)
            k = self.calcHoursGivenSpeed(piles, mid)
            if k <= h:
                answer = min(answer,mid)
                high = mid - 1
            else:
                low = mid + 1
        return answer