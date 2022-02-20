"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""

def formata(codigo):
    ind = 0
    i = 0
    l = len(codigo)
    final = ""
    newline = True
    for c in codigo:
        i += 1
        if c == ';':
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '{':
            ind += 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == '}':
            final = final[:-2]
            ind -= 2
            final += c + ('\n'+ind*' ')*(i<l)
            newline = True
        elif c == ' ' and newline:
            continue
        else:
            newline = False
            final += c
    
    return final
