def delete(self):
        pos= int(input("Enter positon  at which you want to delete "))
        if (pos<1):
            print("enter valid position ")
            return
        elif (pos==1):
            self.head = self.head.next
            return
        curr = self.head
        for i in range(1,pos):
            if (curr==None):
                print("enter a valid posiiton")
                return
            prev = curr
            curr = curr.next
        prev.next = curr.next