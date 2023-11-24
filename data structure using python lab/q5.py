def search (self):
        d=int(input("enter the value you want to search in link list "))
        temp = self.head
        ind=0
        flag =True
        while(temp!=None):
            if (temp.data == d):
                print("index : ",ind)
                flag = False
                break
            temp=temp.next
            ind+=1
        if (flag == True):
            print("element not found in list")