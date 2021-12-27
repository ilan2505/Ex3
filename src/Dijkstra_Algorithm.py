from Ex3.src.DiGraph import DiGraph

from Ex3.src.OrderedSet import add, creat, dec

MAX = 214932743


def Dijkstra_shorted_path(graph: DiGraph, src, dest):
    Q = list(graph.Nodelist)
    dist = creat()
    dist1 = creat()
    prev = {}

    for i in range(len(Q)):
        dist = add(dist, Q[i], MAX)
        dist1 = add(dist, Q[i], MAX)
        prev[i] = None
    dist1 = dec(dist1, Q[src], 0)
    dist = dec(dist, Q[src], 0)
    while Q.__contains__(dest) and len(Q) > 1:
        u = list(dist)[0]
        Q.remove(u)
        x = graph.all_out_edges_of_node(u)
        sort = tuple(x.values())
        for j in range(len(sort)):

            alt = dist1[u] + x[sort[j][0]][1]
            if alt < dist1[sort[j][0]]:
                dist1 = dec(dist1, sort[j][0], alt)
                dist = dec(dist, sort[j][0], alt)
                prev[sort[j][0]] = u
        del dist[u]
    t = [dest]
    if dist1[dest] == MAX:
        return -1, None
    prev1 = prev[dest]
    while prev1 != src:
        t.append(prev1)
        prev1 = prev[prev1]
    t.append(src)
    t.reverse()
    return dist1[dest], t


def Dijkstra_center(graph: DiGraph, src):
    Q = list(graph.Nodelist)
    dist = creat()
    dist1 = creat()
    prev = {}

    for i in range(len(Q)):
        dist = add(dist, Q[i], MAX)
        dist1 = add(dist, Q[i], MAX)
        prev[i] = None
    dist = dec(dist, src, 0)
    dist1 = dec(dist1, src, 0)
    while len(Q) != 0 and len(Q) > 1:
        u = list(dist)[0]
        Q.remove(u)
        x = graph.all_out_edges_of_node(u)
        if x is None:
            return  219439875
        sort = tuple(x.values())
        for j in range(len(sort)):

            alt = dist1[u] + sort[j][1]
            if alt < dist1[sort[j][0]]:
                dist1 = dec(dist1, sort[j][0], alt)
                dist = dec(dist, sort[j][0], alt)
                prev[sort[j][0]] = u
        del dist[u]
    return dist1[Q[0]]
