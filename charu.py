a=[7,8,0,6,5,1,3,4,2]
k=len(a)
for i in range(1,k):#要循环的书
    for j in range(i):#要比较的数
        if a[i]<a[j]:
            a.insert(j,a[i])#插入
            a.pop(i+1)#删去原来的数
            print(a)
            break

print(a)



'''
先把一个列表的数据，一个一个的排序
'''