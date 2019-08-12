##机器人的运动范文
##问题描述：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
##但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
##但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
##解题思路：创建一个m行n列形式列表，初始化0。机器人的移动的条件，位置上的值为0且坐标数位和小于等于阈值。用递归遍历所有情况
##且每找到一个符合情况的位置，标志位都会加1，且位置上的值等于1。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
        self.map = []
    def movingCount(self, threshold, rows, cols):
        self.map =[[0 for i in range(cols)] for j in range(rows)]
        self.find_next(threshold, rows, cols, 0, 0)
        
        return self.count
    
    def find_next(self, threshold, rows, cols, i, j):
        temp = 0
        temp_i = i
        temp_j = j
        while temp_i > 0:
            temp += temp_i % 10
            temp_i = temp_i // 10
        while temp_j > 0:
            temp += temp_j % 10
            temp_j = temp_j // 10
        if temp <= threshold:
            self.map[i][j] = 1
            self.count += 1
        else:
            return None
        if i + 1 < rows and self.map[i+1][j] == 0:
            self.find_next(threshold, rows, cols, i + 1, j)
        if i - 1 >= 0 and self.map[i-1][j] == 0:
            self.find_next(threshold, rows, cols, i - 1, j)
        if j + 1 < cols and self.map[i][j+1] == 0:
            self.find_next(threshold, rows, cols, i, j + 1)
        if j - 1 >= 0 and self.map[i][j-1] == 0:
            self.find_next(threshold, rows, cols, i, j - 1)