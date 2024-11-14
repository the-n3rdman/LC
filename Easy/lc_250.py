"""
   Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. 
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        p = len(t)
        if not n == p:
            return False
        char_map = {}
        for i in range(n):
            c1 = s[i]
            c2 = t[i]
            if c1 in char_map.keys():
                if char_map[c1] == c2:
                    continue
                else:
                    return False
            else:
                if not c2 in char_map.values():
                    char_map[c1] = c2
                else:
                    return False
        return True
                                  

if __name__ == '__main__':
    solution = Solution()
    s = "badc"
    t = "baba"
    print(solution.isIsomorphic(s, t))