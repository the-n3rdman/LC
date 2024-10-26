""" 
    You are given a string s consisting of lowercase English letters, and an integer k. Your task is to convert the string into an integer by a special process, and then transform it by summing its digits repeatedly k times. More specifically, perform the following steps:

    Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
    Transform the integer by replacing it with the sum of its digits.
    Repeat the transform operation (step 2) k times in total.
    For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

    Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
    Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
    Transform #2: 17 ➝ 1 + 7 ➝ 8
    Return the resulting integer after performing the operations described above.
"""
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mapping = {
            'a':'1','b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8',
            'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15',
            'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22',
            'w':'23', 'x':'24', 'y':'25', 'z':'26'}
        num = ""
        for c in s:
            value = mapping[c]
            num += value
        nums = int(num)
        for i in range(k):
            sum_value = 0
            while nums >0:
                sum_value += nums%10
                nums = nums//10
            nums = sum_value
        return nums
    
    
if __name__ == '__main__':
    solution = Solution()
    s = 'iiii'
    k = 1
    print(solution.getLucky(s,k))