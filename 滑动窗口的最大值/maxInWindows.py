##滑动窗口的最大值
##问题描述：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
##那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}。
##解题思路：从左往右遍历找出窗口的数组，在求最大值。

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        length = len(num)
        if length < size or size <= 0:
            return res
        for i in range(length - size + 1):
            temp = num[i : i + size]
            res.append(max(temp))
        return res