def delete_from_start(self):
        if self.head is None:
            print("List is empty. Cannot delete from an empty list.")
            return

        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            # If there is only one element in the list
            self.head = None