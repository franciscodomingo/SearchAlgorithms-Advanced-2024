from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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
        # guardamos los estados de los nodos alcanzados en el diccionario explored
        explored[node.state] = True

        # Test start node
        if node.state == grid.end:
            return Solution(node, explored)

        frontier = QueueFrontier()
        frontier.add(node)

        while True:
            # el orden correcto es el que está acá
            if frontier.is_empty():
                return NoSolution(explored)
            node = frontier.remove()
            actions = grid.get_neighbours(node.state)
            list_actions = list(actions.keys())
            # deberia funcionar poniendo for clave in actions
            for i in range(len(list_actions)):
                next_state = actions[list_actions[i]]
                if next_state not in explored:
                    next_node = Node("", next_state, node.cost+1,
                                     node, actions[list_actions[i]])
                    # next_node.action
                    # next_node.parent
                    # no marca el camino en amarillo
                    if next_node.state == grid.end:
                        return Solution(next_node, explored)
                    # el dicc explored tiene como key el estado, el value es siempre true
                    explored[next_state] = True
                    frontier.add(next_node)
