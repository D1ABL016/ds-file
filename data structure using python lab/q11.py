def traverse(self):
        temp =self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print()

def reverseTraversal(self):
        temp =self.head
        while(temp.next!=None):
            temp = temp.next
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.prev
        print()