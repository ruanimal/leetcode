# -*- coding:utf-8 -*-

# <SUBID:319203786,UPDATE:20230205>
# English:
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
# Example 1:
# Input: ops = ["5","2","C","D","+"] Output: 30 Explanation: "5" - Add 5 to the record, record is now [5]. "2" - Add 2 to the record, record is now [5, 2]. "C" - Invalidate and remove the previous score, record is now [5]. "D" - Add 2 * 5 = 10 to the record, record is now [5, 10]. "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15]. The total sum is 5 + 10 + 15 = 30.
# Example 2:
# Input: ops = ["5","-2","4","C","D","9","+","+"] Output: 27 Explanation: "5" - Add 5 to the record, record is now [5]. "-2" - Add -2 to the record, record is now [5, -2]. "4" - Add 4 to the record, record is now [5, -2, 4]. "C" - Invalidate and remove the previous score, record is now [5, -2]. "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4]. "9" - Add 9 to the record, record is now [5, -2, -4, 9]. "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5]. "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14]. The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
# Example 3:
# Input: ops = ["1","C"] Output: 0 Explanation: "1" - Add 1 to the record, record is now [1]. "C" - Invalidate and remove the previous score, record is now []. Since the record is empty, the total sum is 0.
# Constraints:
# 1 <= operations.length <= 1000
# operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
# For operation "+", there will always be at least two previous scores on the record.
# For operations "C" and "D", there will always be at least one previous score on the record.
#
# 中文:
# 你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。
# 比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：
# 整数 x - 表示本回合新获得分数 x
# "+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
# "D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
# "C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
# 请你返回记录中所有得分的总和。
# 示例 1：
# 输入：ops = ["5","2","C","D","+"] 输出：30 解释： "5" - 记录加 5 ，记录现在是 [5] "2" - 记录加 2 ，记录现在是 [5, 2] "C" - 使前一次得分的记录无效并将其移除，记录现在是 [5]. "D" - 记录加 2 * 5 = 10 ，记录现在是 [5, 10]. "+" - 记录加 5 + 10 = 15 ，记录现在是 [5, 10, 15]. 所有得分的总和 5 + 10 + 15 = 30
# 示例 2：
# 输入：ops = ["5","-2","4","C","D","9","+","+"] 输出：27 解释： "5" - 记录加 5 ，记录现在是 [5] "-2" - 记录加 -2 ，记录现在是 [5, -2] "4" - 记录加 4 ，记录现在是 [5, -2, 4] "C" - 使前一次得分的记录无效并将其移除，记录现在是 [5, -2] "D" - 记录加 2 * -2 = -4 ，记录现在是 [5, -2, -4] "9" - 记录加 9 ，记录现在是 [5, -2, -4, 9] "+" - 记录加 -4 + 9 = 5 ，记录现在是 [5, -2, -4, 9, 5] "+" - 记录加 9 + 5 = 14 ，记录现在是 [5, -2, -4, 9, 5, 14] 所有得分的总和 5 + -2 + -4 + 9 + 5 + 14 = 27
# 示例 3：
# 输入：ops = ["1"] 输出：1
# 提示：
# 1 <= ops.length <= 1000
# ops[i] 为 "C"、"D"、"+"，或者一个表示整数的字符串。整数范围是 [-3 * 104, 3 * 104]
# 对于 "+" 操作，题目数据保证记录此操作时前面总是存在两个有效的分数
# 对于 "C" 和 "D" 操作，题目数据保证记录此操作时前面总是存在一个有效的分数


class Solution(object):
    def calPoints(self, ops: List[str]) -> int:
        """简单模拟题目逻辑"""

        ret = []
        for _, i in enumerate(ops):
            if i == '+':
                ret.append(sum(ret[-2:]))
            elif i == 'D':
                ret.append(2*ret[-1] if ret else 0)
            elif i == 'C':
                if ret:
                    ret.pop()
            else:
                ret.append(int(i))
        return sum(ret)

