# -*- coding:utf-8 -*-

# <SUBID:17612566,UPDATE:20220325>
# English:
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
# Example 1:
# Input: words = ["gin","zen","gig","msg"] Output: 2 Explanation: The transformation of each word is: "gin" -> "--...-." "zen" -> "--...-." "gig" -> "--...--." "msg" -> "--...--." There are 2 different transformations: "--...-." and "--...--.".
# Example 2:
# Input: words = ["a"] Output: 1
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.
#
# 中文:
# 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如:
# 'a' 对应 ".-" ，
# 'b' 对应 "-..." ，
# 'c' 对应 "-.-." ，以此类推。
# 为了方便，所有 26 个英文字母的摩尔斯密码表如下：
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# 给你一个字符串数组 words ，每个单词可以写成每个字母对应摩尔斯密码的组合。
# 例如，"cab" 可以写成 "-.-..--..." ，(即 "-.-." + ".-" + "-..." 字符串的结合)。我们将这样一个连接过程称作 单词翻译 。
# 对 words 中所有单词进行单词翻译，返回不同 单词翻译 的数量。
# 示例 1：
# 输入: words = ["gin", "zen", "gig", "msg"] 输出: 2 解释: 各单词翻译如下: "gin" -> "--...-." "zen" -> "--...-." "gig" -> "--...--." "msg" -> "--...--." 共有 2 种不同翻译, "--...-." 和 "--...--.".
# 示例 2：
# 输入：words = ["a"] 输出：1
# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] 由小写英文字母组成


#
# @lc app=leetcode.cn id=804 lang=python
#
# [804] 旋转数字
#
# https://leetcode-cn.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (70.20%)
# Total Accepted:    10.2K
# Total Submissions: 14.5K
# Testcase Example:  '["gin", "zen", "gig", "msg"]'
#
# 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如: "a" 对应 ".-", "b" 对应 "-...",
# "c" 对应 "-.-.", 等等。
#
# 为了方便，所有26个英文字母对应摩尔斯密码表如下：
#
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# 给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，"cab" 可以写成 "-.-..--..."，(即 "-.-." + "-..."
# + ".-"字符串的结合)。我们将这样一个连接过程称作单词翻译。
#
# 返回我们可以获得所有词不同单词翻译的数量。
#
# 例如:
# 输入: words = ["gin", "zen", "gig", "msg"]
# 输出: 2
# 解释:
# 各单词翻译如下:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# 共有 2 种不同翻译, "--...-." 和 "--...--.".
#
#
#
#
# 注意:
#
#
# 单词列表words 的长度不会超过 100。
# 每个单词 words[i]的长度范围为 [1, 12]。
# 每个单词 words[i]只包含小写字母。
#
#
#
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes_map = dict(zip('abcdefghijklmnopqrstuvwxyz', codes))
        ret = set()
        for word in words:
            ret.add(''.join([codes_map[i] for i in word]))
        return len(ret)

if __name__ == "__main__":
    s = Solution().uniqueMorseRepresentations( ["gin", "zen", "gig", "msg"])
    print(s)

