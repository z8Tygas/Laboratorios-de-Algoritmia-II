'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def build(vizinhos):
    adj = {}
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in adj:
                adj[pais] = set()
            for pais2 in fronteira:
                if pais != pais2:
                    if pais2 not in adj:
                        adj[pais2] = set()
                    adj[pais].add(pais2)
    return adj

################################
#    Also possible with DFS    #
################################

def bfs(adj,o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return vis

def maior(vizinhos):
    adj = build(vizinhos)
    vis = []
    tamanho = 0
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in vis:
                continente = bfs(adj,pais)
                vis.append(list(continente))
                tamanho = max(tamanho, len(continente))
    return tamanho
