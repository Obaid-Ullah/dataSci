# --------------Even Odd----------
# def odd_even(num):
#     if num%2==0:
#         return "even"
#     return 'odd'

# print(odd_even(5))
# ---------------Even_odd---------
# num = int(input('Enter a Num:'))
# def is_even(num):
#     return num%2==0
# print(is_even(num))

# --------------greater num from 2
# def greater_num(a,b):
#     if a>b:
#         return a
#     else: 
#         return b
# answer in true or false

# ---------Function inside a function
def greater_num(a,b):
    if a>b:
        return a
    else: 
        return b

def new_greatest(a,b,c):
    return greater_num(greater_num(a,b),c)

num1 = int(input('Enter  Num1:'))
num2 = int(input('Eneter Num2:'))
num3 = int(input('Eneter Num3:'))
print(new_greatest(num1,num2,num3))

# ------------Greater from 2-numbers
# num1 = int(input('Enter  Num1:'))
# num2 = int(input('Eneter Num2:'))
# greater = greater_num(num1,num2)
# print(greater)

# --------------greater num from 3-numbers
# def greater_num(a,b,c):
#     if a>b:
#         return a
#     elif b>c: 
#         return b
#     else:
#         return c
# num1 = int(input('Enter  Num1:'))
# num2 = int(input('Eneter Num2:'))
# num3 = int(input('Eneter Num3:'))
# greater = greater_num(num1,num2,num3)
# print(greater)
