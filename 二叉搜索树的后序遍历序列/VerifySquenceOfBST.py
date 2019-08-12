##二叉搜索树的后序遍历序列##
##问题描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
##如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
##知识点：二叉搜索树（Binary Search Tree） 又名二叉排序树。它或者是一棵空树，
##或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于
##它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
##它的左、右子树也分别为二叉排序树。
##解题思路：
##后续遍历序列最后一个点是根结点，根据二叉搜索树的性质，在序列中可以找到一个位置i，i之前的序列是左子树，
##数值都比根结点数值小，i以及i之后的结点是右子树，数值都比根结点数值大。

def VerifySquenceOfBST(sequence):
	left_list = []
	right_list = []

	if len(sequence) != 0:
		root_node = sequence.pop()
	else:
		return False
	for i in range(len(sequence)):
		if sequence[i] < root_node:
			left_list.append(sequence[i])
		else:
			right_list = sequence[i:]
			break
	for j in range(len(right_list)):
		if right_list[j] < root_node:
			return False

	return Is_SequenceOfBst(left_list) and Is_SequenceOfBst(right_list)

def Is_SequenceOfBst(sequence):
    left_list = []
    right_list = []
    if len(sequence) != 0:
        root_node = sequence.pop()
    else:
        return True
    for i in range(len(sequence)):
        if sequence[i] < root_node:
            left_list.append(sequence[i])
        else:
            right_list = sequence[i:]
            break
    for j in range(len(right_list)):
        if right_list[j] < root_node:
            return False
    return Is_SequenceOfBst(left_list) and Is_SequenceOfBst(right_list)