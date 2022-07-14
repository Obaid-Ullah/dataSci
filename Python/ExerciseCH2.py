#Exercise: print average of three variables using 
#                   Method-1
# numone = int(input('Enter fisrt number:'))
# numTwo = int(input('Enter Second number:'))
# numThree= int(input('Enter Third number:'))
# #Average = (numone + numTwo + numThree)/3     # at this point total is a number
# print('NumOne: {}, NumTwo: {},NumThree: {} and their average is {}'.format(numone,numTwo,numThree, (numone + numTwo + numThree)/3)) 
#                   Method-2
numone ,numTwo, numThree = input('Enter fisrt number:').split(',')
#Average = (numone + numTwo + numThree)/3     # at this point total is a number
print('NumOne: {}, NumTwo: {},NumThree: {} and their average is {}'.format(numone,numTwo,numThree,(int(numone)+int(numTwo)+int(numThree))/3)) 
