# -*- coding:utf-8 -*-

# <SUBID:319523304,UPDATE:20230205>
# English:
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].
# Example 1:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]] Output: [[1,0,0],[0,1,0],[1,1,1]] Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Constraints:
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.
#
# 中文:
# 给定一个
# n x n 的二进制矩阵 image ，先 水平 翻转图像，然后 反转 图像并返回 结果 。
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。
# 例如，水平翻转 [1,1,0] 的结果是 [0,1,1]。
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。
# 例如，反转 [0,1,1] 的结果是 [1,0,0]。
# 示例 1：
# 输入：image = [[1,1,0],[1,0,1],[0,0,0]] 输出：[[1,0,0],[0,1,0],[1,1,1]] 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]； 然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
# 示例 2：
# 输入：image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]； 然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 提示：
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] == 0 或 1.


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """暴力法"""

        image = [row[::-1] for row in image]

        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image

if __name__ == "__main__":
    d = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    s = Solution().flipAndInvertImage(d)
    print(s)
