from zad2testy import runtests
import sys
sys.setrecursionlimit(300000)
from queue import PriorityQueue


RIGHT=0
DOWN=1
LEFT=2
UP=3

def robot2( L, A, B ):
    m=len(L[0])
    n=len(L)

    F=[[[float('inf ') for _ in range(4)]for _ in range(m)]for _ in range(n)]
    F[A[1]][A[0]][0]=0
    def f(i,j,direction):
        nonlocal n,m
        cur_time=F[i][j][direction]
        new_time=cur_time
       
        if direction==0:
            time=60
            for k in range(j+1,m):
                
                if L[i][k]=='X':
                    break
                if k-j==2:
                    time=40
                if k-j==3:
                    time=30
                new_time+=time
                if new_time< F[i][k][direction]:
                    F[i][k][direction]=new_time
                    f(i,k,direction)
        elif direction==DOWN:
            time=60
            for k in range(i+1,n):
                if L[k][j]=='X':
                    break
                if k-i==2:
                    time=40
                if k-i==3:
                    time=30
                new_time+=time
                if new_time< F[k][j][direction]:
                    F[k][j][direction]=new_time
                    f(k,j,direction)
        elif direction==LEFT:
            time=60
            for k in range(j-1,-1,-1):
                if L[i][k]=='X':
                    break
                if j-k==2:
                    time=40
                if j-k==3:
                    time=30
                new_time+=time
                if new_time< F[i][k][direction]:
                    F[i][k][direction]=new_time
                    f(i,k,direction)
        elif direction==UP:
            time=60
            for k in range(i-1,-1,-1):
                if L[k][j]=='X':
                    break
                if i-k==2:
                    time=40
                if i-k==3:
                    time=30
                new_time+=time
                if new_time< F[k][j][direction]:
                    F[k][j][direction]=new_time
                    f(k,j,direction)
        if F[i][j][(direction+1)%4]>F[i][j][direction]+45:
            F[i][j][(direction+1)%4]=F[i][j][direction]+45
            f(i,j,(direction+1)%4)
        if F[i][j][(direction+3)%4]>F[i][j][direction]+45:
            F[i][j][(direction+3)%4]=F[i][j][direction]+45
            f(i,j,(direction+3)%4)
        
    f(A[1],A[0],0)
    res= min(F[B[1]][B[0]]) 
    return res if res< float('inf') else None 

def robot( L, A, B ):
    m=len(L[0])
    n=len(L)
    Q=PriorityQueue()
    F=[[[[float('inf ') for _ in range(3)] for _ in range(4)]for _ in range(m)]for _ in range(n)]
    S=[60,40,30]
    F[A[1]][A[0]][0][0]=0

    Q.put((0,A[1],A[0],0,0))
    while not Q.empty():
        time,i,j,direction,speed=Q.get()
        if i==B[1] and j==B[0]:
            return time
        newSpeed=speed+1 if speed!=2 else 2

       
        if direction==0:
            if j+1<m and  L[i][j+1]!='X':  
                if F[i][j][direction][speed]+S[speed]<F[i][j+1][direction][newSpeed]:
                    F[i][j+1][direction][newSpeed]=F[i][j][direction][speed]+S[speed]
                    Q.put((F[i][j+1][direction][newSpeed],i,j+1,direction,newSpeed))     
        elif direction==DOWN:
            if i+1<n and  L[i+1][j]!='X':  
                if F[i][j][direction][speed]+S[speed]<F[i+1][j][direction][newSpeed]:
                    F[i+1][j][direction][newSpeed]=F[i][j][direction][speed]+S[speed]
                    Q.put((F[i+1][j][direction][newSpeed],i+1,j,direction,newSpeed))  
        elif direction==LEFT:
            if j-1>=0 and  L[i][j-1]!='X':  
                if F[i][j][direction][speed]+S[speed]<F[i][j-1][direction][newSpeed]:
                    F[i][j-1][direction][newSpeed]=F[i][j][direction][speed]+S[speed]
                    Q.put((F[i][j-1][direction][newSpeed],i,j-1,direction,newSpeed)) 
        elif direction==UP:
            if i-1>=0 and  L[i-1][j]!='X':  
                if F[i][j][direction][speed]+S[speed]<F[i-1][j][direction][newSpeed]:
                    F[i-1][j][direction][newSpeed]=F[i][j][direction][speed]+S[speed]
                    Q.put((F[i-1][j][direction][newSpeed],i-1,j,direction,newSpeed))  
        if F[i][j][(direction+1)%4][0]>F[i][j][direction][speed]+45:
            F[i][j][(direction+1)%4][0]=F[i][j][direction][speed]+45
            Q.put((F[i][j][(direction+1)%4][0],i,j,(direction+1)%4,0))
        if F[i][j][(direction+3)%4][0]>F[i][j][direction][speed]+45:
            F[i][j][(direction+3)%4][0]=F[i][j][direction][speed]+45
            Q.put(( F[i][j][(direction+3)%4][0],i,j,(direction+3)%4,0))
    return None
        
    
    
  






def robot2( L, A, B ):
    # 3 poziomy przyspieszenia, 4 możliwe kierunki, szerokość labiryntu, wysokość labiryntu
    DP = [[[[-1] * 3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    
    queue = PriorityQueue()
    # czas, położenie x, położenie y, kierunek, poziom przyspieszenia
    queue.put((0, A[0], A[1], 0, 0))

    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]

    while not queue.empty():
        time, x, y, direction, idx = queue.get()
        if (x, y) == B:
            return time
        if DP[y][x][direction][idx] != -1 or L[y][x] == 'X':
            continue
        DP[y][x][direction][idx] = time
        queue.put((time + 45, x, y, (direction + 1) % 4, 0))
        queue.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        queue.put((time + seconds[idx], x, y, direction, min(idx + 1, 2)))
    return None



                



                    




   

runtests( robot )


