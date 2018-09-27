import numpy as np

matrix = np.array(
                [[0,1,1,0,0],
                [1,1,1,0,1],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,0]])

visited = [0,0,0,0,0]
queue = [4]

node = queue.pop(0)
visited[node]=1
print(node)

while True:
    for x in range(0,len(visited)):
        if(matrix[node,x]==1 and visited[x]==0):
            queue.append(x)
            visited[x] =1

    if (len(queue)==0):
        break
    else:
        node = queue.pop(0)
        print(node)
