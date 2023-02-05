# -*- coding:utf-8 -*-

# <SUBID:319122179,UPDATE:20230205>
# English:
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
# Example 1:
# Input: root = [3,9,20,null,null,15,7] Output: [3.00000,14.50000,11.00000] Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Example 2:
# Input: root = [3,9,20,15,7] Output: [3.00000,14.50000,11.00000]
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
#
# 中文:
# 给定一个非空二叉树的根节点
# root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7] 输出：[3.00000,14.50000,11.00000] 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。 因此返回 [3, 14.5, 11] 。
# 示例 2:
# 输入：root = [3,9,20,15,7] 输出：[3.00000,14.50000,11.00000]
# 提示：
# 树中节点数量在 [1, 104] 范围内
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """层次遍历"""

        ans = []
        level = [root]
        while level:
            next_level = []
            tmp = 0.0
            for i in level:
                tmp += i.val
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            ans.append(tmp/len(level))
            level = next_level
        return ans
