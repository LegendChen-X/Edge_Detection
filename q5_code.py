import numpy as np
class Queue:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.insert(0,item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0
        
def neighbor_check(src,queue,labels):
    x_boundary, y_boundary = src.shape
    while 1:
        if(queue.isEmpty()): break
        position ,counter =  queue.pop()
        x = position[0]
        y = position[1]
        for i in range(-1,2):
            for j in range(-1,2):
                if (x+i<0 or x+i>=x_boundary or y+j<0 or y+j>=y_boundary): continue
                if src[x+i][y+j]==255 and labels[x+i][y+j]==-1:
                    labels[x+i][y+j] = counter
                    queue.push(((x+i,y+j),counter))
                    
    return counter + 1
        
def CC_label(src):
    queue = Queue()
    x, y = src.shape
    counter = 1
    label_buff = []
    labels = np.empty((x,y), dtype=int)
    for i in range(x):
        for j in range(y):
            labels[i][j] = -1
    for i in range(x):
        for j in range(y):
            if(src[i][j]==255 and labels[i][j]==-1):
                queue.push(((i,j),counter))
                labels[i][j] = counter
                counter = neighbor_check(src,queue,labels)
            
    return (labels ,counter)
      
                
