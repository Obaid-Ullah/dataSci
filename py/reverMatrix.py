
def m_list(l):
    rev=[]
    for i in l:
        rev.append(i[::-1])
    return rev

mix = [[1,2,3],[4,5,6],[7,8,9]]
print(m_list(mix))
            
