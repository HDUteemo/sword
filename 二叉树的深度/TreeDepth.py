##二叉树的深度
##问题描述:
##输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）
##形成树的一条路径，最长路径的长度为树的深度。
##解题思路:用递归的思想得出左右子树的最大深度，从而得到整个二叉树的最大深度。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        depth_temp = 0
        if pRoot == None:
            return 0
        else:
            temp_Root = pRoot
            depth = self.getDepth(temp_Root, depth_temp)
            return depth
        
    def getDepth(self, Root, length):
        depth_temp = length
        temp_Root = Root
        if Root == None:
            return depth_temp
        else:
            depth_temp += 1
            depth_left = self.getDepth(temp_Root.left, depth_temp)
            depth_right = self.getDepth(temp_Root.right, depth_temp)
            return max(depth_left, depth_right)