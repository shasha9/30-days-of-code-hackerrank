#Task
#A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom.

def levelOrder(self,root):
        #BFS
        aVisiter=[root]
        while len(aVisiter)>0:
            for i in range(len(aVisiter)):
                el=aVisiter.pop(0)
                print(el.data, end=" ")
                if el.left:
                    aVisiter.append(el.left)
                if el.right:
                    aVisiter.append(el.right)
