def merge(self, other_list):
        if self.head is None:
            self.head = other_list.head
        elif other_list.head is not None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = other_list.head
            other_list.head.prev = current_node
