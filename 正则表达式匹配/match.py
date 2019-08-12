##正则表达式匹配
##问题描述：请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
##在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
##解题思路：递归。在pattern长度大于1的情况下，若第二个字符为'*'，应当考虑两种情况：1.len(s) > 0， 且pattern第一个字符和s第一个字符相等
##或者pattern第一个字符为'.'；2.其余情况。 如果pattern第二个字符不是'*'，或者只有长度1，那么就匹配s[0]和pattern[0],若匹配令s[1]与pattern[1]
##继续递归匹配。

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if (len(s) == 0 and len(pattern) == 0):
            return True
        if (len(s) > 0 and len(pattern) == 0):
            return False
        if (len(pattern) > 1 and pattern[1] == '*'):
            if (len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.')):
                return (self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern))#'*'之前的字符次数0或者大于0，在大于0的情况下pattern可以形式不变，也可以去掉前两个字符
            else:
                return self.match(s, pattern[2:])
        else:
            if (len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0])):
                return self.match(s[1:], pattern[1:])
        return False