# In previous lectures we came to know that input function will give us output as a string.
# So to it is not good to use input with integer values as it will produce error.
# So we will use int function to overcome this issue
# Also keep in mind interger and float values could be added but output will be in floating point.

# numone = input('Enter fisrt number:')
# numTwo= input('Enter Second number:')
# total = numone + numTwo
# print('total= ' + total) #output:55 as it took numone and numtwo as a string values so what we have to do now 
#                          #is to use input function

numone = int(input('Enter fisrt number:'))
numTwo= int(input('Enter Second number:'))
total = numone + numTwo      # at this point total is a number
print('Total:' + str(total)) 
# but we know that we can't add a string into a number so we will use string function to change total data type from
#number to string and we will get accurate output
