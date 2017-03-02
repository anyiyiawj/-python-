'''
先把list分解成短的，然后一个一个的拼成大的

'''

def bing(seq1,seq2):#合并
    l=len(seq1)+len(seq2)
    k=len(seq2)
    j=0
    for i in range(l):
        if seq1[i]>seq2[j]:
            seq1.insert(i,seq2[j])
            i=i+1
            j=j+1
        else:
            i+1
        print(seq1)
        if j>=k:
            break
    return seq1
a=[2,3,4,5,6,10]
b=[1,3,7,8]
print(bing(a,b))

def fen(seq):
    if len(seq)%2==1:
        l=(len(seq)-1)//2
        a=seq[:l]
        b=seq[l+1:]
        if l==1:
            return a,b
    else:
        l=len(seq)//2
        print(l)
        a=seq[:l]
        b = seq[l+1:]
        if l==1:
            return a,b
    return fen(a),fen(b)
c=fen(a)
print(c)


