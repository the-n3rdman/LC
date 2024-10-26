""" 
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return [1]
        last_digit = digits[-1]
        if last_digit == 9:
            result = self.plusOne(digits[:len(digits) -1])
            result.append(0)
            return result
        else:
            digits[-1] = int(last_digit) + 1
            return digits
        

if __name__ == '__main__':
    solution = Solution()
    # digits = [4,3,2,1]
    digits = [9]
    print(solution.plusOne(digits))