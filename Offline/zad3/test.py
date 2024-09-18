from zad3testy import runtests
def dominates(p1, p2):
    return p1[0] > p2[0] and p1[1] > p2[1]

def dominance(P):
    max_dominance = 0
    dominant_point = None
    
    for p1 in P:
        dominance = 0
        for p2 in P:
            if dominates(p1, p2):
                dominance += 1
        if dominance > max_dominance:
            max_dominance = dominance
            dominant_point = p1
    
    return max_dominance
       
  

#P=[(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)] 
#dominance(P)     


  # tu prosze wpisac wlasna implementacje
 








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )