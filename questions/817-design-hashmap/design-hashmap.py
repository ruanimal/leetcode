# -*- coding:utf-8 -*-

# <SUBID:319274089,UPDATE:20230205>
# English:
# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# Example 1:
# Input ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"] [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]] Output [null, null, null, 1, -1, null, 1, null, -1] Explanation MyHashMap myHashMap = new MyHashMap(); myHashMap.put(1, 1); // The map is now [[1,1]] myHashMap.put(2, 2); // The map is now [[1,1], [2,2]] myHashMap.get(1); // return 1, The map is now [[1,1], [2,2]] myHashMap.get(3); // return -1 (i.e., not found), The map is now [[1,1], [2,2]] myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value) myHashMap.get(2); // return 1, The map is now [[1,1], [2,1]] myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]] myHashMap.get(2); // return -1 (i.e., not found), The map is now [[1,1]]
# Constraints:
# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.
#
# 中文:
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
# 示例：
# 输入： ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"] [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]] 输出： [null, null, null, 1, -1, null, 1, null, -1] 解释： MyHashMap myHashMap = new MyHashMap(); myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]] myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]] myHashMap.get(1); // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]] myHashMap.get(3); // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]] myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值） myHashMap.get(2); // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]] myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]] myHashMap.get(2); // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
# 提示：
# 0 <= key, value <= 106
# 最多调用 104 次 put、get 和 remove 方法


class MyHashMap:

    def __init__(self):
        self.data = [None] * 10001


    def put(self, key: int, value: int) -> None:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            self.data[hash_key] = (key, value)
        elif isinstance(pair, tuple):
            if pair[0] == key:
                self.data[hash_key] = (key, value)
            else:
                self.data[hash_key] = [pair, (key, value)]
        else:
            for i in range(len(pair)):
                if pair[i][0] == key:
                    pair[i] = (key, value)
                    return
            pair.append((key, value))

    def get(self, key: int) -> int:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return -1
        elif isinstance(pair, tuple):
            if pair[0] == key:
                return pair[1]
        else:
            for i in pair:
                if i[0] == key:
                    return i[1]
        return -1


    def remove(self, key: int) -> None:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return
        elif isinstance(pair, tuple):
            if pair[0] == key:
                self.data[hash_key] = None
        else:
            for i in range(len(pair)):
                if pair[i][0] == key:
                    del pair[i]
                    return
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
