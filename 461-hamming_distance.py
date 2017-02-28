# 02/28/2017
# problem description: https://leetcode.com/problems/hamming-distance/?tab=Description
# easy
# author: Xianyue Li

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

solution = Solution()
print(solution.hammingDistance(4, 14))
print(solution.hammingDistance(3, 8))

"""
^: XOR, exclusive OR, results to true if one and only one of the operands true
    0^0 >>> 0
    1^1 >>> 0
    0^1 >>> 1

    8^3 >>> 11    # convert to binary, do XOR compare, convert back and return the result
        1000 (8 in binary)
        0011 (3 in binary)
        ----
        1011 (11 in binary)

    1^2 >>> 3
        01 (1 in binary)
        10 (2 in binary)
        --
        11 (3 in binary)
"""

"""
bin(): convert an int to a binary string
    bin(8) >>> '0b1000'
    bin(3) >>> '0b11'
    bin(3^8) >>> '0b1011'

    '0b' prefix represents binary literal,
    use bin(x)[2:] to get rid of '0b'
"""

"""
.count(): string method, count appearance of a string in another string
    'aaaa'.count('a') >>> 4
    'aaabb'.count('ab') >>> 1
"""
