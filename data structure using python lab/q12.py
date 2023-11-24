def search (self,d):
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