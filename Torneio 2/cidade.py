'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''

def build(ruas):
    adj = {}

    for rua in ruas:
        if rua[0] in adj.keys() and rua[-1] in adj[rua[0]].keys():
            if adj[rua[0]][rua[-1]] > len(rua):
                adj[rua[0]][rua[-1]] = len(rua)
                adj[rua[-1]][rua[0]] = len(rua)
        else:
            if rua[0] not in adj:
                adj[rua[0]] = {}
            if rua[-1] not in adj:
                adj[rua[-1]] = {}
            adj[rua[0]][rua[-1]] = len(rua)
            adj[rua[-1]][rua[0]] = len(rua)
    return adj
  

####################################
#        Solved with dijkstra      #
####################################


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

def tamanho(ruas):
    adj = build(ruas)
    dist = 0
    for cruz in adj.keys():
        pai = dijkstra(adj, cruz)
        for cruzd in adj.keys():
            if cruz != cruzd:
                temp = 0
                d = cruzd
                while d in pai:
                    temp += adj[d][pai[d]]
                    d = pai[d]
                dist = max(dist, temp)

    return dist
  
#########################################
#        Solved with Floy-Warshall      #
#########################################
  
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


def tamanho(ruas):
    adj = build(ruas)
    dist = 0
    dist = fw(adj)
    maxdist = 0
    for cruz in adj:
        for cruzd in adj:
            maxdist = max(maxdist, dist[cruz][cruzd])
    return maxdist
