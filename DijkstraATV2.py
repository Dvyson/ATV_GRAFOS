import math


class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos-a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print('')

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamanho(self):
        return self.nos

    def menor_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'A árvore está vazia'

    def filho_esquerda(self, u):
        if self.nos >= 2*u:
            return self.heap[2*u-1]
        return 'Esse nó não tem filho'

    def filho_direita(self, u):
        if self.nos >= 2*u+1:
            return self.heap[2*u]
        return 'Esse nó não tem filho da direita'

    def pai(self, u):
        return self.heap[u // 2]


class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacencias:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo_vem





g = Grafo(10)

g.adiciona_aresta(1, 2, 10)
g.adiciona_aresta(1, 5, 3)
g.adiciona_aresta(1, 7, 5)
g.adiciona_aresta(2, 1, 5)
g.adiciona_aresta(2, 4, 3)
g.adiciona_aresta(2, 6, 3)
g.adiciona_aresta(3, 1, 6)
g.adiciona_aresta(3, 4, 8)
g.adiciona_aresta(3, 6, 8)
g.adiciona_aresta(4, 5, 10)
g.adiciona_aresta(4, 6, 1)
g.adiciona_aresta(4, 2, 5)
g.adiciona_aresta(5, 6, 20)
g.adiciona_aresta(5, 10, 8)
g.adiciona_aresta(5, 9, 11)
g.adiciona_aresta(6, 7, 20)
g.adiciona_aresta(6, 10, 12)
g.adiciona_aresta(6, 8, 5)
g.adiciona_aresta(7, 3, 2)
g.adiciona_aresta(7, 5, 7)
g.adiciona_aresta(8, 7, 2)
g.adiciona_aresta(8, 9, 12)
g.adiciona_aresta(8, 10, 3)
g.adiciona_aresta(9, 5, 2)
g.adiciona_aresta(9, 6, 20)
g.adiciona_aresta(9, 8, 4)
g.adiciona_aresta(10, 1, 5)
g.adiciona_aresta(10, 3, 7)
g.adiciona_aresta(10, 5, 4)
g.adiciona_aresta(10, 8, 20)
g.adiciona_aresta(10, 9, 6)

g.mostra_matriz()

print('\nResultado do menor caminho, com origem no vertice 1')
resultado_dijkstra = g.dijkstra(1)
print(resultado_dijkstra)

print('\n 4')