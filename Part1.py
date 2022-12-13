from collections import deque
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def readFile():
    file = open("InputData.txt", "r")
    return file


def findStart(grid):
    startEnd = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 83):
                temp = (i, j)
                startEnd.append(temp)
            if (grid[i][j] == 69):
                temp = (i, j)
                startEnd.append(temp)
    return startEnd


def shortestPath(grid, startEnd):
    rowNum = len(grid[0])
    colNum = len(grid)
    # Has a node been visited yet?
    vis = [[False] * rowNum for i in range(colNum)]
    # Distance between nodes
    dist = [[0] * rowNum for i in range(colNum)]
    queue = deque()
    # Start with our starting node
    queue.append(startEnd[0])
    # Initialize our visited and distance list with the starting node
    vis[startEnd[0][0]][startEnd[0][1]] = True
    dist[startEnd[0][0]][startEnd[0][1]] = 0
    while len(queue):
        # Take out first element in the queue
        x, y = queue.popleft()
        # for each x and y in moves try the moves
        for dx, dy in moves:
            newX = x + dx
            newY = y + dy
            # 0 <= newX < rowNum: Makes sure our X is in the bounds of the grid
            # 0 <= newY < colNum: Makes sure our Y is in the bounds of the grid
            # not not vis[newX][newY]: Makes sure we haven't already visited the node
            # grid[newX][newY] <= grid[x][y]+1: Makes sure the move is allowed(One step above and any below)
            if 0 <= newX < colNum and 0 <= newY < rowNum and not vis[newX][newY] and grid[newX][newY] <= grid[x][y] + 1:
                # Add the new node to the queue so that we can check it later
                queue.append((newX, newY))
                # Set the visited to true
                vis[newX][newY] = True
                # Set the distance to the distance of the previous node + 1
                dist[newX][newY] = dist[x][y] + 1
    # Wasn't able to visit the end node
    if not vis[startEnd[1][0]][startEnd[1][1]]:
        print(-1)
    # Print the distance of the end node
    else:
        print(f"Shortest distance to E is: {dist[startEnd[1][0]][startEnd[1][1]]}")


def main():
    file = readFile()
    grid = []
    for line in file:
        split = [*line.strip()]
        split = list(map(ord, split))
        grid.append(split)
    startEnd = findStart(grid)
    grid[startEnd[0][0]][startEnd[0][1]] = 97
    grid[startEnd[1][0]][startEnd[1][1]] = 122
    shortestPath(grid, startEnd)
    file.close()


if (__name__ == "__main__"):
    main()
