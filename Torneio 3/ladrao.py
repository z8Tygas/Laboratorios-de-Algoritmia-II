"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""

def ladrao(capacidade,objectos):
    if len(objectos) == 0 or capacidade == 0:
        return 0
    if objectos[-1][2] > capacidade:
        return ladrao(capacidade, objectos[:-1])
        
    a = objectos[-1][1] + ladrao(capacidade - objectos[-1][2], objectos[:-1])
    b = ladrao(capacidade, objectos[:-1])
    return max(a,b)
