from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()     
        
        length = len(nums)

        if length % 2 == 0:           
            return (nums[length//2] + nums[length//2 - 1]) /2
        
        else:
            return nums[len(nums)//2]

nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))            