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
        #2 circular arrays of vertices are created
        self.vertices_i = list(range(0,self.V//2))
        self.vertices_j = list(range(self.V//2,self.V))

    def isSafe(self, v:int, pos:int, path:list,diff:int)->bool:

        """The above function checks if the next vertex is valid and safe to travel to"""

        if self.graph[path[pos-1]][v] == 0: #Checks if the graph is connected
            return False
        
        for vertex in path: #Checks if the vertex is not repeated
            if vertex == v:
                return False
        
        if pos > 1:        
            #Checks if the difference is valid
            #2 circular array of vertices is created, and difference is added and checked if the next element is valid.
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

    def hamCycleUtil(self, path:list, pos:int,diff:int,size:int,file)->bool:

        """The function is used to traverse the vertices of the graph"""
        if pos == size:

            if self.graph[path[pos-1]][path[0]] == 1:
                self.graph[path[pos-1]][path[0]] = 0
                self.graph[path[0]][path[pos-1]] = 0
                return True
            else:
                return False

        for v in range(1, self.V):

            if self.isSafe(v, pos, path,diff) == True:

                #As the traversal is edge destroying changes are made to adjacency matrix
                path[pos] = v
                self.graph[path[pos-1]][v] = 0
                self.graph[v][path[pos-1]] = 0

                if self.hamCycleUtil(path, pos+1,diff,size,file) == True:
                    return True

                #If the vertex was not appropriate the changes are removed
                self.graph[path[pos-1]][v] = 1
                self.graph[v][path[pos-1]] = 1
                path[pos] = -1
        return False

    def hamCycle(self,diff:int,size:int,file,start:int)->bool:

        """The function finds one Hamiltonian cycle or normal cycle in the graph based on difference and size"""
        path = [-1] * size

        path[0] = start

        if self.hamCycleUtil(path, 1,diff,size,file) == False:
            return False

        self.printSolution(path,diff,file)
        return True

    def printSolution(self, path:list,diff:int,file)->None:
        #1 is added to all vertices as the expected output varies from 1 to n.

        print("The difference is {}".format(diff),file=file)
        for vertex in path:
            print(vertex+1, end=" ",file=file)
        print(path[0]+1,file=file)

    def numHamCycles(self,size:int,file)->int:

        """The function is used to find Hamiltonian or normal cycles based on difference, size and start"""
        count = 0 #The index in the prime list
        number = 0 #The number of cycles in the graph
        #The difference varies from 1,2,3...primes upto pi(n) - 2
        prime_list = pi_list(self.V//2)
        prime_list = [x for x in prime_list if x <= prime_list[len(prime_list)-1]-2]
        prime_list.insert(0,1)
        while 1 in self.graph[0]:
            start = 0
            if count>= len(prime_list):
                break
            if self.hamCycle(prime_list[count],size,file,start) == False:
                if size == self.V//2:
                    #As the cycles can start from any vertex, for normal cycles
                    #This tries every combination of starting vertex for given difference if we are checking for normal cycles
                    while(start<size):
                        start = start + 1
                        while self.hamCycle(prime_list[count],size,file,start) == True:
                           number = number + 1
                count = count + 1
                continue
            else:
                number = number + 1
                if size == self.V//2:
                    #Similar to above we are using this to check every starting vertex for the normal cycle
                    while(start<size):
                       while self.hamCycle(prime_list[count],size,file,start) == True:
                           number = number + 1
                       start = start + 1
        return number

    def disjoint(self):
        """This function is used to count the disjoint vertices left after all the cycles are done"""
        disjoint = 0
        #The number of 1's left in the adjacency matrix after all the cycles
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 1:
                    disjoint = disjoint + 1
        return disjoint//2
    
    def details(self,file):

        """The function used to list all the Hamiltonian cycles,normal cycles and the disjoint edges in a graph"""

        print("The Hamiltonian cycles start here:",file=file)
        print("The number of hamiltonian cycles is {}".format(self.numHamCycles(self.V,file)),file=file)
        print(file=file)
        print("The cycles of size {} start here: ".format(self.V//2),file=file)
        print("The number of cycles with size {} is {}".format(self.V//2,self.numHamCycles(self.V//2,file)),file=file)
        print(file=file)
        print("The number of disjoint edges is {}".format(self.disjoint()),file=file)
        print("\n",file=file)

if __name__ == "__main__":
    n1 = int(input("Enter the lower bound of n: "))
    n2 = int(input("Enter the upper bound of n: "))
    file = open("Hamiltonian.txt","w")

    for i in range(n1,n2+1):
        #Loop to iterate from lower to upper index to check for all graphs listed in the range
        g1 = Graph(2*i)
        g1.graph = knodel_adjacency(i)
        print("The value of n is {}".format(i),file=file)
        print("The adjacency matrix (C) is:",file=file)
        print(g1.graph[:(g1.V//2),(g1.V//2):],file=file)
        print(file=file)
        g1.details(file)

    file.close()
