# -*- coding:utf-8 -*-


# English:
# We have two special characters:
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
# Example 1:
# Input: bits = [1,0,0] Output: true Explanation: The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
# Example 2:
# Input: bits = [1,1,1,0] Output: false Explanation: The only way to decode it is two-bit character and two-bit character. So the last character is not one-bit character.
# Constraints:
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.
#
# 中文:
# 有两种特殊字符：
# 第一种字符可以用一比特 0 表示
# 第二种字符可以用两比特（10 或 11）表示
# 给你一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。
# 示例 1:
# 输入: bits = [1, 0, 0] 输出: true 解释: 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。 所以最后一个字符是一比特字符。
# 示例 2:
# 输入：bits = [1,1,1,0] 输出：false 解释：唯一的解码方式是将其解析为两比特字符和两比特字符。 所以最后一个字符不是一比特字符。
# 提示:
# 1 <= bits.length <= 1000
# bits[i] 为 0 或 1


#
# @lc app=leetcode.cn id=717 lang=python
#
# [717] 1比特与2比特字符
#
# https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (41.79%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 14.9K
# Testcase Example:  '[1,0,0]'
#
# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
#
# 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
#
# 示例 1:
#
#
# 输入:
# bits = [1, 0, 0]
# 输出: True
# 解释:
# 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
#
#
# 示例 2:
#
#
# 输入:
# bits = [1, 1, 1, 0]
# 输出: False
# 解释:
# 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
#
#
# 注意:
#
#
# 1 <= len(bits) <= 1000.
# bits[i] 总是0 或 1.
#
#
#
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                if i+2 < len(bits):
                    i += 2
                else:
                    break
            else:
                if i+1 < len(bits):
                    i += 1
                else:
                    break
        # print(i)
        if bits[i:] == [0]:
            return True
        return False

if __name__ == "__main__":
    s = Solution().isOneBitCharacter(bits = [1, 0, 0])
    print(s)
    s = Solution().isOneBitCharacter(bits = [1, 1, 1, 0])
    print(s)


