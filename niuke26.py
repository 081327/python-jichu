#牛牛的反转列表
num = [3, 5, 9, 0, 1, 9, 0, 3]
print(num)
num.sort(reverse=True)  #这里注意不能直接print(num.reverse()) 否则结果错误，需要单领出来！！
print(num)
