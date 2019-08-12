##孩子们的游戏(圆圈中最后剩下的数)
##问题描述：然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,
##并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友。
##解题思路：运用栈的知识。

##思路正确但是速度慢
def LastRemaining_Solution(n, m):
        # write code here
        if n == 0:
            return -1
        elif n == 1:
            return 0

        array = []
        for i in range(n):
            array.append(i)
        while n > 1:
            for i in range(m):
                if i == m - 1:
                    array.pop(0)
                    n -= 1
                else:
                    temp = array.pop(0)
                    array.append(temp)
        return array[0]

##每找出一个temp位置的数后，pop出去，下一个数在新数组中还是第temp个，但是数组长度减1
def LastRemaining_Solution(n, m):
        # write code here
        if n == 0:
            return -1
        elif n == 1:
            return 0

        array = []
        for i in range(n):
            array.append(i)
        temp = 0
        while n > 1:
            temp = (m - 1 + temp) % n
            array.pop(temp)
            n -= 1
            
        return array[0]

if __name__ == '__main__':
    result = LastRemaining_Solution(500, 90000)
    print('result: ', result)