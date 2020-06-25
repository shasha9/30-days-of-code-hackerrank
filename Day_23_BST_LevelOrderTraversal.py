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
