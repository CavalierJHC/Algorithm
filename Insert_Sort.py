def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while li[i]<li[j] and j>=0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp