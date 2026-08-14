class Solution:
    def findPivot(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while(low <= high):
            mid = low + (high - low)//2
            
            if nums[low] <= nums[high]:
                return low
            else:
                if nums[mid] >= nums[low]:
                    low = mid + 1
                else:
                    high = mid
        return -1

    def binary_search(self, nums: List[int], low: int, high: int, target: int) -> int:
        n = len(nums)
        if min(low, high) < 0 or max(low,high) > n:
            return -1

        while(low <= high):
            mid = low + (high - low)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
        

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot_idx = self.findPivot(nums)
        if pivot_idx == -1:
            return -1

        left_answer = self.binary_search(nums,0,pivot_idx-1,target)
        right_answer = self.binary_search(nums,pivot_idx,n-1,target)

        return max(left_answer, right_answer)

        
        