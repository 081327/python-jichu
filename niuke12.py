#格式化输出二
#牛牛、牛妹和牛可乐都是Nowcoder的用户，某天Nowcoder的管理员希望将他们的用户名以某种格式进行显示，
#现在给定他们三个当中的某一个名字name，请分别按全小写、全大写和首字母大写的方式对name进行格式化输出（注：每种格式独占一行）。

a=input('请输入第一个名字：')
b=input('请输入第二个名字：')
c=input('请输入第三个名字：')
print(a.lower(),b.upper(),c.title(),sep='\n')
#lower表示所有字母小写
#upper表示所有字母大写
#title表示各字符第一个字母大写

#将每个字符串以换行作为每个字符串之间的间隔，如下面代码所示:
#name = input()
#print(name.lower(),name.upper(),name.title(),sep='\n')

#同时打印多个的时候，每个字符串都会自动默认以空格作为每个字符串之间的间隔。
#print("abc", "uuu", "oop")