"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""

def aux(ini, lista):
    result = 1
    last = ini

    for i in range(len(lista)):
        new = lista[i]
        if last <= new:
            result += 1
            last = new
    return result

def crescente(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return 1
    final = {}
    for i in range(1, len(lista)):
        final[i] = aux(lista[0], lista[i:])
    value = max(final.values())
    return value
