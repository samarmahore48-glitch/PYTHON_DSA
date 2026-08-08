def zeroatend(lis):
    j=0
    for i in range(len(lis)):
        if lis[i]!=0:
            lis[i],lis[j]=lis[j],lis[i]
            j+=1
    return lis
        
print(zeroatend([1,2,0,1,2,0,3,6,5,0,0,4,0,5,8]))
