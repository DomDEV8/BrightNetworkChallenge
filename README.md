# BrightNetworkChallenge

### Approaches to the problem
#### DFS:
1. Create Node class to keep track of children nodes, and explore further until the end is reached
2. Use recursion until the goal is reached or all possible ways were evaluated
The pro, one of the easiest to implement
The con of this approach is the fact all nodes to be manually specified which makes it especially tricky with larger grids and obsticles

#### A*:
1. Create Node with Starting row, column, Ending row, column, estimated distance to the end and id to keep track of x and y axis
2. Create grid with the necessary data
The pro, the most efficient path searching algorithms
The con, space complexity while storing evaluated nodes, difficult to implement compared to the other path searching algorithms
