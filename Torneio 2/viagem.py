'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''

def build(rotas):
    adj = {}
    for rota in rotas:
        for i in range(0, len(rota)-2, 2):
            cid1 = rota[i]
            custo = rota[i+1]
            cid2 = rota[i+2]
            if cid1 not in adj:
                adj[cid1] = {}
            if cid2 not in adj:
                adj[cid2] = {}
            adj[cid1][cid2] = custo
            adj[cid2][cid1] = custo

    return adj

###############################
#     Dijkstra Version        #
###############################

def dijkstra(adj,o):
 pai = {}
 dist = {}
 dist[o] = 0
 orla = {o}
 while orla:
    v = min(orla,key=lambda x:dist[x])
    orla.remove(v)
    for d in adj[v]:
        if d not in dist:
            orla.add(d)
            dist[d] = float("inf")
        if dist[v] + adj[v][d] < dist[d]:
            pai[d] = v
            dist[d] = dist[v] + adj[v][d]
 return pai

def viagem(rotas,o,d):
    custo = 0

    adj = build(rotas)
    if d not in adj:
        return custo
    pai = dijkstra(adj, d)

    while o in pai:
        custo += adj[o][pai[o]]
        o = pai[o]

    return custo


####################################
#     Floyd-Warshal Version        #
####################################

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist

def viagem(rotas,o,d):
    adj = build(rotas)
    if not len(adj):
        return 0
    dists = fw(adj)
    return dists[o][d]
