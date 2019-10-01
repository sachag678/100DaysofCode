import numpy as np
import random
import time
import math

class Node:

    def __init__(self, board, parent):
        self.board = board
        self.score = 0
        self.visits = 0
        self.ucb = 0
        self.children = []
        self.parent = parent

    def update(self, score):
        self.score += score
        self.visits += 1

    def update_ucb(self):
        self.ucb = self.score/(self.visits) + math.sqrt(2)*math.sqrt(math.log(self.parent.visits)/self.visits)

    def add_children(self, child):
        self.children.append(child)

    def __repr__(self):
        line = self.board.print_grid()
        line += '\n'
        line += 'score: ' + str(self.score)
        line += '\n'
        line += 'visits: ' + str(self.visits)
        line += '\n'
        line += 'ucb: ' + str(self.ucb)
        line += '\n'
        line += '-------------'
        return line

class TicTacToe():

    def __init__(self):
        self.grid = np.zeros((3,3))
        self.current_player = 1

    @staticmethod
    def Factory(grid, current_player):
        tc = TicTacToe()
        tc.grid = grid
        tc.current_player = current_player
        return tc

    def play_game(self, print_grid=False):
        count = 0
        grid_copy = np.copy(self.grid)
        while(self.game_not_over()):
            actions = self.get_available_actions()
            action = random.choice(actions)
            self.grid[action[0]][action[1]] = self.current_player
            if(self.current_player==1):
                self.current_player = -1
            else:
                self.current_player = 1
            if print_grid:
                print('-----' + 'Turn ' + str(count) + '-----')
                self.print_grid()
                print('----------------')
                time.sleep(0.5)
            count += 1

        score = self.get_value()
        self.grid = grid_copy
        return score

    def print_grid(self):
        line = ''
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[i][j]==1:
                    line += ' X '
                elif self.grid[i][j]==-1:
                    line += ' O '
                else:
                    line += ' _ '
            line += '\n'
        return line

    def get_available_actions(self):
        return [index for index in zip(np.where(self.grid==0)[0], np.where(self.grid==0)[1])]

    def __add__(self, action):
        temp = np.copy(self.grid)
        temp[action[0]][action[1]] = self.current_player
        if self.current_player == 1:
            pl = -1
        else:
            pl = 1
        return TicTacToe.Factory(temp, pl)

    def get_value(self):
        for i in range(0, 3):
            if (self.grid[:,i] == np.array([-1, -1, -1])).all():
                return -1
            if (self.grid[:,i] == np.array([1, 1, 1])).all():
                return 1

        for i in range(0, 3):
            if (self.grid[i,:] == np.array([-1, -1, -1])).all():
                return -1
            if (self.grid[i,:] == np.array([1, 1, 1])).all():
                return 1

        # Main Diagonal
        if (np.diag(self.grid) == np.array([1, 1, 1])).all():
            return 1

        if (np.diag(self.grid) == np.array([-1, -1, -1])).all():
            return -1

        # Opposite Diagonal
        if (np.diag(np.rot90(self.grid)) == np.array([1, 1, 1])).all():
            return 1

        if (np.diag(np.rot90(self.grid)) == np.array([-1, -1, -1])).all():
            return -1

        return 0

    def game_not_over(self):
        for i in range(0, 3):
            if (self.grid[:,i] == np.array([-1, -1, -1])).all():
                return False
            if (self.grid[:,i] == np.array([1, 1, 1])).all():
                return False

        for i in range(0, 3):
            if (self.grid[i,:] == np.array([-1, -1, -1])).all():
                return False
            if (self.grid[i,:] == np.array([1, 1, 1])).all():
                return False

        # Main Diagonal
        if (np.diag(self.grid) == np.array([1, 1, 1])).all():
            return False

        if (np.diag(self.grid) == np.array([-1, -1, -1])).all():
            return False

        # Opposite Diagonal
        if (np.diag(np.rot90(self.grid)) == np.array([1, 1, 1])).all():
            return False

        if (np.diag(np.rot90(self.grid)) == np.array([-1, -1, -1])).all():
            return False

        if(len(np.where(self.grid==0)[0])==0):
            return False

        return True

class MCTS:

    def __init__(self, board):
        self.current = Node(board, None)
        self.expand()

    def expand(self):
        actions = self.current.board.get_available_actions()
        for action in actions:
            self.current.add_children(Node(self.current.board+action, self.current))

    def backpropagation(self, score):
        pointer = self.current
        while True:
            pointer.update(score)
            pointer = pointer.parent
            if pointer is None:
                break
        self.current = self.current.parent

    def update_ucb(self):
        for child in self.current.children:
            child.update_ucb()

    def simulate(self):
        return self.current.board.play_game()

    def selection(self):

        tempCurrent = None
        for child in self.current.children:
            if child.visits == 0:
               tempCurrent = child
               break

        if tempCurrent is not None:
            self.current = tempCurrent
        else:
            #expand new nodes
            tree.update_ucb()
            best_ucb = 0
            best_index = 0
            for index, child in enumerate(self.current.children):
                if index ==0:
                    best_ucb = child.ucb
                    best_index = index

                if best_ucb<child.ucb:
                    best_ucb = child.ucb
                    best_index = index

            self.current = self.current.children[best_index]
            self.expand()
            self.selection()

if __name__ == '__main__':
    tc = TicTacToe()
    tree = MCTS(tc)
    for i in range(10):
        tree.selection()
        val = tree.simulate()
        tree.backpropagation(val)

    for child in tree.current.children:
        print(child)
