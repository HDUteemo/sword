##二叉树的镜像##
##问题描述:
##操作给定的二叉树，将其变换为源二叉树的镜像
##解题思路:
##递归的思想，若当前根结点非空，交换左右子结点，若为空 返回根结点。

##自己的版本，不够简洁
def Mirror(self, root):
    # write code here
    if root == None:
        return root
    else:
        pNode = root
        if self.change(pNode) == 1:
        	return root
            
def change(self, pNode):
    if pNode == None:
        return 1
    else:
        temp = pNode.left
        pNode.left = pNode.right
        pNode.right = temp
        return self.change(pNode.left) and self.change(pNode.right)


##简洁版本
def Mirror(self, root):
    # write code here
    if not root:
        return root
    if not root.right and not root.left:
        return root            
    if root.right or root.left:
        t=root.right
        root.right=root.left
        root.left=t
    self.Mirror(root.right)
    self.Mirror(root.left)
    return root
