from gettext import find


name = input('Enter Your name:')
age = int(input('enter your age:'))
if age>=10 and (name[0]=='a' or name[0]==['A']):
    print('you can wacth movie.')
else: 
    print('you can not watch movie.')