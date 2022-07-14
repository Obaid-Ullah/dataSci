# Exercise= ticket booking
age= int(input('Enter Your age:'))
if age==0 or age<=0:
    print('Your can not watch.')
elif 0<age<3:
    print('Ticket: Free')
elif 3<age<=10:
    print('Ticket : 150')
elif 11<age<=60:
    print('Ticket:250')
else:
    print('Ticket: 500')