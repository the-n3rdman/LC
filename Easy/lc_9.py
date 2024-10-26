"""
    Given an integer x, return true if x is a palindrome, and false otherwise.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        c = str(x)
        r = c[::-1]
        return c == r
        
        
        
if __name__ == "__main__":
    solution = Solution()
    x = -121
    print(solution.isPalindrome(x))