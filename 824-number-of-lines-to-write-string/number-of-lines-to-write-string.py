# -*- coding:utf-8 -*-


# English:
# We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.
# Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.
# Example : Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] S = "abcdefghijklmnopqrstuvwxyz" Output: [3, 60] Explanation: All letters have the same length of 10. To write all 26 letters, we need two full lines and one line with 60 units.
# Example : Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] S = "bbbcccdddaaa" Output: [2, 4] Explanation: All letters except 'a' have the same length of 10, and "bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units. For the last 'a', it is written on the second line because there is only 2 units left in the first line. So the answer is 2 lines, plus 4 units in the second line.
# Note:
# The length of S will be in the range [1, 1000].
# S will only contain lowercase letters.
# widths is an array of length 26.
# widths[i] will be in the range of [2, 10].
#
# 中文:
# 我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。
# 现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
# 示例 1: 输入: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] S = "abcdefghijklmnopqrstuvwxyz" 输出: [3, 60] 解释: 所有的字符拥有相同的占用单位10。所以书写所有的26个字母， 我们需要2个整行和占用60个单位的一行。
# 示例 2: 输入: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] S = "bbbcccdddaaa" 输出: [2, 4] 解释: 除去字母'a'所有的字符都是相同的单位10，并且字符串 "bbbcccdddaa" 将会覆盖 9 * 10 + 2 * 4 = 98 个单位. 最后一个字母 'a' 将会被写到第二行，因为第一行只剩下2个单位了。 所以，这个答案是2行，第二行有4个单位宽度。
# 注:
# 字符串 S 的长度在 [1, 1000] 的范围。
# S 只包含小写字母。
# widths 是长度为 26的数组。
# widths[i] 值的范围在 [2, 10]。


#
# @lc app=leetcode.cn id=806 lang=python
#
# [806] 写字符串需要的行数
#
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        widths_map = dict(zip('abcdefghijklmnopqrstuvwxyz', widths))
        length = 0
        for i in S:
            if (length + widths_map[i]) > (length // 100 + 1) * 100:
                length = (length // 100 + 1) * 100
            length += widths_map[i]
        a, b = divmod(length, 100)
        if b:
            return [a + 1, b]
        return a, b


if __name__ == "__main__":
    s = Solution().numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "bbbcccdddaaa")
    print(s)
    s = Solution().numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "abcdefghijklmnopqrstuvwxyz")
    print(s)


