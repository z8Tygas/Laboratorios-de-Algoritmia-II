"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""

def formata(codigo):
    ind = 0
    final = ""
    lw = ''
    for c in codigo:
        if c == ';':
            final += c + '\n'
            final += ind*2*' '
            lw = c
        elif c == '{':
            ind += 1
            final += c + '\n'
            final += ind*2*' '
            lw = c
        elif c == '}':
            ind -= 1
            final = final[:-2]
            final += c + '\n'
            final += ind*2*' '
            lw = c
        elif c == ' ' and lw == ';':
            continue
        else:
            final += c
            lw = c
    if lw == ';' or lw == '}':
        final = final[:-1-ind*2]
    return final
