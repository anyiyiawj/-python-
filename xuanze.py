a=[7,8,0,6,5,1,3,4,2]
k=len(a)

for i in range(k-1):#排k-1次
    n=i
    for j in range(i,k):
        if a[n]>a[j]:
            n=j
    if i != n:
        a[i],a[n]=a[n],a[i]
    print(a)
print(a)


'''
简单选择排序
先找到最小的值放在第一位，交换，再选择从第二到最后一位，选择最小的放在第二位
方法是把i赋值给n，这样下面再比较的时候把j的值赋值给n就行，不用留住下表和值。最后比较i和n是否相等即可
'''
