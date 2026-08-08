def largest(lis):
    lar=lis[0]
    n=len(lis)
    for i in range(1,n):
        if lar < lis[i]:
            lar=lis[i]
    return lar
print(largest([2,3,4,5,6,9,8,7,4,1,2,55]))    