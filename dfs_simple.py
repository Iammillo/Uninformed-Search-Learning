import numpy as np

matrix = np.array(
                 [[0,1,1,0,0],
                    [1,1,1,0,1],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0]
                 ])

visited = [0,0,0,0,0]
stack = [1]
node = stack.pop()
print(node)
visited[node]=1

while True:
    for x in range(0,len(visited)):
        if(matrix[node,x]==1 and visited[x]==0):
            stack.append(x)
            visited[x]=1
    if(len(stack)==0):
        break
    else:
        node = stack.pop()
        print(node)
