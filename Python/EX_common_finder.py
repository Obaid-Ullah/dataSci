def common(l1,l2):
    outPut =[]
    for i in l1:
        if i in l2:
            outPut.append(i)
    return outPut

num1=[1,2,3,4,5,6]
num2=[2,3,4,7,8,9]
print(common(num1,num2))
