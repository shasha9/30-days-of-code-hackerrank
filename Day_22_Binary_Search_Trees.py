#Task
#The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
#You are given a pointer,root,pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

def getHeight(self,root):
        
        if root.left==None and root.right==None:
            return(0)
        else:
            hLeft = 0
            hRight = 0
            if root.left:
                hLeft = self.getHeight(root.left) + 1
            if root.right:
                hRight = self.getHeight(root.right) + 1
            return(max(hLeft, hRight))
