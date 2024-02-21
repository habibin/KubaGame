# Nargis Habibi
# May 30, 2021
# KubaGame: A players wins by pushing off and capturing seven neutral red stones or
# by pushing off all of the opposing stones. A player who has no legal moves available has lost the game.

class KubaGame():
    def __init__(self, first_player, second_player):  # Reb, Black, White marbles
        """takes as its parameters two tuples, each containing player name
        and color of the marble that the player is playing (ex: ('PlayerA', 'B'), ('PlayerB','W'))
        and it intializes the board"""

        self._first_player = first_player
        self._second_player = second_player
        self._current_turn = None
        self._winner = None
                            # 0,  1,    2,   3,   4,   5,   6
        self._marble_loc = [['W', 'W', 'X', 'X', 'X', 'B', 'B'],  # 0
                            ['W', 'W', 'X', 'R', 'X', 'B', 'B'],  # 1
                            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],  # 2
                            ['X', 'R', 'R', 'R', 'R', 'R', 'X'],  # 3
                            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],  # 4
                            ['B', 'B', 'X', 'R', 'X', 'W', 'W'],  # 5
                            ['B', 'B', 'X', 'X', 'X', 'W', 'W']]  # 6

        self._marble_count = []
        self._playerA_list = []
        self._playerB_list = []

    def get_playerA_list(self):
        """returns player A list"""
        return self._playerA_list

    def set_playerA_list(self, alist):
        """sets player A list"""
        self._playerA_list = alist

    def get_playerB_list(self):
        """returns player B list"""
        return self._playerB_list

    def set_playerB_list(self, blist):
        """sets player B list"""
        self._playerB_list = blist

    def get_first_player(self):
        """returns player name"""
        return self._first_player

    def set_first_player(self,first_player):
        """set player name"""
        self._first_player = first_player

    def get_second_player(self):
        """Returns marble color"""
        return self._second_player

    def set_second_player(self, second_player):
        """sets marble color"""
        self._second_player = second_player

    def get_current_turn(self):
        """returns the player name whose turn it is to play the game"""
        return self._current_turn

    def set_current_turn(self, current_turn):
        """Sets the player name whose turn it is to play the game"""
        self._current_turn = current_turn

    def get_board(self):
        """returns board"""
        return self._marble_loc

    def set_board(self, board):
        """sets board"""
        self._marble_loc = board

    def player_marble(self,player_name, coord):
        """sets the first player with the first move to the player name and marble color"""
        coord1 = list(coord)
        board = self.get_board()
        row = board[coord[0]]
        pos = coord[1]
        board_marble = row[pos]
        first_player = self.get_first_player()
        second_player = self.get_second_player()

        if player_name == first_player[0] and board_marble == first_player[1]:
            return True

        if player_name == second_player[0] and board_marble == second_player[1]:
            return True

        else:
            return False


    def isValid(self, coord, direction):
        """method checks if the move is valid"""
        board = self.get_board()

        """checks for edge of the board for forward"""
        if direction == "F":
            if coord[0] == 6:
                return True

            else:
                """checks if the opposite spot is empty"""
                if board[coord[0] + 1][coord[1]] == "X":
                    return True
                else:
                    return False

        """checks for edge of the board for backward"""
        if direction == "B":
            if coord[0] == 0:
                return True
            else:
                """checks if the opposite spot is empty"""
                if board[coord[0] - 1][coord[1]] == "X":
                    return True
                else:
                    return False

        """checks for edge of the board for left"""
        if direction == "L":
            if coord[1] == 6:
                return True
            else:
                """checks if the opposite spot is empty"""
                if board[coord[0]][coord[1] + 1] == "X":
                    return True
                else:
                    return False

        """checks for edge of the board for right"""
        if direction == "R":
            if coord[1] == 0:
                return True
            else:
                """checks if the opposite spot is empty"""
                if board[coord[0]][coord[1] - 1] == "X":
                    return True
                else:
                    return False

    def make_move(self, player_name, coord, direction):
        # direction=Left(L),Right(R),Forward(F),Backward(B)
        """takes 3 parameters and makes a move on the board if valid"""

        coord1 = list(coord)  # convert the tuple into list
        board = self.get_board()

        """first 3 if checks if move is valid"""
        # player cannot undo a move the opponent just made (if it leads to the exact same board position)
        if self.isValid(coord1, direction) == True:

            if self.player_marble(player_name,coord) == True:

                if self.get_current_turn() == player_name or self.get_current_turn() == None:

                    """updates next player's turn"""
                    if player_name == 'PlayerA':
                        self.set_current_turn('PlayerB')
                    else:
                        self.set_current_turn('PlayerA')

                    if direction == "L":
                        row = board[coord1[0]]
                        #print(row)
                        pos = coord1[1]
                        current = row[pos]
                        temp = row[pos - 1]
                        next = row[pos - 2]

                        while pos > 0:
                            """if player removes a red marble off the board, adds it to player's list"""
                            if pos == 1 and row[pos - 1] == 'R':
                                if player_name == 'PlayerA':
                                    alist = self.get_playerA_list()
                                    alist.append(row[pos - 1])
                                    self.set_playerA_list(alist)

                                else:
                                    blist = self.get_playerB_list()
                                    blist.append(row[pos - 1])
                                    self.set_playerB_list(blist)

                            """shifts the marbles"""
                            if row[pos] != 'X':
                                if row[pos - 1] == 'X':
                                    row[pos - 1] = current
                                    row[coord1[1]] = 'X'
                                    #print(row)
                                    return True

                                else:
                                    row[pos - 1] = current
                                    current = temp
                                    temp = next
                                    next = row[pos - 3]
                                    pos -= 1
                                    row[coord1[1]] = 'X'
                                    #print(row)

                        return True

                    if direction == "R":
                        row = board[coord1[0]]
                        #print(row)
                        pos = coord1[1]
                        current = row[pos]
                        temp = row[pos + 1]

                        while pos < 6:
                            """if player removes a red marble off the board, adds it to player's list"""
                            if pos == 5 and row[pos + 1] == 'R':
                                if player_name == 'PlayerA':
                                    alist = self.get_playerA_list()
                                    alist.append(row[pos + 1])
                                    self.set_playerA_list(alist)

                                else:
                                    blist = self.get_playerB_list()
                                    blist.append(row[pos + 1])
                                    self.set_playerB_list(blist)

                            """shifts the marbles"""
                            if row[pos] != 'X':
                                if row[pos + 1] == 'X':
                                    row[pos + 1] = current
                                    row[coord1[1]] = 'X'
                                    #print(row)
                                    return True

                                else:
                                    row[pos + 1] = current
                                    current = temp
                                    if (pos + 2) < 6:
                                        temp = next = row[pos + 2]
                                    if (pos + 3) < 6:
                                        next = row[pos + 3]
                                    pos += 1
                                    row[coord1[1]] = 'X'
                                    #print(row)
                        return True

                    if direction == "B":
                        column = coord1[1]
                        column_list = []
                        for row in range(0, 7):
                            column_list.append(board[row][column])
                            #print(column_list)

                        row = column_list
                        pos = coord1[0]
                        current = row[pos]
                        temp = row[pos + 1]

                        while pos < 6:
                            """if player removes a red marble off the board, adds it to player's list"""
                            if pos == 5 and row[pos + 1] == 'R':
                                if player_name == 'PlayerA':
                                    alist = self.get_playerA_list()
                                    alist.append(row[pos + 1])
                                    self.set_playerA_list(alist)

                                else:
                                    blist = self.get_playerB_list()
                                    blist.append(row[pos + 1])
                                    self.set_playerB_list(blist)

                            """shifts the marbles"""
                            if row[pos] != 'X':
                                if row[pos + 1] == 'X':
                                    row[pos + 1] = current
                                    row[coord1[0]] = 'X'
                                    #print(row)
                                    return True

                                else:
                                    row[pos + 1] = current
                                    current = temp
                                    if (pos + 2) < 6:
                                        temp = next = row[pos + 2]
                                    if (pos + 3) < 6:
                                        next = row[pos + 3]
                                    pos += 1
                                    row[coord1[0]] = 'X'
                                    #print(row)

                        column = coord1[1]
                        for i in range(0, 7):
                            board[i][column] = row[i]

                        return True

                    if direction == "F":
                        column = coord1[1]
                        column_list = []
                        for row in range(0, 7):
                            column_list.append(board[row][column])
                        #print(column_list)

                        row = column_list
                        pos = coord1[0]
                        current = row[pos]
                        temp = row[pos - 1]
                        next = row[pos - 2]

                        while pos > 0:

                            """if player removes a red marble off the board, adds it to player's list"""
                            if pos == 1 and row[pos - 1] == 'R':
                                if player_name == 'PlayerA':
                                    alist = self.get_playerA_list()
                                    alist.append(row[pos - 1])
                                    self.set_playerA_list(alist)

                                else:
                                    blist = self.get_playerB_list()
                                    blist.append(row[pos - 1])
                                    self.set_playerB_list(blist)

                            """shifts the marbles"""
                            if row[pos] != 'X':
                                if row[pos - 1] == 'X':
                                    row[pos - 1] = current
                                    row[coord1[0]] = 'X'
                                    #print(row)
                                    return True

                                else:
                                    row[pos - 1] = current
                                    current = temp
                                    temp = next
                                    next = row[pos - 3]
                                    pos -= 1
                                    row[coord1[0]] = 'X'
                                    #print(row)

                        column = coord1[1]
                        for i in range(0, 7):
                            board[i][column] = row[i]

                        return True

                    if self.get_winner() != None:
                        return self.get_winner()

                else:
                    return False

            else:
                return False

        else:
            return False

    def get_winner(self):
        """returns the name of the winning player."""
        marble_count_list = list(self.get_marble_count())
        white_marble_count = marble_count_list[0]
        black_marble_count = marble_count_list[1]
        first_player = self.get_first_player()
        second_player = self.get_second_player()

        """if player catured 7 red marbles"""
        if self.get_captured('PlayerA') == 7:
            return 'PlayerA'

        if self.get_captured('PlayerB') == 7:
            return 'PlayerB'

        """if all the players marbles are off the board"""
        if white_marble_count == 0:
            if first_player[1] == 'W':
                return second_player[0]
            else:
                return first_player[0]

        if black_marble_count == 0:
            if first_player[1] == 'B':
                return second_player[0]
            else:
                return first_player[0]

        else:
            return None

    def get_captured(self, player_name):
        """takes player's name as parameter and returns the number of Red marbles captured by the player"""
        # print(self.get_playerA_list())

        if player_name == 'PlayerA':
            leng_alist = self.get_playerA_list()
            return len(leng_alist)

        else:
            leng_blist = self.get_playerB_list()
            return len(leng_blist)

    def get_marble(self, coord):
        """takes the coordinates of a cell as a tuple and returns the marble that is present at the location"""
        coord1 = list(coord)  # convert the tuple into list
        board = self.get_board()
        row = board[coord1[0]]
        pos = coord1[1]

        return row[pos]

    def get_marble_count(self):
        """returns the number of White marbles, Black marbles and Red marbles as tuple in the order(W,B,R)"""

        white = 0
        black = 0
        red = 0
        for row in self._marble_loc:
            for space in row:
                if space == 'W':
                    white += 1
                if space == 'B':
                    black += 1
                if space == 'R':
                    red += 1
        return (white, black, red)


game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
game.get_marble_count() #returns (8,8,13)
game.get_captured('PlayerA') #returns 0
game.get_current_turn() #returns 'PlayerB' because PlayerA has just played.
game.get_winner() #returns None
game.make_move('PlayerB', (1,1), 'L')
game.get_captured('PlayerB')
game.get_marble_count()
game.make_move('PlayerA', (6,5), 'L') #Cannot make this move
game.get_marble((5,5)) #returns 'W'
