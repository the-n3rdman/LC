"""
    Given a string s consisting of words and spaces, return the length of the last word in the string.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.strip().split(' ')[-1]
        return len(word)
    

if __name__ == '__main__':
    solution = Solution()
    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s))
