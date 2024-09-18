# Drzewo prefiksowe

from zad2testy import runtests



def double_prefix( L ):
    Prefix={}
    res=[]
    for string in L:
        cur_prefix=string
        for z in range(len(string),0,-1):
            cur_prefix=string[:z]
            if cur_prefix not in Prefix:
                Prefix[cur_prefix]=1
                
            else:
                Prefix[cur_prefix]+=1   
                if Prefix[cur_prefix]>=2:
                    break
    for p,l in Prefix.items():      
        if l>=2:
            res.a
            
   

    

runtests( double_prefix )

