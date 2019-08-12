##扑克牌顺子
##问题描述：一副扑克牌，A看作1，J看作11。大小王为0，可以看作任意数字，判断从扑克牌抽出的牌能否组成顺子。
##解题思路：先排序，然后从小到大遍历，除了大小王，出现相同牌则直接判断不是顺子，如果前后两个数出现间隔，
##那么就看大小王所剩的数量是否足够弥补，够继续判断，不够直接判断不是顺子。

def IsContinuous(self, numbers):
    # write code here
    array = sorted(numbers)
    length = len(array)
    count = 0
        
    if length == 0:
        return False
    for i in range(length):
        if array[i] == 0:
            count += 1
        elif i != 0 and array[i - 1] != 0:
            if array[i] == array[i - 1]:
                return False
            elif array[i] == array[i - 1] + 1:
                continue
            else:
                count = count - (array[i] - array[i - 1] - 1)
                if count < 0:
                    return False
        return True