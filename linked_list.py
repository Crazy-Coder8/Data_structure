




class Nord :
    data = None
    next_nord = None
    def __init__(self ,data):
        self .data = data


    def __repr__(self):
        return "<nord data : %s>"%self.data


class linked_list:
    
    def __init__(self):
        self.head = None


    def size(self):
        current = self.head
        count = 0
        while current :
            count +=1
            current = current.next_nord

        return count




        




