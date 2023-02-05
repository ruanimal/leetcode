# -*- coding:utf-8 -*-

# <SUBID:283292138,UPDATE:20230205>
# English:
# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.
# Example 1:
# Input: nums = [3,2,1,6,0,5] Output: [6,3,5,null,2,0,null,null,1] Explanation: The recursive calls are as follow: - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5]. - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1]. - Empty array, so no child. - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1]. - Empty array, so no child. - Only one element, so child is a node with value 1. - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is []. - Only one element, so child is a node with value 0. - Empty array, so no child.
# Example 2:
# Input: nums = [3,2,1] Output: [3,null,2,null,1]
# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.
#
# 中文:
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
# 返回 nums 构建的 最大二叉树 。
# 示例 1：
# 输入：nums = [3,2,1,6,0,5] 输出：[6,3,5,null,2,0,null,null,1] 解释：递归调用如下所示： - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。 - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。 - 空数组，无子节点。 - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。 - 空数组，无子节点。 - 只有一个元素，所以子节点是一个值为 1 的节点。 - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。 - 只有一个元素，所以子节点是一个值为 0 的节点。 - 空数组，无子节点。
# 示例 2：
# 输入：nums = [3,2,1] 输出：[3,null,2,null,1]
# 提示：
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# nums 中的所有整数 互不相同


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Solution_A:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        简单递归, 内存复制过多
        """

        if len(nums) == 0:
            return

        maxid = max((elem, idx) for (idx, elem) in enumerate(nums))[1]
        root = TreeNode(nums[maxid])
        root.left = self.constructMaximumBinaryTree(nums[:maxid])
        root.right = self.constructMaximumBinaryTree(nums[maxid+1:])
        return root

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        简单递归, 传递下标防止复制
        注意边界, 防止无法终止
        """

        if len(nums) == 0:
            return
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums: List[int], i: int, j: int) -> TreeNode:
        if (j-i) < 0:
            return
        maxid = self.get_maxid(nums, i, j)
        root = TreeNode(nums[maxid])
        root.left = self.helper(nums, i, maxid-1)
        root.right = self.helper(nums, maxid+1, j)
        return root

    @staticmethod
    def get_maxid(nums: List[int], i: int, j: int) -> int:
        assert len(nums) > 0
        idx = i
        for x in range(i+1, j+1):
            if nums[x] > nums[idx]:
                idx = x
        return idx



if LOCAL_TEST:
    s = Solution()
    print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))
    print(s.get_maxid([3,2,1,6,0,5], 0, 5))
