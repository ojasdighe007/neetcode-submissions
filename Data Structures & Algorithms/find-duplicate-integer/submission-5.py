class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n):
            #print(nums[abs(nums[i])-1])
            if nums[abs(nums[i])-1] < 0:
                return abs(nums[i])
            nums[abs(nums[i])-1] *= -1
        return -1