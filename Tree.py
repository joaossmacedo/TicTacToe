import copy

USER = 'x'
AI = 'o'


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def check_end_game(tiles):

    # X
    if tiles[0] == USER and tiles[1] == USER and tiles[2] == USER:
        return -1
    elif tiles[3] == USER and tiles[4] == USER and tiles[5] == USER:
        return -1
    elif tiles[6] == USER and tiles[7] == USER and tiles[8] == USER:
        return -1
    elif tiles[0] == USER and tiles[3] == USER and tiles[6] == USER:
        return -1
    elif tiles[1] == USER and tiles[4] == USER and tiles[7] == USER:
        return -1
    elif tiles[2] == USER and tiles[5] == USER and tiles[8] == USER:
        return -1

    elif tiles[0] == USER and tiles[4] == USER and tiles[8] == USER:
        return -1
    elif tiles[2] == USER and tiles[4] == USER and tiles[6] == USER:
        return -1
    # O
    elif tiles[0] == AI and tiles[1] == AI and tiles[2] == AI:
        return 1
    elif tiles[3] == AI and tiles[4] == AI and tiles[5] == AI:
        return 1
    elif tiles[6] == AI and tiles[7] == AI and tiles[8] == AI:
        return 1

    elif tiles[0] == AI and tiles[3] == AI and tiles[6] == AI:
        return 1
    elif tiles[1] == AI and tiles[4] == AI and tiles[7] == AI:
        return 1
    elif tiles[2] == AI and tiles[5] == AI and tiles[8] == AI:
        return 1

    elif tiles[0] == AI and tiles[4] == AI and tiles[8] == AI:
        return 1
    elif tiles[2] == AI and tiles[4] == AI and tiles[6] == AI:
        return 1

    return 0


class Node:
    def __init__(self, tiles, depth):
        self.tiles = tiles
        self.depth = depth
        self.result = 0
        self.next = []


class Tree:
    def __init__(self):
        self.root = None
        self.tree_height = 0

    # simulate all plays
    def simulate(self, init_tiles):
        self.root = Node(init_tiles, 0)
        self.aux_simulate(self.root, AI, 1)

    # auxiliary method to simulate the plays
    def aux_simulate(self, node, player, depth):
        empty_tiles = list(filter(lambda x: x != USER and x != AI, node.tiles))

        if len(empty_tiles) <= 0:  # if all tiles are occupied
            return
        elif check_end_game(node.tiles) != 0:  # if its an end game situation
            node.result = check_end_game(node.tiles)
        else:
            # adds the next possible plays
            for i in range(len(empty_tiles)):
                pos = empty_tiles[i]
                new_tiles = copy.copy(node.tiles)
                new_tiles[pos] = player
                node_new_tiles = Node(new_tiles, depth)
                node.next.append(node_new_tiles)

            if player == AI:
                player = USER
            else:
                player = AI

            for i in range(len(empty_tiles)):
                self.aux_simulate(node.next[i], player, depth + 1)

    # sum all results
    def sum(self, node):
        next_sum = 0

        if node is None:
            return 0
        else:
            for i in range(len(node.next)):
                next_sum += self.sum(node.next[i])
            weight = factorial(self.tree_height - node.depth)
            return (weight * node.result) + next_sum

    # calculate tree height
    def calculate_tree_height(self):
        self.tree_height = self.aux_calculate_tree_height(self.root)

    # auxiliary method to calculate the tree height
    def aux_calculate_tree_height(self, p):
        if len(p.next) == 0:
            return 1
        else:
            return 1 + max(self.aux_calculate_tree_height(x) for x in p.next)
