##翻转单词顺序列
##问题描述：例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。

def ReverseSentence(self, s):
    # write code here
    length = len(s)
    result = ''
    temp = ''
        
    for i in range(length):
        if s[i] != ' ' and i != length - 1:
            temp += s[i]
        elif i == length - 1:
            temp += s[i]
            temp += ' '
            result = temp + result
            temp = ''
        else:
            temp += s[i]
            result = temp + result
            temp = ''
        
    return result[0: length]