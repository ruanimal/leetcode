# -*- coding:utf-8 -*-

# <SUBID:16394789,UPDATE:20220325>
# English:
# You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.
# You are given an array of employees employees where:
# employees[i].id is the ID of the ith employee.
# employees[i].importance is the importance value of the ith employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
# Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.
# Example 1:
# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1 Output: 11 Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3. They both have an importance value of 3. Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
# Example 2:
# Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5 Output: -3 Explanation: Employee 5 has an importance value of -3 and has no direct subordinates. Thus, the total importance value of employee 5 is -3.
# Constraints:
# 1 <= employees.length <= 2000
# 1 <= employees[i].id <= 2000
# All employees[i].id are unique.
# -100 <= employees[i].importance <= 100
# One employee has at most one direct leader and may have several subordinates.
# The IDs in employees[i].subordinates are valid IDs.
#
# 中文:
# 给定一个保存员工信息的数据结构，它包含了员工 唯一的 id ，重要度 和 直系下属的 id 。
# 比如，员工 1 是员工 2 的领导，员工 2 是员工 3 的领导。他们相应的重要度为 15 , 10 , 5 。那么员工 1 的数据结构是 [1, 15, [2]] ，员工 2的 数据结构是 [2, 10, [3]] ，员工 3 的数据结构是 [3, 5, []] 。注意虽然员工 3 也是员工 1 的一个下属，但是由于 并不是直系 下属，因此没有体现在员工 1 的数据结构中。
# 现在输入一个公司的所有员工信息，以及单个员工 id ，返回这个员工和他所有下属的重要度之和。
# 示例：
# 输入：[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1 输出：11 解释： 员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。
# 提示：
# 一个员工最多有一个 直系 领导，但是可以有多个 直系 下属
# 员工数量不超过 2000 。


#
# @lc app=leetcode.cn id=690 lang=python
#
# [690] 员工的重要性
#
# https://leetcode-cn.com/problems/employee-importance/description/
#
# algorithms
# Easy (47.50%)
# Total Accepted:    2.8K
# Total Submissions: 5.7K
# Testcase Example:  '[[1,2,[2]], [2,3,[]]]\n2'
#
# 给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。
#
# 比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。那么员工1的数据结构是[1, 15,
# [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5,
# []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。
#
# 现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。
#
# 示例 1:
#
#
# 输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# 输出: 11
# 解释:
# 员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
#
#
# 注意:
#
#
# 一个员工最多有一个直系领导，但是可以有多个直系下属
# 员工数量不超过2000。
#
#
#
"""
# Employee info
"""
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

    def __repr__(self):
        return 'Employee(%r, %r, %r)' % (self.id, self.importance, self.subordinates)

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def count_total(node):
            if not node.subordinates:
                node.total_importance = node.importance
                return node.total_importance

            node.total_importance = node.importance + sum([count_total(e_map[i]) for i in node.subordinates])
            return node.total_importance

        e_map = {i.id:i for i in employees}
        e = e_map[id]
        return count_total(e)

if __name__ == "__main__":
    data = [Employee(101, 3, []), Employee(2, 5, [101])]
    s = Solution().getImportance(data, 2)
    print(s)
    data = [Employee(1, 5, [2,3]), Employee(2, 3, []), Employee(3, 3, [])]
    s = Solution().getImportance(data, 1)
    print(s)

