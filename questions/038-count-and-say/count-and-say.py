# -*- coding:utf-8 -*-

# <SUBID:19454752,UPDATE:20220325>
# English:
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
# For example, the saying and conversion for digit string "3322251":
# Given a positive integer n, return the nth term of the count-and-say sequence.
# Example 1:
# Input: n = 1 Output: "1" Explanation: This is the base case.
# Example 2:
# Input: n = 4 Output: "1211" Explanation: countAndSay(1) = "1" countAndSay(2) = say "1" = one 1 = "11" countAndSay(3) = say "11" = two 1's = "21" countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
# Constraints:
# 1 <= n <= 30
#
# 中文:
# 给定一个正整数 n ，输出外观数列的第 n 项。
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
# 你可以将其视作是由递归公式定义的数字字符串序列：
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
# 前五项如下：
# 1. 1 2. 11 3. 21 4. 1211 5. 111221 第一项是数字 1 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11" 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21" 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211" 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
# 要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。
# 例如，数字字符串 "3322251" 的描述如下图：
# 示例 1：
# 输入：n = 1 输出："1" 解释：这是一个基本样例。
# 示例 2：
# 输入：n = 4 输出："1211" 解释： countAndSay(1) = "1" countAndSay(2) = 读 "1" = 一 个 1 = "11" countAndSay(3) = 读 "11" = 二 个 1 = "21" countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
# 提示：
# 1 <= n <= 30


#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] 报数
#
class Solution:
    f = {}
    def countAndSay(self, n):
        '''
        f[x] ????
        f[x] = baoshu(f[x-1])
        f[0] = str(n)
        '''
        f = Solution.f
        f[0] = str('1')

        def baoshu(string):
            if len(string) == 1:
                return '1' + string
            ret = []
            count = 1
            for i in range(len(string)-1):
                if string[i] != string[i+1]:
                    ret.append('{}{}'.format(count, string[i]))
                    count = 1
                    continue
                count += 1
            ret.append('{}{}'.format(count, string[-1]))
            return ''.join(ret)
        for i in range(1, n):
            f[i] = baoshu(f[i-1])
        return f[n-1]
if __name__ == "__main__":
    s = Solution().countAndSay(1)
    print(s)


