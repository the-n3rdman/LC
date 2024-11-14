"""
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        :type nums1: list[int]
        :type m: int
        :type nums2: list[int]
        :type n: int
        """
        if n == 0:
            return
        if m == 0:
            for i in range(m+n):
                nums1[i] = nums2[i]
            return
        j = 0
        for i in range(m+n):
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                j += 1
                
        
                

if __name__ == '__main__':
    solution = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3] 
    n = 3
    print(solution.merge(nums1, m, nums2, n))
    print(nums1, nums2)