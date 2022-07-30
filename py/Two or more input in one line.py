# so to use two input variables in one line we use split function which will split both values in to two separate
# as we have used an integer value so we will use str function or use "" with variable
# , is used in split instead of space , but you may use space if feel ease.

name,age = input('Enter your Name and Age:').split(',')
print('Name: ' +name+  '\nAge:' + str(age))
