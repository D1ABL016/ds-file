def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        # Find the middle of the list
        mid = self.get_middle(head)
        left_half = head
        right_half = mid.next
        mid.next = None  # Split the list into two halves

        # Recursively sort the two halves
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        # Merge the sorted halves
        sorted_list = self.merge(left_half, right_half)

        return sorted_list

def merge(self, left, right):
        result = Node(None)  # Dummy node to simplify code
        current = result

        while left and right:
            if left.data < right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Add the remaining nodes, if any
        if left:
            current.next = left
        if right:
            current.next = right

        return result.next

def get_middle(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow