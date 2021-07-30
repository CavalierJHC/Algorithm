def linear_search(li,val):
    for ind , v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

def linear_search(li,val):
    for i in range(len(li)):
        if li[i] == val:
            return i
    else:
        return None
