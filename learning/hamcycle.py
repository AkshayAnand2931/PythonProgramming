import numpy as np


def isPrime(n: int) -> bool:
    """This function is to determine whether or not the given number is a prime number"""

    if n <= 1:
        return False

    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False

    return True


def pi_list(n: int) -> list:
    """This function is to generate a list of prime numbers starting from 2 to a given value n"""

    list_primes = []
    for i in range(0, n+1):
        if isPrime(i):
            list_primes.append(i)

    return list_primes


def knodel_adjacency(n: int) -> list:
    """This function defines the adjacency matrix for a given n-vertex knodel graph"""

    list_primes = pi_list(n)
    adjacency_matrix = np.zeros((2*n, 2*n), dtype=int)

    for i in range(1, 2*n+1):
        for j in range(1, 2*n+1):

            if i <= n:
                if j > n:
                    if j-i+1 in list_primes or j-i+1-n in list_primes:
                        adjacency_matrix[i-1][j-1] = 1

            if i > n:
                if j <= n:
                    if i-j+1 in list_primes or i-j+1-n in list_primes:
                        adjacency_matrix[i-1][j-1] = 1

    return adjacency_matrix


class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices
        self.vertices_i = list(range(0,self.V//2))
        self.vertices_j = list(range(self.V//2,self.V))

    def isSafe(self, v, pos, path,diff):

        if self.graph[path[pos-1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False
        
        if pos > 1:
            if v >= self.V//2:
                index = self.vertices_j.index(path[pos-2])
                count = (index + diff) % len(self.vertices_j)
                if self.vertices_j[count] == v:
                    return True
                else:
                    return False
                
            else:
                index = self.vertices_i.index(path[pos-2])
                count = (index + diff) % len(self.vertices_i)
                if self.vertices_i[count] == v:
                    return True
                else:
                    return False
    
        return True

    def hamCycleUtil(self, path, pos,diff):

        if pos == self.V:

            if self.graph[path[pos-1]][path[0]] == 1:
                self.graph[path[pos-1]][path[0]] = 0
                self.graph[path[0]][path[pos-1]] = 0
                return True
            else:
                return False

        for v in range(1, self.V):

            if self.isSafe(v, pos, path,diff) == True:

                path[pos] = v
                self.graph[path[pos-1]][v] = 0
                self.graph[v][path[pos-1]] = 0

                if self.hamCycleUtil(path, pos+1,diff) == True:
                    return True

                self.graph[path[pos-1]][v] = 1
                self.graph[v][path[pos-1]] = 1
                path[pos] = -1
            #print(path)
        return False

    def hamCycle(self,diff):
        path = [-1] * self.V

        path[0] = 0

        if self.hamCycleUtil(path, 1,diff) == False:
            #print("Solution does not exist\n")
            return False

        self.printSolution(path,diff)
        return True

    def printSolution(self, path,diff):
        #print("Solution Exists: Following is one Hamiltonian Cycle")
        print("The difference should be {}".format(diff))
        for vertex in path:
            print(vertex+1, end=" ")
        print(path[0]+1)

    def numHamCycles(self):
        count = 0
        prime_list = pi_list(self.V//2)
        prime_list.insert(0,1)
        while 1 in self.graph[0]:
            #print(self.graph)
            if self.hamCycle(prime_list[count]) == False:
                break
            else:
                count = count + 1
        print("The number of disjoint edges is {}".format(self.disjoint()))
        return count

    def disjoint(self):
        disjoint = 0
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 1:
                    disjoint = disjoint + 1
        return disjoint//2

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    g1 = Graph(2*n)
    g1.graph = knodel_adjacency(n)
    print("The number of cycles is {}".format(g1.numHamCycles()))