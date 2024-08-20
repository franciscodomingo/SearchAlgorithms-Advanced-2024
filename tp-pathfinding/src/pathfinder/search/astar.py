from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Herustic function
        def h(node, end):
            # return (pow((node.state[0]-end[0]), 2)+pow((node.state[1]-end[1]), 2))
            return (abs(node.state[0]-end[0])+abs(node.state[1]-end[1]))

        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        frontier = PriorityQueueFrontier()
        node.estimated_distance = h(node, grid.end)

        frontier.add(node, node.cost+node.estimated_distance)

        # Initialize the explored dictionary to be empty
        explored = {}

        # Add the node to the explored dictionary
        explored[node.state] = node.cost

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.pop()
            if node.state == grid.end:
                return Solution(node, explored)

            actions = grid.get_neighbours(node.state)
            list_actions = list(actions.keys())
            # for i in list_actions
            # for a,s in actions.items():
            for i in range(len(list_actions)):
                next_state = actions[list_actions[i]]
                next_cost = node.cost + grid.get_cost(next_state)
                if next_state not in explored or next_cost < explored[next_state]:
                    next_node = Node("", next_state, next_cost,
                                     node, actions[list_actions[i]])
                    explored[next_state] = next_cost
                    frontier.add(next_node, next_node.cost +
                                 h(next_node, grid.end))
