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
        for i in range(0, len(rota), 2):
            if i + 2 < len(rota):
                o = rota[i]
                p = rota[i+1]
                d = rota[i+2]
                if o not in adj:
                    adj[o] = {}
                if d not in adj:
                    adj[d] = {}
                adj[o][d] = p
                adj[d][o] = p

    return adj


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
