from collections import defaultdict
  

jugA = int(input("Enter capacity of jug 1 : "))
jugB = int(input("Enter capacity of jug 2 : "))
target = int(input("Enter target volume: "))
#jugA, jugB, target = 3, 4, 2

kmap = defaultdict(lambda: False)
  
def solve(volA, volB): 
  
   
    if (volA == target and volB == 0) or (volB == target and volA == 0):
        
        print("( {},{} )".format(volA, volB))
        return True
      
    
    if kmap[(volA, volB)] == False:
        print("( {},{} )".format(volA, volB))
      
        
        kmap[(volA, volB)] = True
      
        
        return (solve(0, volB) or
                solve(volA, 0) or
                solve(jugA, volB) or
                solve(volA, jugB) or
                solve(volA + min(volB, (jugA-volA)),
                volB - min(volB, (jugA-volA))) or
                solve(volA - min(volA, (jugB-volB)),
                volB + min(volA, (jugB-volB))))
      
   
    else:
        return False
  

print("Steps: ")
# initial state : (0,0) final state (0,2)
solve(0, 0)