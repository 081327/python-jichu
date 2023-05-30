#增加派对名单
#为庆祝驼瑞驰在牛爱网找到合适的对象，驼瑞驰通过输入的多个连续字符串创建了一个列表作为派对邀请名单，在检查的时候发现少了他最好的朋友“Allen”的名字，你能使用append函数将这个名字加到列表末尾吗？添加完成请输出完整列表。
list=input().split('')
list.insert(0,"Allen")
print('list')
#insert()方法语法：

#list.insert(index, obj)

#index — 对象 obj 需要插入的索引位置。

#obj — 要插入列表中的对象。