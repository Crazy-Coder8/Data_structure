# this function is for linear search 
# and function need not to be sorted 
# use  only for the small list that to be sorted 




def  liner_search(value,lst) :
    for  _ in range (len(lst)) :
         if value == lst[_] :
             return _

    
d = [ 1,2,3,67,8,9,98]
print(liner_search(int(input()),d))


























