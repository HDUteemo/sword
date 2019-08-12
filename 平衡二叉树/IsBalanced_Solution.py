##平衡二叉树
##问题描述:输入一棵二叉树，判断该二叉树是否是平衡二叉树。
##知识点：平衡二叉树,具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
##并且左右两个子树都是一棵平衡二叉树。
##思路描述：递归计算左右子树的深度，并进行比较

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        depth_left = self.TreeDepth(pRoot.left)
        depth_right = self.TreeDepth(pRoot.right)
        if abs(depth_left - depth_right) > 1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        
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