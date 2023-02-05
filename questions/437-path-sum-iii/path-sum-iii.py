# -*- coding:utf-8 -*-

# <SUBID:315052818,UPDATE:20230205>
# English:
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 Output: 3 Explanation: The paths that sum to 8 are shown.
# Example 2:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 Output: 3
# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000
#
# 中文:
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 示例 1：
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 输出：3 解释：和等于 8 的路径有 3 条，如图所示。
# 示例 2：
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 输出：3
# 提示:
# 二叉树的节点个数的范围是 [0,1000]
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000



class SolutionA(object):
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """暴力法
        """
        if not root:
            return 0
        return self.helper(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def helper(self, root: TreeNode, sum: int) -> int:
        """求以当前节点为起点的路径数目
        """

        if not root:
            return 0
        ans = 0
        if sum == root.val:
            ans += 1
        # print(root.val, ans)
        ans += self.helper(root.left, sum-root.val)
        ans += self.helper(root.right, sum-root.val)
        return ans

class Solution(object):
    def pathSum(self, root, sum):
        """动态规划思想, 前缀和"""

        from collections import defaultdict
        lookup = defaultdict(int)
        lookup[0] = 1
        self.res = 0

        def helper(root,curSum):
            if not root:
                return
            curSum += root.val
            self.res += lookup[curSum - sum]
            lookup[curSum] += 1
            helper(root.left,curSum)
            helper(root.right,curSum)
            lookup[curSum] -= 1
        helper(root,0)
        return self.res

