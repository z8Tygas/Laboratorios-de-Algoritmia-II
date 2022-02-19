'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):
    maxeq = 0
    for i in range(1,len(palavra)):
        if palavra[:i] == palavra[-i:]:
            maxeq = i
    final = palavra
    final += (n-1) * palavra[maxeq:]
    
    if n != 0:
        return final
    else:
        return ''
