user = {
    'name': 'Obaid',
    'age' : 26,
    'Degree':'MSSE'
}

# print(user)
# print(user['age'])

# user1={}
# user1['name']='Obaid'
# user1['class']='MS'
# print(user1['class'])

def cubefinder(i):
    cube={}
    for i in range(1,i+1):
        cube[i]=i**3
    return cube

print(cubefinder(3))
