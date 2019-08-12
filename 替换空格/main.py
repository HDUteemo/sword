# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = len(s)
        a = ''
        for i in range(l):
            if s[i] == ' ':
                a += '%20'
            else:
                a += s[i]
        return a
        # a = s.replace(' ', '%20')
        # return a


if __name__ == '__main__':
    s = Solution()
    strings = 'We Are Happy'
    a = s.replaceSpace(strings)
    print('s: ', a)
