#格式化输出
#牛牛、牛妹和牛可乐正在Nowcoder学习Python语言，现在给定他们三个当中的某一个名字name，
#假设输入的name为Niuniu，则输出 I am Niuniu and I am studying Python in Nowcoder!
#请按以上句式输出相应的英文句子。

#f {}-字符串形式
name=input()
print(f' I am {name} and I am studying Python in Nowcoder!')

#format格式化
name=input()
print( 'I am {name} and I am studying Python in Nowcoder!'.format(name))

#%格式化
name=input()
print( 'I am %s and I am studying Python in Nowcoder!'%name)