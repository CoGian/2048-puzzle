from random import randint
import math
import time
from BaseAI_3 import BaseAI
from Displayer_3  import Displayer
from collections import deque
import itertools

class PlayerAI(BaseAI):

    def getMove(self, grid):

        disp = Displayer()
        moves = grid.getAvailableMoves()
        initial_state = self.ids_search(grid, moves)
        for child in initial_state.children:
            disp.display(child.grid)

        exit()
    def ids_search(self, grid, moves):
        initial_state = GridState(grid, moves)
        prev_initial_state = initial_state

        for depth in itertools.count():
            if self.dfs(initial_state, depth):
                prev_initial_state = initial_state
                initial_state = GridState(grid, moves)
            else:
                return prev_initial_state

    def dfs(self, initial_state, depth):
        # initialize frontier and explored
        frontier = deque()
        frontier.append(initial_state)

        # initialize metrics variables
        nodes = 0
        currTime = time.time()
        timelimit = 0.15
        while frontier:
            # pop the first state the last state entered in frontier
            state = frontier.pop()

            # check for time limit
            if time.time() - currTime > timelimit :
                return False

            # check if state does not exceed depth
            if state.cost < depth:

                # expand the state
                state.expand()

                nodes = nodes + 1

                for child in state.children:
                    # add child to frontier
                    frontier.append(child)

        return True


class GridState(object):

    def __init__(self, grid, moves, parent=None, action="Initial", cost=0, f=0 ):
        self.cost = cost  # int g cost

        self.parent = parent  # BlockState

        self.action = action  # string

        self.grid = grid

        self.moves = moves

        self.children = []  # list

        self.f = f  # f cost

    def expand(self):

        for move in self.moves:
            gridCopy = self.grid.clone()

            gridCopy.move(move)
            moves = gridCopy.getAvailableMoves()
            child = GridState(gridCopy, moves, parent=self, action=move, cost=self.cost + 1)
            self.children.append(child)

