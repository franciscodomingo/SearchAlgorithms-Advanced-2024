# Search Algorithms #

This GitHub repository contains Python code for a maze game, where different search algorithms can be applied to solve the mazes. The implementation provides an educational visualization of how these algorithms behave in different scenarios. The following search algorithms are implemented:

- **Breadth-First Search (BFS)**: Explores all possible paths uniformly, expanding the shallowest nodes first.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking, expanding the deepest nodes first.
- **Uniform Cost Search (UCS)**: Expands the least costly node first, ensuring that the optimal path is found if costs vary.
- **Greedy Best-First Search (GBFS)**: Selects the node that appears to be closest to the goal based on a heuristic, which can be faster but not always optimal.
- **A***: Combines the benefits of UCS and GBFS by considering both the cost to reach a node and the estimated cost to reach the goal, providing an optimal and efficient solution.

## How to Run the Code ##

To execute the code, you need to install the required dependencies by running the following command in the repository:

```bash
pip install -r requirements.txt
```
And inside the repo, run:

```bash
python3 run.pyw
```