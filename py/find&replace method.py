string = 'If you encounter UnSupportedClassVersionError, check the JRE version you are using to run program and switch to higher version for quick solution.'
# print(string.replace(' ','-',5))
print(string.find('to'))

tofrst = string.find('to')
tosecond = string.find('to', tofrst+1)
print(tosecond)
# ----------

print('If you encounter UnSupportedClassVersionError, check the JRE version you are using to run program and switch to higher version for quick solution.'.replace(' ','-',5))
print('If you encounter UnSupportedClassVersionError, check the JRE version you are using to run program and switch to higher version for quick solution.'.find('to'))
