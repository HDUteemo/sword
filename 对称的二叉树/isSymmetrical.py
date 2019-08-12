##对称的二叉树
##问题描述：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
##解题思路：递归思想，根结点的左右子树各镜像结点的值进行比较。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left_node = pRoot.left
        right_node = pRoot.right
        result = self.check_val(left_node, right_node)
        
        return result
    
    def check_val(self, left_node, right_node):
        if left_node == None and right_node == None:
            return True
        elif left_node != None and right_node != None:
            if left_node.val == right_node.val:
                return self.check_val(left_node.left, right_node.right) and self.check_val(left_node.right, right_node.left)
            else:
                return False
        else:
            return False