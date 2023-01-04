from statistics import median
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()     
        length = len(nums)
        
        # make floor division to get the index of the middle element

        n = length // 2 - 1
        m = length // 2
        
        if length % 2 == 0:           
            return (nums[n] + nums[m]) /2
        
        else:
            return nums[len(nums)//2]

    def medianStats(self, nums1: List[int], nums2: List[int]) -> float:
        # num = nums1+nums2
        nums1.extend(nums2)
        nums1.sort()
        return median(nums1)

nums1 = [1,2]
nums2 = [3,4]
print(Solution().medianStats(nums1, nums2))