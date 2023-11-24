def update(self):
        old = int(input("enter the data that you want to change "))
        new = int(input("enter the data that you want to replace with the old one "))
        current_node = self.head
        while current_node:
            if current_node.data == old:
                current_node.data = new
                return
            current_node = current_node.next
        print(f"Node with data {old} not found.")