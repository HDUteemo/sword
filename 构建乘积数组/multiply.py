##构建乘积数组
##问题描述：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
##解题思路：用矩阵的知识，上下三角分开看。上三角从上往下看每一行乘积1，A0，A0*A1；下三角从下往上看每一行乘积1，A2, A2*A1；然后每一行对应乘积相乘就是最后结果 
##[1 , A1, A2
## A0, 1 , A2
## A0, A1, 1]

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        if length == 0:
            return None
        if length == 1:
            return A
        B = [1 for i in range(length)]
        for i in range(0, length-1):
            B[i + 1] = B[i] * A[i]
        temp = 1
        for j in range(length - 1, 0, -1):
            temp *= A[j]
            B[j - 1] *= temp
        
        return B