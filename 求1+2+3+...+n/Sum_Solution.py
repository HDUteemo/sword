##求1+2+3+...+n
##问题描述：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
##解题思路：1.使用递归； 2. 1+2+3+...+n = n*(n + 1)/2 = (n**2 + n)>>1.

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return (n**2 + n)>>1