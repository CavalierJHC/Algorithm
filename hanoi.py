def hanoi(n,a,b,c):
    if n >0 :
        hanoi(n-1,a,c,b)
        print("moving %s to %s" % (a,c))
        hanoi(n-1,b,a,c)
        
hanoi(4,"a","b","c")