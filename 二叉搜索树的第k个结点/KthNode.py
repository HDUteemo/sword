##二叉搜索树的第k个结点
##问题描述：给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    
##中，按结点数值大小顺序第三小结点的值为4。
##解题思路：二叉搜索树左子树所有值小于根结点值，根结点值小于右子树结点值。中序遍历结点的值是从小到大排序的。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        res = self.SeqNode(pRoot)
        if k > len(res) or k <= 0:
            return None
        else:
            return res[k-1]
    
    def SeqNode(self, pRoot):
        if not pRoot:
            return None
        res = [pRoot]
        
        left_Node = self.SeqNode(pRoot.left)
        right_Node = self.SeqNode(pRoot.right)
        
        if left_Node != None:
            res = left_Node + res
        if right_Node != None:
            res = res + right_Node
        
        return res