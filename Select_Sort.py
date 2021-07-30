def select_sort(li):
    for i in range(len(li)-1):
        v = i
        for j in range(i+1,len(li)):
            if li(j)<li(i):
                v = j
        li[i],li[v] = li[v],li[i]
