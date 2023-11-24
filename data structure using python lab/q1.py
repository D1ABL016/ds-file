class node:
    def __init__(self,d):
        self.data=d
        self.next=None

class LinkList:
    def __init__(self):
       self.head = None

    def add1(self,d):
        n1 = node(d)
        if ((self.head)==None):
            self.head = n1
            return
        temp = self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next = n1
        return

           
    def traverse(self):
        temp =self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print()
   
   
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
           

       
       


ll = LinkList()
ll.add1(10)
ll.add1(45)
ll.add1(96)
ll.add1(4)
ll.add1(53)
ll.add1(95)
ll.traverse()
ll.delete()
ll.traverse()
