def recursive_binary_search (l,t) :
    if len(l) == 0 :
        return False
    else :
        m = len(l) // 2 
        if t == l[m] :
            return m+1
        elif t < l[m] :
            return recursive_binary_search(l[:m+1],t)
        else :
            return recursive_binary_search(l[m-1:],t)



import binary_search  
t = [1,2,3,4,5]

print( binary_search.binary_search(t,4))
print( recursive_binary_search(t,4))
