class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cnt = 0
        for val in nums:
            if val == 0:
                cnt += 1
            else:
                prod *= val
        
        productExceptSelfList: List[int] = []
        for i, val in enumerate(nums):
            if (cnt > 1) or (cnt == 1 and val):
                productExceptSelfList.append(0)
            elif cnt == 1 and val == 0:
                productExceptSelfList.append(int(prod))
            else:
                productExceptSelfList.append(int(prod/val))
        return productExceptSelfList
