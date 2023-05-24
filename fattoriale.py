def fact(n):
    ret = n                 #O(1)
    while n > 1:            #O(n)
        ret *= n            #O(1) * n  
        n -= 1              #O(1) * n
    return ret              #O(1) 

#Tfact = O(n)
#Sfact = O(1)

def factRic(n):
    if n == 1 or n == 0:                #O(1)
        return 1                        #O(1)
    else:                               
        return n * factRic(n - 1)       #O(n)
    
#TfactRic = O(n)
#SfactRic = O(n)