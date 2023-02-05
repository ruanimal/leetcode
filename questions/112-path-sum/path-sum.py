# -*- coding:utf-8 -*-

# <SUBID:308758433,UPDATE:20230205>
# English:
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 Output: true Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:
# Input: root = [1,2,3], targetSum = 5 Output: false Explanation: There two root-to-leaf paths in the tree: (1 --> 2): The sum is 3. (1 --> 3): The sum is 4. There is no root-to-leaf path with sum = 5.
# Example 3:
# Input: root = [], targetSum = 0 Output: false Explanation: Since the tree is empty, there are no root-to-leaf paths.
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
# 中文:
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 输出：true 解释：等于目标和的根节点到叶节点路径如上图所示。
# 示例 2：
# 输入：root = [1,2,3], targetSum = 5 输出：false 解释：树中存在两条根节点到叶子节点的路径： (1 --> 2): 和为 3 (1 --> 3): 和为 4 不存在 sum = 5 的根节点到叶子节点的路径。
# 示例 3：
# 输入：root = [], targetSum = 0 输出：false 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
# 提示：
# 树中节点的数目在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000



class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        后序位置判断
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True if targetSum == root.val else False
        elif root.left and root.right:
            return self.hasPathSum(root.left, targetSum-root.val) \
                or self.hasPathSum(root.right, targetSum-root.val)
        elif root.left:
            return self.hasPathSum(root.left, targetSum-root.val)
        else:
            return self.hasPathSum(root.right, targetSum-root.val)

    # def helper(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:  # 排除根节点为空的情况
    #         return True if targetSum == 0 else False
    #     return self.helper(root.left, targetSum-root.val) \
    #         or self.helper(root.right, targetSum-root.val)
