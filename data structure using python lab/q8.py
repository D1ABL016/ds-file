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