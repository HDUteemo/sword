# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            count = 0
            n = -n 
            n = 2**32 - n
            X2b = bin(n)
            s = str(X2b)[2:]
            for i in range(len(s)):
                if int(s[i]) == 1:
                    count += 1
        else:
            count = 0
            X2b = bin(n)
            s = str(X2b)[2:]
            for i in range(len(s)):
                if int(s[i]) == 1:
                    count += 1
        return count
'''
    return sum([(n>>i & 1) for i in range(0,32)])
    计算机在计算的时候，所有数字都是以补码的形式在计算的。
'''
if __name__ == '__main__':
    s = Solution()
    num = s.NumberOf1(-1)
    print(num)