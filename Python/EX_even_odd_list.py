def e_o(l):
    even=[]
    odd=[]
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output= [even,odd]
    return output

num =[1,2,3,4,5,6,7,8,9,10]
print(e_o(num))
