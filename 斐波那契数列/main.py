# -*- coding:utf-8 -*-
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         if n == 1:
#             return 1
#         elif n < 1:
#             return 0
#         else:
#             return self.Fibonacci(n-1) + self.Fibonacci(n-2)
###时间比较长
########

class Solution:
    def Fibonacci(self, n):
        # write code here
        a0, a1 = 0, 1
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            for i in range(2, n+1):
                res = a0 + a1
                a0 = a1
                a1 = res
            return res



if __name__ == '__main__':
    s = Solution()
    result = s.Fibonacci(39)
    print('result: ', result)