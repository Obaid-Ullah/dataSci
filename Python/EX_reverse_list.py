def rev_list(l):
    rev =[]
    for i in range(len(l)):
        poped = l.pop()
        rev.append(poped)
        
    return rev

num = [1,2,3,4]
print(rev_list(num))