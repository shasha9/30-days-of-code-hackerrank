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
  
