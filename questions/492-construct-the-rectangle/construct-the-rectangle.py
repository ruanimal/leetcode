# -*- coding:utf-8 -*-


# English:
# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
# The area of the rectangular web page you designed must equal to the given target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
# Example 1:
# Input: area = 4 Output: [2,2] Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. But according to requirement 2, [1,4] is illegal; according to requirement 3, [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
# Example 2:
# Input: area = 37 Output: [37,1]
# Example 3:
# Input: area = 122122 Output: [427,286]
# Constraints:
# 1 <= area <= 107
#
# 中文:
# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
# 你设计的矩形页面必须等于给定的目标面积。
# 宽度 W 不应大于长度 L ，换言之，要求 L >= W 。
# 长度 L 和宽度 W 之间的差距应当尽可能小。
# 返回一个 数组 [L, W]，其中 L 和 W 是你按照顺序设计的网页的长度和宽度。
#
# 示例1：
# 输入: 4 输出: [2, 2] 解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。 但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
# 示例 2:
# 输入: area = 37 输出: [37,1]
# 示例 3:
# 输入: area = 122122 输出: [427,286]
# 提示:
# 1 <= area <= 107


#
# @lc app=leetcode.cn id=492 lang=python
#
# [492] 构造矩形
#
# https://leetcode-cn.com/problems/construct-the-rectangle/description/
#
# algorithms
# Easy (44.73%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 7K
# Testcase Example:  '1'
#
# 作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W
# 且满足以下要求的矩形的页面。要求：
#
#
# 1. 你设计的矩形页面必须等于给定的目标面积。
#
# 2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
#
# 3. 长度 L 和宽度 W 之间的差距应当尽可能小。
#
#
# 你需要按顺序输出你设计的页面的长度 L 和宽度 W。
#
# 示例：
#
#
# 输入: 4
# 输出: [2, 2]
# 解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
# 但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
#
#
# 说明:
#
#
# 给定的面积不大于 10,000,000 且为正整数。
# 你设计的页面的长度和宽度必须都是正整数。
#
#
#
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        base = int(sqrt(area))
        for w in range(base, 0, -1):
            l = area / float(w)
            if l % 1 == 0:
                return sorted([int(w), int(l)], reverse=True)

if __name__ == "__main__":
    s = Solution().constructRectangle(2)
    print(s)


