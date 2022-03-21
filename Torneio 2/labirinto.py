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
    length = len(mapa)
    width = len(mapa[0])
    for y in range(length):
        for x in range(width):
            if mapa[y][x] == '#':
                continue
            elif (x, y) not in adj:
                adj[(x, y)] = set()
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if abs(i) + abs(j) == 2:
                        continue
                    if not 0 <= x+i < width:
                        continue
                    if not 0 <= y+j < length:
                        continue
                    if mapa[y+j][x+i] == '#':
                        continue
                    if (x+i, y+j) not in adj:
                        adj[(x+i, y+j)] = set()
                    
                    adj[(x, y)].add((x+i, y+j))
                    adj[(x+i, y+j)].add((x, y))

    return adj

def bfs(adj,o):
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

def caminho(mapa):
    o = (0,0)
    d = (len(mapa[0])-1 , len(mapa)-1)
    adj = build(mapa)
    pai = bfs(adj, d)
    final = ""

    while o in pai:
        dx = pai[o][0] - o[0]
        dy = pai[o][1] - o[1]
        if dx == 1 and dy == 0:
            final += 'E'
        elif dx == -1 and dy == 0:
            final += 'O'
        elif dx == 0 and dy == 1:
            final += 'S'
        elif dx == 0 and dy == -1:
            final += 'N'
        o = pai[o]

    return final
