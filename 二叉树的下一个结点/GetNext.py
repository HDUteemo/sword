##二叉树的下一个结点
##问题描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
##解题思路：1.先判断该结点是否为None;2.再判断是否有右子结点，找右子树的中序遍历第一个结点；
##3.若没有右子节点，则判断该结点是否为父结点的左子结点，若是则父节点为下一个结点，若不是继续向上找，直到某结点为其父节点的左子节点为止。

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        temp = pNode.right
        while temp:
            left_node = temp.left
            if left_node == None:
                return temp
            temp = left_node
        if temp == None:
            father = pNode.next
            temp = pNode
            while father != None and father.left != temp:
                temp = father
                father = father.next
            return father
