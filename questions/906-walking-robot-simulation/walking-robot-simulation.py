# -*- coding:utf-8 -*-


# English:
# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
# Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
# Note:
# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.
# Example 1:
# Input: commands = [4,-1,3], obstacles = [] Output: 25 Explanation: The robot starts at (0, 0): 1. Move north 4 units to (0, 4). 2. Turn right. 3. Move east 3 units to (3, 4). The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.
# Example 2:
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]] Output: 65 Explanation: The robot starts at (0, 0): 1. Move north 4 units to (0, 4). 2. Turn right. 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4). 4. Turn left. 5. Move north 4 units to (1, 8). The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
# Example 3:
# Input: commands = [6,-1,-1,6], obstacles = [] Output: 36 Explanation: The robot starts at (0, 0): 1. Move north 6 units to (0, 6). 2. Turn right. 3. Turn right. 4. Move south 6 units to (0, 0). The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.
# Constraints:
# 1 <= commands.length <= 104
# commands[i] is either -2, -1, or an integer in the range [1, 9].
# 0 <= obstacles.length <= 104
# -3 * 104 <= xi, yi <= 3 * 104
# The answer is guaranteed to be less than 231.
#
# 中文:
# 机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：
# -2 ：向左转 90 度
# -1 ：向右转 90 度
# 1 <= x <= 9 ：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）
# 注意：
# 北表示 +Y 方向。
# 东表示 +X 方向。
# 南表示 -Y 方向。
# 西表示 -X 方向。
# 示例 1：
# 输入：commands = [4,-1,3], obstacles = [] 输出：25 解释： 机器人开始位于 (0, 0)： 1. 向北移动 4 个单位，到达 (0, 4) 2. 右转 3. 向东移动 3 个单位，到达 (3, 4) 距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25
# 示例 2：
# 输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]] 输出：65 解释：机器人开始位于 (0, 0)： 1. 向北移动 4 个单位，到达 (0, 4) 2. 右转 3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4) 4. 左转 5. 向北走 4 个单位，到达 (1, 8) 距离原点最远的是 (1, 8) ，距离为 12 + 82 = 65
# 提示：
# 1 <= commands.length <= 104
# commands[i] is one of the values in the list [-2,-1,1,2,3,4,5,6,7,8,9].
# 0 <= obstacles.length <= 104
# -3 * 104 <= xi, yi <= 3 * 104
# 答案保证小于 231


#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#
# https://leetcode-cn.com/problems/walking-robot-simulation/description/
#
# algorithms
# Easy (27.95%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 8.5K
# Testcase Example:  '[4,-1,3]\n[]'
#
# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
#
#
# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
#
#
# 在网格上有一些格子被视为障碍物。
#
# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
#
# 如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
#
# 返回从原点到机器人的最大欧式距离的平方。
#
#
#
# 示例 1：
#
# 输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#
#
# 示例 2：
#
# 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#
#
#
#
# 提示：
#
#
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# 答案保证小于 2 ^ 31
#
#
#
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        def check_turn(head, c):
            heads = [
                (0, 1),   # 朝向x, 正方向
                (1, 1),   # 朝向y, 正方向
                (0, -1),
                (1, -1),
            ]
            if c == -2:  # 左转
                next_head = (heads.index(head)+1) % 4
                return heads[next_head]
            elif c == -1:
                next_head = (heads.index(head)-1) % 4
                return heads[next_head]
            else:
                return

        marks = [set(), set()]
        obstacles_set = set()
        for x, y in obstacles:
            marks[0].add(y)
            marks[1].add(x)
            obstacles_set.add((x, y))

        head = (1, 1)  # 朝向
        pos = [0, 0]   # 当前位置
        ans = 0
        for i in commands:
            next_head = check_turn(head, i)
            if next_head:
                head = next_head
                continue

            if pos[head[0] ^ 1] not in marks[head[0]]:
                pos[head[0]] += head[1] * i
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
                continue

            for _ in range(i):
                pos[head[0]] += head[1] * 1
                if tuple(pos) in obstacles_set:
                    pos[head[0]] -= head[1] * 1
                    break
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans

if __name__ == "__main__":
    s = Solution().robotSim(commands = [4,-1,3], obstacles = [])
    print(s)
    s = Solution().robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]])
    print(s)
    # s = Solution().robotSim(commands = [4,-1,4,-1,4,-2,4,-2], obstacles = [])
    s = Solution().robotSim([1,2,-2,5,-1,-2,-1,8,3,-1,9,4,-2,3,2,4,3,9,2,-1,-1,-2,1,3,-2,4,1,4,-1,1,9,-1,-2,5,-1,5,5,-2,6,6,7,7,2,8,9,-1,7,4,6,9,9,9,-1,5,1,3,3,-1,5,9,7,4,8,-1,-2,1,3,2,9,3,-1,-2,8,8,7,5,-2,6,8,4,6,2,7,2,-1,7,-2,3,3,2,-2,6,9,8,1,-2,-1,1,4,7], [[-57,-58],[-72,91],[-55,35],[-20,29],[51,70],[-61,88],[-62,99],[52,17],[-75,-32],[91,-22],[54,33],[-45,-59],[47,-48],[53,-98],[-91,83],[81,12],[-34,-90],[-79,-82],[-15,-86],[-24,66],[-35,35],[3,31],[87,93],[2,-19],[87,-93],[24,-10],[84,-53],[86,87],[-88,-18],[-51,89],[96,66],[-77,-94],[-39,-1],[89,51],[-23,-72],[27,24],[53,-80],[52,-33],[32,4],[78,-55],[-25,18],[-23,47],[79,-5],[-23,-22],[14,-25],[-11,69],[63,36],[35,-99],[-24,82],[-29,-98],[-50,-70],[72,95],[80,80],[-68,-40],[65,70],[-92,78],[-45,-63],[1,34],[81,50],[14,91],[-77,-54],[13,-88],[24,37],[-12,59],[-48,-62],[57,-22],[-8,85],[48,71],[12,1],[-20,36],[-32,-14],[39,46],[-41,75],[13,-23],[98,10],[-88,64],[50,37],[-95,-32],[46,-91],[10,79],[-11,43],[-94,98],[79,42],[51,71],[4,-30],[2,74],[4,10],[61,98],[57,98],[46,43],[-16,72],[53,-69],[54,-96],[22,0],[-7,92],[-69,80],[68,-73],[-24,-92],[-21,82],[32,-1],[-6,16],[15,-29],[70,-66],[-85,80],[50,-3],[6,13],[-30,-98],[-30,59],[-67,40],[17,72],[79,82],[89,-100],[2,79],[-95,-46],[17,68],[-46,81],[-5,-57],[7,58],[-42,68],[19,-95],[-17,-76],[81,-86],[79,78],[-82,-67],[6,0],[35,-16],[98,83],[-81,100],[-11,46],[-21,-38],[-30,-41],[86,18],[-68,6],[80,75],[-96,-44],[-19,66],[21,84],[-56,-64],[39,-15],[0,45],[-81,-54],[-66,-93],[-4,2],[-42,-67],[-15,-33],[1,-32],[-74,-24],[7,18],[-62,84],[19,61],[39,79],[60,-98],[-76,45],[58,-98],[33,26],[-74,-95],[22,30],[-68,-62],[-59,4],[-62,35],[-78,80],[-82,54],[-42,81],[56,-15],[32,-19],[34,93],[57,-100],[-1,-87],[68,-26],[18,86],[-55,-19],[-68,-99],[-9,47],[24,94],[92,97],[5,67],[97,-71],[63,-57],[-52,-14],[-86,-78],[-17,92],[-61,-83],[-84,-10],[20,13],[-68,-47],[7,28],[66,89],[-41,-17],[-14,-46],[-72,-91],[4,52],[-17,-59],[-85,-46],[-94,-23],[-48,-3],[-64,-37],[2,26],[76,88],[-8,-46],[-19,-68]])
    print(s)


