def list_num(l):
    count = 0
    for i in l:
        if type(i) == list:
            count+=1
    return count

num = [1,2,3,4,[1,2,3],[3,4,5,6]]
print(list_num(num))