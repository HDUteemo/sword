'''
举个列子，如果number = 6时，4跳2, 5跳1 存在这两种情况， 所以f(6) = f(5) + f(4)
斐波那契数列。
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        if (number <= 0):
            return 0
        if (number == 1):
            return 1
        if (number == 2):
            return 2
        first = 1
        second = 2
        third = 0
        for i in range(3, number+1):
            third = first + second
            first = second
            second = third

        return third


