#列表长度
#输入一行多个字符串，字符串之间通过空格间隔。输出列表的长度。
names_str=input('请输入一串字符串：')
a=names_str.split()  #注意：names_str后面不要加(),直接接.
print('a')
print(len(a))