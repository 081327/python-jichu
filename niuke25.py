#有序的列表
list=['P','y','t','h','o','n']
print(sorted(list))   #sorted只是临时排序,原来的列表并不会改变
print(list)
list.sort(reverse=True)   #reverse别写错    #sort会改变原来的列表，同时题目要求降序就还需要reverse
print(list)