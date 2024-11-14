"""
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        :type nums: list[int]
        :rtype: int
        """   
        ### NOT USING CONSTANT SPACE CURRENTLY ###
        seen = set()
        for elem in nums:
            if elem in seen:
                seen.remove(elem)
            else:
                seen.add(elem)
        return seen.pop()

if __name__ == '__main__':
    solution = Solution()
    nums = [4,1,2,1,2]
    print(solution.singleNumber(nums))