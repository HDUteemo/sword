##把二叉树打印成多行
##问题描述：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
##解题思路：
##从上至下，从左往右遍历即可。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        res = [[pRoot.val]]
        list_node = [pRoot]
        while len(list_node) != 0:
            list_node, val = self.Print_row(list_node)
            if len(list_node) != 0:
                res.append(val[:])
        return res
    def Print_row(self, list_node):
        length = len(list_node)
        res = []
        res_val = []
        for i in range(0, length):
            if list_node[i].left != None:
                res.append(list_node[i].left)
                res_val.append(list_node[i].left.val)
            if list_node[i].right != None:
                res.append(list_node[i].right)
                res_val.append(list_node[i].right.val)
        
        return res, res_val