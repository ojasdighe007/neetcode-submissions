class Solution:
    def searchNumberOfElementsLTE(self, nums: List[int], value: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        prev_mid = -1

        answer = 0
        while low <= high:
            mid = low + (high - low)//2
            if prev_mid == mid:
                break
            elif nums[mid] <= value:
                low = mid+1
                answer = mid+1
            else:
                high = mid-1
            prev_mid = mid

        return answer

    def findValue(self, nums1: List[int], nums2: List[int], median_pos: int) -> int:
        n = len(nums1)
        m = len(nums2)

        low = -1e7
        high = 1e7
        median = 1e7
        while low <= high:
            mid = low + (high - low)//2

            first = self.searchNumberOfElementsLTE(nums1,mid)
            second = self.searchNumberOfElementsLTE(nums2,mid)
            
            if first + second < median_pos+1:
                low = mid + 1
            else:
                median = min(median, mid)
                high = mid
            #print(mid, first, second, median)
            if low == high:
                break
        print(median)
        return median

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        median_pos = (m+n-1)//2

        # print(self.searchNumberOfElementsLTE(nums1,3))
        # print(self.searchNumberOfElementsLTE(nums2,3))

        median = self.findValue(nums1,nums2,median_pos)
        second_median = self.findValue(nums1,nums2,median_pos+1)
        #second_median = 4
        #print(median, second_median)
        if ((m + n)% 2) == 0:
            return (median + second_median)/2
        
        return median