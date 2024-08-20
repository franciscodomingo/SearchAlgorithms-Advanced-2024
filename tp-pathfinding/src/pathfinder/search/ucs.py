from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        # Initialize the explored dictionary to be empty
        explored = {node.state: node.cost}

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.pop()
            if node.state == grid.end:
                return Solution(node, explored)

            actions = grid.get_neighbours(node.state)
            list_actions = list(actions.keys())
            for i in range(len(list_actions)):
                next_state = actions[list_actions[i]]
                next_cost = node.cost + grid.get_cost(next_state)
                if next_state not in explored or next_cost < explored[next_state]:
                    next_node = Node("", next_state, next_cost,
                                     node, actions[list_actions[i]])
                    explored[next_state] = next_cost
                    frontier.add(next_node, next_cost)
