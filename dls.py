import numpy as np

matrix = np.array(
                 [[0,0,0,0,0,0,0,0,0,0,0,0],
                  [1,0,1,1,0,0,0,0,0,0,0,0],
                  [0,0,0,0,1,1,0,0,0,0,0,0],
                  [0,0,0,0,0,0,1,1,0,0,0,0],
                  [0,0,0,0,0,0,0,0,1,0,0,0],
                  [0,0,0,0,0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,0,0,0,0,0,1],
                  [0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0],
                 ])

max_depth = 1

visited = [0,0,0,0,0,0,0,0,0,0,0,0]
stack = [1]
depth_stack = [0]
node = stack.pop()
depth = depth_stack.pop()
print("node\tdepth")
print(node,"\t",depth)
visited[node]=1

while True:
    for x in range(0,len(visited)):
        if(matrix[node,x]==1 and visited[x]==0 and depth<max_depth):
            stack.append(x)
            depth_stack.append(depth+1)
            visited[x]=1
    if(len(stack)==0):
        break
    else:
        node = stack.pop()
        depth = depth_stack.pop()
        print(node,"\t",depth)
