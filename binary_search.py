def binary_search ( l,t ) :
    

    # here l is list 
    # t is targeted value
    # m is mid value

    start = 0 
    end = (len(l) -1)
    while start <= end :
        m = (start + end) // 2
        if t == l[m] :
            return m
        elif t <l[m] :
            end = m-1


        else :
            start = m+1


    return None




l = [1,2,3,4]
print(binary_search(l,2))















