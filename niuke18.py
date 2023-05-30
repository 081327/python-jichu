#生成数字列表
#牛牛在牛客网系统录入了一连串数字，数字之间依靠逗号隔开，你能帮助他将这些数字存储在列表中吗，列表元素以int的形式。
#利用空列表填入法

names_str=input('请输入一串数字：')  #获取输入的字符串
names_list=names_str.split()       #将字符串转换成列表，split是以空格形式分割成列表形式
names_new_list=[int(s) for s in names_list ]  #搞成列表形式，记得加[]
print(names_new_list)  #输出列表
#下面输入数字以空格进行输入数字