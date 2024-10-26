"""
    Given two binary strings a and b, return their sum as a binary string.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """        
        if len(a) < len(b):
            a_rev = a[::-1]
            b_rev = b[::-1]
            min_length = len(a)
        else:
            a_rev = b[::-1]
            b_rev = a[::-1]
            min_length = len(b)
       
        num = ""
        carry = 0
        for i in range(min_length):
            value = int(a_rev[i]) + int(b_rev[i]) + carry
            if value == 3:
                num += "1"
                carry = 1
            elif value == 2:
                num += "0"
                carry = 1
            else:
                num += str(value)
                carry = 0
                
        for i in range(min_length, len(b_rev)):
            value = int(b_rev[i]) + carry
            if value == 2:
                num += "0"
                carry = 1
            else:
                num += str(value)
                carry = 0
        if carry == 1:
            num += "1"
            
        return num[::-1]


if __name__ == '__main__':
    solution = Solution()
    a = "11010" 
    b = "1"
    print(solution.addBinary(a, b))
    