#Task
#Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) 
#and inserts it at the tail of the linked list referenced by the head parameter. 
#Once the new node is added, return the reference to the head node.

def insert(self,head,data): 
    n = Node(data)
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = n
            return head
        else:
            return n
