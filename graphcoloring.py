
# Python program for solution of M Coloring problem using backtracking 
  
class GraphColoring(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                              for row in range(vertices)]

    def acceptmat(self): #X of CSP 
        self.graph = [] 
        for i in range(self.V): 
            a=[] 
            for j in range(self.V): 
                a.append(int(input("Enter element for index {},{} :".format(i,j)))) 
            self.graph.append(a)
        print("Following is the adjacency matrix for our graph: ",self.graph)
        print()  
  
   
    def check(self, v, solution, c): #C of CSP
        for i in range(self.V): 
            if self.graph[v][i] == 1 and solution[i] == c: 
                return False
        return True
      
    def solver(self, m, solution, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m+1): 
            if self.check(v, solution, c) == True: 
                solution[v] = c 
                if self.solver(m, solution, v+1) == True: 
                    return True
                solution[v] = 0
  
    def graphcolouring(self, m): 
        solution = [0] * self.V 
        if self.solver(m, solution, 0) == False: 
            return False
  
        # Print the solution 
        print ("Solution exist in the following colours order:")
        for c in solution: 
            print (c) 
        return True
  

g  = GraphColoring(4) 
#adjmat = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]] 
g.acceptmat()
m=3 #D of CSP
g.graphcolouring(m)