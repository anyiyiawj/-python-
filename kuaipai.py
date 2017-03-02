a=[7,8,0,6,5,1,3,4,2]

def qsort(seq):
    if seq==[]:
        return []
    else:
        p=seq[0]
        l=qsort([x for x in seq[1:] if x<p])
        g=qsort([x for x in seq[1:] if x>=p])
    return l+[p]+g

print(qsort(a))
'''
快速排序
先那第一个，把小于第一个放到第一个序列，大于第二个放到第二个序列，然后把他们组装起来
每个都这样，知道所有的数被这样有计划的组织
'''