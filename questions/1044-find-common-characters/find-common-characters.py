# -*- coding:utf-8 -*-

# <SUBID:319946397,UPDATE:20230205>
# English:
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# Example 1:
# Input: words = ["bella","label","roller"] Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"] Output: ["c","o"]
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
# 中文:
# 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。
# 示例 1：
# 输入：words = ["bella","label","roller"] 输出：["e","l","l"]
# 示例 2：
# 输入：words = ["cool","lock","cook"] 输出：["c","o"]
# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 由小写英文字母组成



from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """hash计数法"""

        if len(words) == 1:
            return list(words[0])

        counts = [Counter(s) for s in words]
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
