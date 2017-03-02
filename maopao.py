a=[7,8,0,6,5,1,3,4,2]
j=len(a)-1#注意次数
for k in range(j):
    flag=True
    for i in range(j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            flag=False
    print(a)
    if flag:
        break
print(a)

'''
780651342
706513428
从小到大
每次两两比较，把最大的数沉底，把最小的数一次一次向上
叫做交换排序法
做flag来减小排序所需要的次数
'''