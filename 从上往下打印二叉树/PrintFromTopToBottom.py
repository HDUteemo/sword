##从上往下打印二叉树##
##问题描述：
##从上往下打印出二叉树的每个节点，同层节点从左至右打印。
##解题思路：
##p_node存储当前层的结点，t_node存储下一层的结点。
def PrintFromTopToBottom(root):
	val_node = []
	p_node = []
	t_node = []
	if root:
		p_node.append(root)
		val_node.append(root.val)
	while len(p_node) > 0:
		t_node = []
		for i in range(len(p_node)):
			if p_node[i].left != None:
				t_node.append(p_node[i].left)
				val_node.append(p_node[i].left.val)
			if p_node[i].right != None:
				t_node.append(p_node[i].right)
				val_node.append(p_node[i].right.val)
		p_node = t_node
	return val_node



##最佳思路：用arraylist模拟一个队列来存储相应的TreeNode
def PrintFromTopToBottom(self, root):
    # write code here
    l=[]
    if not root:
        return []
    q=[root]
    while len(q):
    	t=q.pop(0)
        l.append(t.val)
        if t.left:
            q.append(t.left)
        if t.right:
            q.append(t.right)
    return l  