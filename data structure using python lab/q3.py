def traverse(self):
        temp =self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print()