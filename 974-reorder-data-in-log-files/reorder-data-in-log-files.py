# -*- coding:utf-8 -*-


# English:
# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
# Return the final order of the logs.
# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"] Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Constraints:
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.
#
# 中文:
# 你有一个日志数组 logs。每条日志都是以空格分隔的字串。
# 对于每条日志，其第一个字为字母数字标识符。然后，要么：
# 标识符后面的每个字将仅由小写字母组成，或；
# 标识符后面的每个字将仅由数字组成。
# 我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。
# 将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按内容字母顺序排序，忽略标识符；在内容相同时，按标识符排序。数字日志应该按原来的顺序排列。
# 返回日志的最终顺序。
# 示例 ：
# 输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"] 输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# 提示：
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] 保证有一个标识符，并且标识符后面有一个字。


#
# @lc app=leetcode.cn id=937 lang=python
#
# [937] 重新排列日志文件
#
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []

        num_logs = []
        alpha_logs = []
        for i in logs:
            sign, content = i.split(' ', 1)
            if content[0].isalpha():
                alpha_logs.append((sign, content))
            else:
                num_logs.append((sign, content))
        alpha_logs.sort(key=lambda i: (i[1], i[0]))
        ret = []
        for i in alpha_logs:
            ret.append(' '.join(i))
        for i in num_logs:
            ret.append(' '.join(i))
        return ret

