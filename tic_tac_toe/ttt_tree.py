
class Node:

    def __init__(self, game_state): 
        self.game_state = game_state
        self.upcoming_player = self.upcoming_player()
        self.winner = self.check_win_states()
    
    def upcoming_player(self): 
        upcoming_player = 2
        if self.game_state.count(1) == self.game_state.count(2):
            upcoming_player = 1
        return upcoming_player 

    def check_win_states(self):
    

        #rows
        if self.game_state[0] == self.game_state[1] == self.game_state[2] != 0: 
            return self.game_state[0]
        elif self.game_state[3] == self.game_state[4] == self.game_state[5] != 0: 
            return self.game_state[3]
        elif self.game_state[6] == self.game_state[7] == self.game_state[8] != 0: 
            return self.game_state[6]
        #columns
        elif self.game_state[0] == self.game_state[3] == self.game_state[6] != 0: 
            return self.game_state[0]
        elif self.game_state[1] == self.game_state[4] == self.game_state[7] != 0: 
            return self.game_state[1]
        elif self.game_state[2] == self.game_state[5] == self.game_state[8] != 0: 
            return self.game_state[2]
        #diagonals
        elif self.game_state[0] == self.game_state[4] == self.game_state[8] != 0: 
            return self.game_state[0]
        elif self.game_state[2] == self.game_state[4] == self.game_state[6] != 0: 
            return self.game_state[2]
        #cats_cradle
        elif 0 not in self.game_state: 
            return 'Tie'
        
        return None
    
    def remaining_moves(self): 
    
        avaliable_moves = []
        for i in range(9):
            if self.game_state[i] == 0:
                avaliable_moves.append(i)
        return avaliable_moves

class Queue:
    def __init__(self):
        self.items = [] 

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


class TicTacToeTree: 
    def __init__(self): 
        self.leaf_nodes = []
        self.num_leaf_nodes = 0

    def generate_tree(self): 
    
        empty_board = Node([0 for i in range(9)])

        queue = Queue()
        queue.enqueue(empty_board)
    
        while len(queue.items) != 0:
            current_node = queue.items[0]
            if current_node.winner == None: 
                avaliable_moves = current_node.remaining_moves()
                current_board = current_node.game_state
                for move in avaliable_moves: 
                    new_move_board = current_board.copy()
                    new_move_board[move] = current_node.upcoming_player
                    new_node = Node(new_move_board)
                    queue.enqueue(new_node)
            
            else: 
                self.leaf_nodes.append(current_node)
                self.num_leaf_nodes += 1 
            queue.dequeue() 
        



tree = TicTacToeTree()
tree.generate_tree()
print(tree.num_leaf_nodes)