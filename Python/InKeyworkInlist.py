# mostly it is used to check wether we have an element in our list or not. so lets have a look
from turtle import pensize


mix= [1,2,3,4,5,6,7,8,9]
if 10 in mix:
    print('present')
else:
    mix[-1]= 'O'
print(mix)
print(mix[-1])



 