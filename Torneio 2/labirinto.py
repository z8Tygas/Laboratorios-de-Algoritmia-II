'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''

def build(mapa):
    adj = {}
    for y in range(len(mapa)):
        for x in range(len(mapa)):
            if mapa[y][x] != '#':
                if x != len(mapa)-1:
                    if mapa[y][x+1] == ' ':
                        if (x,y) not in adj:
                            adj[(x,y)] = set()
                        if (x+1,y) not in adj:
                            adj[(x+1,y)] = set()
                        adj[(x,y)].add((x+1,y))
                        adj[(x+1,y)].add((x,y))
                if y != len(mapa)-1:
                    if mapa[y+1][x] == ' ':
                        if (x,y) not in adj:
                            adj[(x,y)] = set()
                        if (x,y+1) not in adj:
                            adj[(x,y+1)] = set()
                        adj[(x,y)].add((x,y+1))
                        adj[(x,y+1)].add((x,y))
    return adj

def bfs(adj, o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai

def curto(adj, o, d):
    pai = bfs(adj, o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return caminho

def caminho(mapa):
    adj = build(mapa)
    if len(adj)== 0:
        return ""
    maiscurto = curto(adj, (0,0), (len(mapa)-1, len(mapa)-1))
    strfinal = ""
    
    for i in range(len(maiscurto)-1):
        dx = maiscurto[i+1][0] - maiscurto[i][0]
        dy = maiscurto[i+1][1] - maiscurto[i][1]
        if dx == 1:
            strfinal += "E"
        elif dx == -1:
            strfinal += "O"
        elif dy == 1:
            strfinal += "S"
        elif dy == -1:
            strfinal += "N"
    return strfinal
