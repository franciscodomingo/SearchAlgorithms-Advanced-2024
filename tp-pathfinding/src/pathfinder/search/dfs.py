from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
import pdb


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {}

        # Add the node to the explored dictionary
        # creo que esto habría que comentarlo
        # explored[node.state] = True

        # Test start node
        if node.state == grid.end:
            return Solution(node, explored)

        frontier = StackFrontier()
        # no hace el add, frontier queda vacío
        frontier.add(node)

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.remove()
            # ----

            if node.state in explored:
                continue
            # si no está en explorad lo agregamos (puede que esto no este bien)
            explored[node.state] = True

            # list_actions = list(actions.keys())
            # for i in range(len(list_actions)):
            actions = grid.get_neighbours(node.state)
            for i in actions:
                # next_state = actions[actions[i]]
                next_state = actions[i]
                next_node = Node("", next_state, node.cost+1,
                                 node, i)
                # next_node = Node("", next_state, node.cost+1)
                # next_node.action
                # next_node.parent
                # no marca el camino en amarillo
                if next_node not in explored:
                    if next_node.state == grid.end:
                        return Solution(next_node, explored)
                    frontier.add(next_node)
