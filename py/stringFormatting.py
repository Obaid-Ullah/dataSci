#in previous programs we have formatted our string such as mentioned below
# print('Name: ' +name+  '\nAge:' + str(age))
#but now we will use format function to format our string

name,age = input('Enter your Name and Age:').split(',')
#print('Name: ' +name+  '\nAge:' + str(age)) old formatting style
# python 3.6: print(f'Name: {name} \n Age:{age}') 
print('Name: {} \nAge:{}'.format(name,age))
