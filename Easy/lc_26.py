"""
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        seen = set()
        i=0
        length = len(nums)
        for index in range(length):
            num = nums[i]
            
            if num in seen:
                del nums[i]
                
                
            else:
                i+=1
                k+=1
                seen.add(num)
        return k


if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]    
    print(solution.removeDuplicates(nums), nums)