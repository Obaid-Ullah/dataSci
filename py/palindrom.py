from audioop import reverse
from operator import truediv


# def palendrom(word):
#     reverse_word = word[::-1]
#     if word== reverse_word:
#         return True
#     else:
#         return False

def palendrom(word):
    return word== word[::-1]
    
print(palendrom('horse'))
print(palendrom('naman'))