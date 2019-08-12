##左旋转字符串
##问题描述：对于一个给定的字符序列S，请你把其循环左移K位后的序列输出
##解题思路：对于S，将左移超出最大位部分记为s1，其余为s2；最终结果为result = s2 + s1

def LeftRotateString(self, s, n):
        # write code here
        if n == 0:
            return s
        s1 = s[0:n]
        s2 = s[n: ]
        result = s2 + s1
        return result