##按之字形顺序打印二叉树
##问题描述：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
##第三行按照从左到右的顺序打印，其他行以此类推。
##解题思路：
##注意从左往右是先左子结点再右子结点，从右往左相反。

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
        direction = 'left'
        list_node = [pRoot]
        while len(list_node) != 0:
            list_node, val, direction = self.Print_row(list_node, direction)
            if len(list_node) != 0:
                res.append(val[::-1])
        return res
    def Print_row(self, list_node, direction):
        length = len(list_node)
        res = []
        res_val = []
        for i in range(length, 0, -1):
            if direction == 'left':
                if list_node[i - 1].left != None:
                    res.append(list_node[i - 1].left)
                    res_val.append(list_node[i - 1].left.val)
                if list_node[i - 1].right != None:
                    res.append(list_node[i - 1].right)
                    res_val.append(list_node[i - 1].right.val)
            if direction == 'right':
                if list_node[i - 1].right != None:
                    res.append(list_node[i - 1].right)
                    res_val.append(list_node[i - 1].right.val)
                if list_node[i - 1].left != None:
                    res.append(list_node[i - 1].left)
                    res_val.append(list_node[i - 1].left.val)
        if direction == 'left':
            new_direction = 'right'
        else:
            new_direction = 'left'
        
        return res, res_val, new_direction