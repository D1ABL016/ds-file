def add1(self,d):
        n1 = node(d)
        if ((self.head)==None):
            self.head = n1
            return
        temp = self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next = n1
        n1.prev = temp
        return