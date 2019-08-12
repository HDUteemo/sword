##序列化二叉树
##问题描述：请实现两个函数，分别用来序列化和反序列化二叉树
##解题思路：
##1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
##不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
##2. 反序列化：之前序列化是先序遍历，反序列化以先序遍历的顺序重新生成树，
##引入flag来遍历所有数值，且flag增加的顺序符合先序遍历。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.flag = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
     
    def Deserialize(self, s):
        # write code here
        self.flag += 1
         
        l = s.split(',')
        if self.flag >= len(s):
            return None
         
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root