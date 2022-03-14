# -*- coding:utf-8 -*-


# English:
# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
# Example 1:
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] Explanation: Person 0 has height 5 with no other people taller or the same height in front. Person 1 has height 7 with no other people taller or the same height in front. Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1. Person 3 has height 6 with one person taller or the same height in front, which is person 1. Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3. Person 5 has height 7 with one person taller or the same height in front, which is person 1. Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
# Example 2:
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]] Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
# Constraints:
# 1 <= people.length <= 2000
# 0 <= hi <= 106
# 0 <= ki < people.length
# It is guaranteed that the queue can be reconstructed.
#
# 中文:
# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
# 示例 1：
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 解释： 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。 因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
# 示例 2：
# 输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]] 输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
# 提示：
# 1 <= people.length <= 2000
# 0 <= hi <= 106
# 0 <= ki < people.length
# 题目数据确保队列可以被重建


#
# @lc app=leetcode.cn id=406 lang=python
#
# [406] 根据身高重建队列
#
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (63.11%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 6K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) <= 1:
            return people
        # h代表身高, k代表插队权
        # 按身高倒序, 插队权正序; 根据插队权插到对应的位置, 不影响他前面的人的插队权
        people.sort(key=lambda x: [-x[0], x[1]])
        print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

if __name__ == "__main__":
    s = Solution().reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    print(s)

