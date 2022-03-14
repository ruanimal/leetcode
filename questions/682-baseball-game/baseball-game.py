# -*- coding:utf-8 -*-


# English:
# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.
# Example 1:
# Input: ops = ["5","2","C","D","+"] Output: 30 Explanation: "5" - Add 5 to the record, record is now [5]. "2" - Add 2 to the record, record is now [5, 2]. "C" - Invalidate and remove the previous score, record is now [5]. "D" - Add 2 * 5 = 10 to the record, record is now [5, 10]. "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15]. The total sum is 5 + 10 + 15 = 30.
# Example 2:
# Input: ops = ["5","-2","4","C","D","9","+","+"] Output: 27 Explanation: "5" - Add 5 to the record, record is now [5]. "-2" - Add -2 to the record, record is now [5, -2]. "4" - Add 4 to the record, record is now [5, -2, 4]. "C" - Invalidate and remove the previous score, record is now [5, -2]. "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4]. "9" - Add 9 to the record, record is now [5, -2, -4, 9]. "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5]. "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14]. The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
# Example 3:
# Input: ops = ["1"] Output: 1
# Constraints:
# 1 <= ops.length <= 1000
# ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
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


#
# @lc app=leetcode.cn id=682 lang=python
#
# [682] 棒球比赛
#
# https://leetcode-cn.com/problems/baseball-game/description/
#
# algorithms
# Easy (59.94%)
# Total Accepted:    5.7K
# Total Submissions: 9.2K
# Testcase Example:  '["5","2","C","D","+"]'
#
# 你现在是棒球比赛记录员。
# 给定一个字符串列表，每个字符串可以是以下四种类型之一：
# 1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
# 2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
# 3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
# 4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。
#
# 每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
# 你需要返回你在所有回合中得分的总和。
#
# 示例 1:
#
# 输入: ["5","2","C","D","+"]
# 输出: 30
# 解释:
# 第1轮：你可以得到5分。总和是：5。
# 第2轮：你可以得到2分。总和是：7。
# 操作1：第2轮的数据无效。总和是：5。
# 第3轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
# 第4轮：你可以得到5 + 10 = 15分。总数是：30。
#
#
# 示例 2:
#
# 输入: ["5","-2","4","C","D","9","+","+"]
# 输出: 27
# 解释:
# 第1轮：你可以得到5分。总和是：5。
# 第2轮：你可以得到-2分。总数是：3。
# 第3轮：你可以得到4分。总和是：7。
# 操作1：第3轮的数据无效。总数是：3。
# 第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。
# 第5轮：你可以得到9分。总数是：8。
# 第6轮：你可以得到-4 + 9 = 5分。总数是13。
# 第7轮：你可以得到9 + 5 = 14分。总数是27。
#
#
# 注意：
#
#
# 输入列表的大小将介于1和1000之间。
# 列表中的每个整数都将介于-30000和30000之间。
#
#
#
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ret = []
        for idx, i in enumerate(ops):
            if i == '+':
                ret.append(sum(ret[-2:]))
            elif i == 'D':
                ret.append(2*ret[-1] if ret else 0)
            elif i == 'C':
                if ret:
                    ret.pop()
            else:
                ret.append(int(i))
        # print(ret)
        return sum(ret)

if __name__ == "__main__":
    s = Solution().calPoints(["5","2","C","D","+"])
    print(s)
    s = Solution().calPoints(["5","-2","4","C","D","9","+","+"])
    print(s)

