##二叉树中和为某一值的路径##
##问题描述：输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数
##的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
##(注意: 在返回值的list中，数组长度大的数组靠前)
##利用递归的思想，只有和等于expectNumber才会返回非空列表，然后上一层递归拼接返回的列表。
##注意：这里的方法没有把数组长度大的数组靠前

def FindPath(self, root, expectNumber):
	if not root:
        return []
    if root and not root.left and not root.right and root.val == expectNumber:
        return [[root.val]]
    res = []
    left = self.FindPath(root.left, expectNumber - root.val)
    right = self.FindPath(root.right, expectNumber - root.val)
    for i in left + right:
        res.append([root.val] + i)
    return res
