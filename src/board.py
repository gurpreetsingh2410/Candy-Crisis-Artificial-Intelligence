class board:

    def __init__(self, board):
        self.board = board
        self.draw_board()

    def draw_board(self):
        board = self.board
        print('   ____ ' + '____ ' + '____ ' + '____ ' + '____ ')
        print('  | ' + board[0] + '  |  ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3] + ' | ' + board[4] + '  |  ')
        print('   ---- ' + '---- ' + '---- ' + '---- ' + '---- ')
        print('   ____ ' + '____ ' + '____ ' + '____ ' + '____ ')
        print('  | ' + board[5] + '  | ' + board[6] + '  |  ' + board[7] + ' |  ' + board[8] + ' | ' + board[9] + '  |  ')
        print('   ---- ' + '---- ' + '---- ' + '---- ' + '---- ')
        print('   ____ ' + '____ ' + '____ ' + '____ ' + '____ ')
        print('  | ' + board[10] + '  | ' + board[11]+ '  |  ' + board[12] + ' |  ' + board[13] + ' | ' + board[14] + '  | ')
        print('   ---- ' + '---- ' + '---- ' + '---- ' + '---- ')
        print('  ==========================')

