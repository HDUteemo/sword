##二叉搜索树与双向链表
##问题描述：
##输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
##解题思路：
##二叉搜索树的中序遍历就是一个递增的序列，所以将根结点的left指向左子树的中序双向链表的尾部，左子树的中序双向链表的尾部的right指向根结点
##根结点的right指向右子树的中序双向链表的头部， 右子树的中序双向链表的头部指向根结点。
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        pHead = None
        pEnd = None
        pHead, pEnd = self.Head_End(pRootOfTree)

        return pHead

    def Head_End(self, pRootOfTree):
        pHead = None
        pEnd = None
        if pRootOfTree == None:
            return pHead, pEnd
        else:
            L_pHead, L_pEnd = self.Head_End(pRootOfTree.left)
            R_pHead, R_pEnd = self.Head_End(pRootOfTree.right)

        if L_pHead == None and L_pEnd == None:
            L_pHead = pRootOfTree
        if R_pHead == None and R_pEnd == None:
            R_pEnd = pRootOfTree

        pRootOfTree.left = L_pEnd
        if L_pEnd != None:
            L_pEnd.right = pRootOfTree
        pRootOfTree.right = R_pHead
        if R_pHead != None:
            R_pHead.left = pRootOfTree

        return L_pHead, R_pEnd