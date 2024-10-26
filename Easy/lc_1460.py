"""
    You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

    Return true if you can make arr equal to target or false otherwise.
"""
from collections import Counter
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        c1 = Counter(target)
        c2 = Counter(arr)

        if c1 == c2:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    target = [1,2,3,4]
    arr = [2,4,1,3]
    print(solution.canBeEqual(target, arr))