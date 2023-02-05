# -*- coding:utf-8 -*-

# <SUBID:308464902,UPDATE:20230205>
# English:
# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.
# Implement the SummaryRanges class:
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
# Example 1:
# Input ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"] [[], [1], [], [3], [], [7], [], [2], [], [6], []] Output [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]] Explanation SummaryRanges summaryRanges = new SummaryRanges(); summaryRanges.addNum(1); // arr = [1] summaryRanges.getIntervals(); // return [[1, 1]] summaryRanges.addNum(3); // arr = [1, 3] summaryRanges.getIntervals(); // return [[1, 1], [3, 3]] summaryRanges.addNum(7); // arr = [1, 3, 7] summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]] summaryRanges.addNum(2); // arr = [1, 2, 3, 7] summaryRanges.getIntervals(); // return [[1, 3], [7, 7]] summaryRanges.addNum(6); // arr = [1, 2, 3, 6, 7] summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
# Constraints:
# 0 <= value <= 104
# At most 3 * 104 calls will be made to addNum and getIntervals.
# Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?
#
# 中文:
# 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
# 实现 SummaryRanges 类：
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
# 示例：
# 输入： ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"] [[], [1], [], [3], [], [7], [], [2], [], [6], []] 输出： [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]] 解释： SummaryRanges summaryRanges = new SummaryRanges(); summaryRanges.addNum(1); // arr = [1] summaryRanges.getIntervals(); // 返回 [[1, 1]] summaryRanges.addNum(3); // arr = [1, 3] summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]] summaryRanges.addNum(7); // arr = [1, 3, 7] summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]] summaryRanges.addNum(2); // arr = [1, 2, 3, 7] summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]] summaryRanges.addNum(6); // arr = [1, 2, 3, 6, 7] summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
# 提示：
# 0 <= val <= 104
# 最多调用 addNum 和 getIntervals 方法 3 * 104 次
# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?



class SummaryRanges:
    def __init__(self):
        self.data = [[-10, -10], [10010, 10010]]  # 最大边界和最小边界, 简化越界处理

    def addNum(self, val: int) -> None:
        left = 0
        right = len(self.data)-1
        while left < right:
            mid = (left+right) >> 1
            if self.data[mid][0] < val:
                left = mid + 1
            else:
                right = mid
        # self.data[left][0] >= val
        # 如: [(1, 1), (4, 4)] add 3
        # 我们找到一个区间 (self.data[left-1][0], self.data[left][0]]
        # val所在区间有下面几种情况
        # (start1, end1], [end1+1, end1+1] (end1+1, start2-1) [start2-1, start2-1] [start2, start2]
        if self.data[left][0] == val:  # 已存在
            return
        if self.data[left-1][1] >= val: # (start1, end1]
            return
        # (end1+1, start2-1) 且区间只有一个空位, 合并区间
        if self.data[left-1][1]+1 == val == self.data[left][0]-1:
            self.data[left-1][1] = self.data[left][1]
            del self.data[left]
        elif self.data[left-1][1]+1 == val:   # [end1+1, end1+1], 扩展前一个区间的右边界
            self.data[left-1][1] += 1
        elif val == self.data[left][0]-1:  # [start2-1, start2-1], 扩展当前区间的的左边界
            self.data[left][0] -= 1
        else:   # (end1+1, start2-1) 且区间有多个位置, 插入
            self.data.insert(left, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.data[1: -1]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
