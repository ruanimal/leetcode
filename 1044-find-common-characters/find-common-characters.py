# -*- coding:utf-8 -*-


# English:
# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
# You may return the answer in any order.
# Example 1:
# Input: ["bella","label","roller"] Output: ["e","l","l"]
# Example 2:
# Input: ["cool","lock","cook"] Output: ["c","o"]
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
#
# 中文:
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。
# 示例 1：
# 输入：["bella","label","roller"] 输出：["e","l","l"]
# 示例 2：
# 输入：["cool","lock","cook"] 输出：["c","o"]
# 提示：
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母


#
# @lc app=leetcode.cn id=1002 lang=python
#
# [1002] 最大宽度坡
#
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 1:
            return list(A[0])

        counts = []
        for s in A:
            t = {}
            for i in s:
                t[i] = t.get(i, 0) + 1
            counts.append(t)
        tmp = {}
        for i in 'abcdefghijklmnopqrstuvwxyz':
            tmp[i] = 100  # max value
            for count in counts:
                if i not in count:
                    tmp[i] = 0
                    break
                tmp[i] = min(tmp[i], count[i])
        ret = []
        for k, v in tmp.items():
            for _ in range(v):
                ret.append(k)
        return ret

if __name__ == "__main__":
    s = Solution().commonChars(["bella","label","roller"])
    print(s)
    s = Solution().commonChars(["cool","lock","cook"])
    print(s)


