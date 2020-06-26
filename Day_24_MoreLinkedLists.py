#Task
#A Node class is provided. A Node object has an integer data field,data, and a Node instance pointer,next , pointing to another node (i.e.: the next node in a list).

#A removeDuplicates function is declared, which takes a pointer to the head node of a linked list as a parameter. 
#Complete the removeDuplicates function so that it deletes any duplicate nodes from the list and returns the head of the updated list.


def removeDuplicates(self,head):
        #Write your code here
        if head!=None:
            cur=head
            nex=cur.next
            pre=cur
            while(cur!=None):
                while(nex!=None):                    
                    if nex.data==cur.data:                       
                        pre.next=nex.next
                    else:
                        pre=pre.next
                    nex=nex.next
                cur=cur.next
                if cur!=None:
                    nex=cur.next
                    pre=cur
        return head
  
