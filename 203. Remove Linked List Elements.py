# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.
# val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Definition for singly-linked list.
from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle empty list case
        if not head:
            return None

        # Initialize a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                # Skip the node with the specified value
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return dummy.next


if __name__ == "__main__":
    # Create a linked list [1, 2, 6, 3, 4, 5, 6]
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

    # Create an instance of the Solution class
    solution = Solution()

    # Call the removeElements method
    modified_head = solution.removeElements(head, 6)

    # Print the modified linked list
    while modified_head:
        print(modified_head.val, end=" ")
        modified_head = modified_head.next

# op: 1 2 3 4 5 