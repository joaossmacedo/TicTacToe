from Tree import Tree


class Board:
    USER = 'x'
    AI = 'o'

    def __init__(self):
        self._number_of_moves = 0
        self.winner = 'N'
        self.tiles = []
        for i in range(9):
            self.tiles.append(i)

    # prints the board
    def print_board(self):
        print('\n')
        for i in range(9):
            if self.tiles[i] == self.USER or self.tiles[i] == self.AI:
                print(' ' + self.tiles[i] + ' ', end='')
            else:
                print(' - ', end='')
            if (i + 1) % 3 == 0:
                print('')

    # movement by the player
    def manual_move(self):
        while True:
            while True:
                column = int(input('\nSelect a column: '))
                if 0 <= column < 3:
                    break
            while True:
                line = int(input('Select a line: '))
                if 0 <= line < 3:
                    break
            if self.tiles[line * 3 + column] != self.AI and self.tiles[line * 3 + column] != self.USER:
                break
        if self._number_of_moves % 2 == 0:
            self.tiles[line * 3 + column] = self.USER
        else:
            self.tiles[line * 3 + column] = self.AI

    # movement by the CPU
    def ai_move(self):
        possibilities = Tree()

        # simulates all the possibilities
        possibilities.simulate(self.tiles)

        possibilities.calculate_tree_height()

        chances = []

        for i in range(len(self.empty_tiles(self.tiles))):
            # calculates the difference between wins and looses in each of the next plays
            chances.append(possibilities.sum(possibilities.root.next[i]))

        # identify the best chance
        best_chance = max(chances)

        best_option = chances.index(best_chance)

        self.tiles = possibilities.root.next[best_option].tiles

    # a game
    def play(self):
        while True:
            number_of_players = int(input('How many players(MAX: 2): '))
            if 0 < number_of_players < 3:
                break

        while not self.check_end_game(self.tiles) and self._number_of_moves < 9:
            self.print_board()
            if number_of_players == 2 or self._number_of_moves % 2 == 0:
                self.manual_move()
            else:
                self.ai_move()
            self._number_of_moves += 1
        self.print_board()

        if self.winner == self.USER:
            print("\n\nCongrats player X\n")
        elif self.winner == self.AI:
            print("\n\nCongrats player O\n")
        else:
            print("\n\nTIC TAC TIE\n")

    # defines if a game is over or not
    def check_end_game(self, tiles):
        # X
        if tiles[0] == self.USER and tiles[1] == self.USER and tiles[2] == self.USER:
            self.winner = self.USER
            return True
        elif tiles[3] == self.USER and tiles[4] == self.USER and tiles[5] == self.USER:
            self.winner = self.USER
            return True
        elif tiles[6] == self.USER and tiles[7] == self.USER and tiles[8] == self.USER:
            self.winner = self.USER
            return True

        elif tiles[0] == self.USER and tiles[3] == self.USER and tiles[6] == self.USER:
            self.winner = self.USER
            return True
        elif tiles[1] == self.USER and tiles[4] == self.USER and tiles[7] == self.USER:
            self.winner = self.USER
            return True
        elif tiles[2] == self.USER and tiles[5] == self.USER and tiles[8] == self.USER:
            self.winner = self.USER
            return True

        elif tiles[0] == self.USER and tiles[4] == self.USER and tiles[8] == self.USER:
            self.winner = self.USER
            return True
        elif tiles[2] == self.USER and tiles[4] == self.USER and tiles[6] == self.USER:
            self.winner = self.USER
            return True
        # O
        elif tiles[0] == self.AI and tiles[1] == self.AI and tiles[2] == self.AI:
            self.winner = self.AI
            return True
        elif tiles[3] == self.AI and tiles[4] == self.AI and tiles[5] == self.AI:
            self.winner = self.AI
            return True
        elif tiles[6] == self.AI and tiles[7] == self.AI and tiles[8] == self.AI:
            self.winner = self.AI
            return True

        elif tiles[0] == self.AI and tiles[3] == self.AI and tiles[6] == self.AI:
            self.winner = self.AI
            return True
        elif tiles[1] == self.AI and tiles[4] == self.AI and tiles[7] == self.AI:
            self.winner = self.AI
            return True
        elif tiles[2] == self.AI and tiles[5] == self.AI and tiles[8] == self.AI:
            self.winner = self.AI
            return True

        elif tiles[0] == self.AI and tiles[4] == self.AI and tiles[8] == self.AI:
            self.winner = self.AI
            return True
        elif tiles[2] == self.AI and tiles[4] == self.AI and tiles[6] == self.AI:
            self.winner = self.AI
            return True

        return False

    # return the empty tiles
    def empty_tiles(self, tiles):
        return list(filter(lambda x: x != self.AI and x != self.USER, tiles))


init_board = Board()
init_board.play()
