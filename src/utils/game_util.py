class GameUtil:

    def convert_letter_to_numeric(letter):
        if letter == 'A':
            return 0
        elif letter == 'B':
            return 1
        elif letter == 'C':
            return 2
        elif letter == 'D':
            return 3
        elif letter == 'E':
            return 4
        elif letter == 'F':
            return 5
        elif letter == 'G':
            return 6
        elif letter == 'H':
            return 7
        elif letter == 'I':
            return 8
        elif letter == 'J':
            return 9
        elif letter == 'K':
            return 10
        elif letter == 'L':
            return 11
        elif letter == 'M':
            return 12
        elif letter == 'N':
            return 13
        elif letter == 'O':
            return 14
        elif letter == 'Q':
            return 21

    def swap_tile(position, board_object):
        if position - 1 >= 0 and board_object['board'][position - 1] == ' ':
            return swap_positions(position, board_object, position - 1)
        elif position + 1 <= 14 and board_object['board'][position + 1] == ' ':
            return swap_positions(position, board_object, position + 1)
        elif position - 5 >= 0 and board_object['board'][position - 5] == ' ':
            return swap_positions(position, board_object, position - 5)
        elif position + 5 <= 14 and board_object['board'][position + 5] == ' ':
            return swap_positions(position, board_object, position + 5)
        else:
            print("You cannot move this block. Please choose another position")


    @staticmethod
    def check_if_all_levels_finished(main_list):
        if all(main_list.get(k)['won'] == True for k in main_list):
            return True
        else:
            return False

    def check_game(object):
        data = object['board']
        if data[0] == data[10] and data[1] == data[11] and data[2] == data[12] and data[3] == data[13] and data[4] == data[14]:
            object['won'] = True
            print("You Won the above level")
            return True
        else:
            return False


def swap_positions(position, board_object, swap_with):
    temp = board_object['board'][position]
    board_object['board'][position] = board_object['board'][swap_with]
    board_object['board'][swap_with] = temp


