"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
def maiorPal(subfrase, palavras):
    maxmatch = 0
    for i in range(len(subfrase)+1):
        for palavra in palavras:
            if subfrase[:i] == palavra:
                maxmatch = max(maxmatch, i)
    return maxmatch

def espaca(frase, palavras):
    final = ""
    maior = 1
    while maior:
        maior = maiorPal(frase, palavras)
        if maior:
            final += frase[:maior] + ' '
            frase = frase[maior:]
    return final[:-1]
