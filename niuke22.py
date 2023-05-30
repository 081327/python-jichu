#删除简历
#牛牛在各大互联网公司投入了简历，公司的名字通过字符串的形式在一行中输入，请用列表记录。现在牛牛已经确定了第一所公司的HR表露了不录用他的态度，请你使用del函数帮助牛牛从列表中删除第一个元素，然后输出列表。
list=input().split('')
list.remove(list[0])
print(list)


#法一：pop（pop后跟下标值）
#s = input().split()
#s.pop(0)#删除s列表中下标为0的元素
#print(com)

#法二：remove（remove后跟元素值）
#com = input().split()
#com.remove(com[0])
#print(com)
