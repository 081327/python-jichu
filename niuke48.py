#验证登录名与密码
name=input('请输入登录名：')
key=input('请输入登录密码：')
print('name','key',sep=' ')
if(name=='admis'and key=='Nowcoder666'):    #注意：里面的admis和Nowcoder666必须用单引号引上，一定要注意单引号的使用！
    print('Welcome!')
else:
   print('user id or password is not correct!')