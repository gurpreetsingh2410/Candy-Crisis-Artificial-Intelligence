from src.utils.file_utils import FileUtil
from src.board import board
import copy
import time

class Auto:

    def __init__(self, file, count):
        self.count = count
        self.file = file
        self.main_list = {}
        self.read_input_file()
        self.closedList = []
        self.openList = []
        self.prevList = []
        self.main()

    def add_one_object(self, parentObject, newBoard, emptyIndex, tempBoard, currentMove, cost):
        data = {}
        data['board'] = newBoard
        if emptyIndex != '*' or emptyIndex != "Null":
            data['parentMove'] = self.getLetter(emptyIndex)
        else:
            data['parentMove'] = "Null"
        data['heuristic'] = self.get_heuristic_value(tempBoard) + cost
        data['currentMove'] = self.getLetter(currentMove)
        data['parentObject'] = parentObject
        return data

    def add_to_close_object(self, board, parent, current):
        data = {}
        data['board'] = board
        data['parentMove'] = parent
        data['heuristic'] = self.get_heuristic_value(board)
        data['currentMove'] = current
        return data

    def getLetter(self, position):
            if position == 0:
                return 'A'
            elif position == 1:
                return 'B'
            elif position == 2:
                return 'C'
            elif position == 3:
                return 'D'
            elif position == 4:
                return 'E'
            elif position == 5:
                return 'F'
            elif position == 6:
                return 'G'
            elif position == 7:
                return 'H'
            elif position == 8:
                return 'I'
            elif position == 9:
                return 'J'
            elif position == 10:
                return 'K'
            elif position == 11:
                return 'L'
            elif position == 12:
                return 'M'
            elif position == 13:
                return 'N'
            elif position == 14:
                return 'O'

    def read_input_file(self):
        i = 0
        file = open(self.file, 'r').readlines()
        for row in file:
            data = row.split(" ")
            self.main_list[i] = {
                'board': list(map(lambda x: ' ' if x == 'e' or x == 'e\n' else x and x.replace('\n', ''), data))
            }
            i = i + 1

    def get_heuristic_value(self, board):
        data = board
        count = 0
        for i in range(5):
            if data[i] != data[i+10]:
                count = count+1
        return count

    @staticmethod
    def swap_for_possible_moves(currentBoard, currentPos, nextPos):
        board = currentBoard
        temp = board[currentPos]
        board[currentPos] = board[nextPos]
        board[nextPos] = temp
        return board

    def generate_moves(self, parentNode):
        currentNode = copy.deepcopy(parentNode)
        emptyIndex = currentNode['board'].index(' ')
        FileUtil.write_to_visual_file(str(currentNode['board'])+"\n")

        if (emptyIndex-1 >= 0 and emptyIndex-1 < 4) or (emptyIndex-1 >= 5 and emptyIndex-1 < 9) or (emptyIndex-1 >= 10 and emptyIndex-1 <= 14):
            tempBoard = copy.deepcopy(currentNode)
            newBoard = self.swap_for_possible_moves(tempBoard['board'], emptyIndex, emptyIndex-1)
            if not any(x['board'] == newBoard for x in self.closedList):
                self.openList.append(self.add_one_object(currentNode, newBoard, emptyIndex, tempBoard['board'], emptyIndex-1, 2))

        if (emptyIndex+1 > 0 and emptyIndex+1 <= 4) or (emptyIndex+1 > 5 and emptyIndex+1 <= 9) or (emptyIndex+1 > 10 and emptyIndex+1 <= 14):
            tempBoard = copy.deepcopy(currentNode)
            newBoard = Auto.swap_for_possible_moves(tempBoard['board'], emptyIndex, emptyIndex+1)
            if not any(x['board'] == newBoard for x in self.closedList):
                self.openList.append(self.add_one_object(currentNode, newBoard, emptyIndex, tempBoard['board'], emptyIndex+1, 2))

        if emptyIndex-5 >= 0:
            tempBoard = copy.deepcopy(currentNode)
            newBoard = self.swap_for_possible_moves(tempBoard['board'], emptyIndex, emptyIndex-5)
            if not any(x['board'] == newBoard for x in self.closedList):
                self.openList.append(self.add_one_object(currentNode, newBoard, emptyIndex, tempBoard['board'], emptyIndex-5, 1))

        if emptyIndex+5 <= 14:
            tempBoard = copy.deepcopy(currentNode)
            newBoard = self.swap_for_possible_moves(tempBoard['board'], emptyIndex, emptyIndex+5)
            if not any(x['board'] == newBoard for x in self.closedList):
                self.openList.append(self.add_one_object(currentNode, newBoard, emptyIndex, tempBoard['board'], emptyIndex+5, 1))

        self.openList.sort(key=lambda x: x['heuristic'])

    def play_automatic(self):
        if len(self.openList) >= 1:
            node = self.openList.pop(0)
            self.prevList.append(node)
            self.closedList.append(self.add_to_close_object(node['board'], node['parentMove'], node['currentMove']))
            self.generate_moves(node)
        else:
            self.generate_moves(self.main_list.get(0))

    def main(self):
        for k, v in self.main_list.items():
            start = int(round(time.time() * 1000))
            data = self.main_list.get(k)
            emptyIndex = data['board'].index(' ')
            print("Initial State")
            board(data['board'])
            self.openList.append(self.add_one_object(data, data['board'], '*', data['board'], emptyIndex, 0))
            while not any(x['heuristic'] == 0 for x in self.closedList):
                self.play_automatic()
            print("Goal State")
            goal_board = self.closedList[len(self.closedList)-1]
            board(goal_board['board'])
            output = self.generate_solution()
            end_time = str(int(round(time.time() * 1000) - start))+"ms"
            FileUtil.write_to_file(output+"\n", self.count)
            FileUtil.write_to_file(end_time+"\n", self.count)
            start = None
            end_time = None
            self.closedList = []
            self.openList = []
        print("Your output has been saved")

    def generate_solution(self):
        out = []
        node = self.prevList[-1]
        out.append(node['currentMove'])
        self.recursive_items(node, out)
        new_out = out[::-1]
        new = ''.join([str(x) for x in new_out[1:]])
        output = ''.join(new)
        return output

    def recursive_items(self, dict, out):
        current_keys = dict.keys()
        if 'parentObject' in current_keys:
            node = dict['parentObject']
            node_keys = node.keys()
            if 'currentMove' in node_keys:
                out.append(node['currentMove'])
            self.recursive_items(node, out)

