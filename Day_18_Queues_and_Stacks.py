    def __init__(self):
        self.queue = []
        self.stack = []
        
    def pushCharacter(self, ch):
        self.stack.insert(0, ch)
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    def popCharacter(self):
        return self.stack.pop(0)
    def dequeueCharacter(self):
        return self.stack.pop()
     
    
