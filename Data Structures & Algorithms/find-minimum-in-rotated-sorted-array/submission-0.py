class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        minimum = 1e4
        while(low <= high):
            mid = int((low + high)/2)
            #print(low,high,mid)
            if nums[low] <= nums[high]:
                return nums[low]
            else:
                if nums[mid] >= nums[low]:
                    low = mid + 1
                else:
                    high = mid
        return minimum