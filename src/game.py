import time
from src.board import board
from src.utils.file_utils import FileUtil
from src.utils.game_util import GameUtil


main_list = {}
start = time.time()
mode_type = 0
input_type = 0

class game:

    def __init__(self, file):
        self.file = file
        self.get_cont()

    def play_game_manual(self, board_object):
        while not GameUtil.check_game(board_object):
            position = input("Enter Q to Quit or Position to play on current board from letters as instructions A-O ").upper()
            if len(position) == 1 and ord(position) == 81:
                break
            elif len(position) == 1 and ord(position) > 64 and ord(position) < 80 :
                FileUtil.write_to_file(position)
                GameUtil.swap_tile(GameUtil.convert_letter_to_numeric(position), board_object)
                board(board_object['board'])
            else:
                print("illegal move")

        FileUtil.write_to_file("\n"+str(time.time() - start)[:4]+"ms")

    def get_cont(self):
        FileUtil.read_input_file(main_list, self.file)
        self.send_to_board()

    def send_to_board(self):
        for k, v in main_list.items():
            if main_list.get(k)['won'] == False:
                board(v['board'])
                self.play_game_manual(v)
