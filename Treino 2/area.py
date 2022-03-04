'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def area(p,mapa):
    xi, yi = p

    if mapa[yi][xi] == '*':
        return 0
    else:
        area = 1
        vis = {(xi,yi)}
        queue = [(xi,yi)]
        while queue:
            x,y = queue.pop(0)
            for i in [-1,0,1]:
                for k in [-1,0,1]:
                    if abs(i)+abs(k)-2:
                        if (x+i,y+k) not in vis:
                            if y + k >= 0 and y + k < len(mapa) and x + i >= 0 and x + i < len(mapa):
                                if mapa[y+k][x+i] == '.':
                                    print("add", x+i,y+k )
                                    vis.add((x+i,y+k))
                                    area += 1
                                    queue.append((x+i,y+k))

        return area
