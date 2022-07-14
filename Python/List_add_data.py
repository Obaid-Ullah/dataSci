# ====================================
# we use APPEND method to add items in a list
# append method always add items in the end list.
# For example

    # mixed = ['obaid','Ullah',1,2,3]
    # mixed.append(6)
    # print(mixed)
    # print(mixed[-1]*mixed[-2])
    # print(mixed[0]+'-'+mixed[1])

    # mixed = ['obaid','Ullah',1,2,3]
    # mixed.insert(-1,'O')
    # print(mixed)
# ===========To concatenate two lists=============

    # mixed = ['obaid','Ullah',1,2,3]
    # mixed2 = ['MSSE','2021-2023']
    # mixed.insert(-1,'')
    # mixed[2]=''
    # mixed[3]=''
    # mixed[4]=''
    # mix = mixed+mixed2
    # print(mix)

# ---- There is a diff between APPEND and EXTEND method
# if we APPEND a list it will add the whole list inside a list ,but by using EXTEND it will only EXTEND list items 
# but not the list inside a list..
# -==============lets have a look===============

    # mixed = ['obaid','Ullah',1,2,3]
    # mixed2 = ['MSSE','2021-2023']
    # print(mixed)
    # mixed.extend(mixed2)
    # print(mixed2)
    # print(mixed)
    # mixed.append(mixed2)
    # print(mixed)
# ===============Delete method >> Pop,remove methods and del operator is used for this purpose=======

from os import remove


mixed = ['obaid','Ullah',1,2,3]
mixed2 = ['MSSE','2021-2023']

# mixed.pop(2)
# mixed.pop(3)
# mix = mixed+mixed2
# mix.pop(2)
# print('pop method')
# print(mix)

# print('Delete operator')
# del mixed[2]
# del mixed[3]
# del mixed[-1]
# print(mixed)

print('REMOVE Method')
mixed.remove(1)
mixed.remove(2)
mixed.remove(3)

print(mixed)