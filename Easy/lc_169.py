"""
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        :type nums: list[int]
        :rtype: int
        """   
        majority = 0
        result = 0
        for num in nums:
            if majority == 0:
                result = num
            if num == result:
                majority = majority + 1
            else:
                majority = majority - 1
         
        return result
    
    
if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    print(solution.majorityElement(nums))