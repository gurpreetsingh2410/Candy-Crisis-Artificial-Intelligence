from src.game import game
from src.auto import Auto
import os.path
import glob

def main():
    file_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_path)
    count = 0

    for file in glob.glob("input*.txt"):
        file = file_path+"/"+file
        count = count + 1
        input_type = input("How you want to play all the levels. Press '1' for Automatic and '2' for Manual ?")
        if len(input_type) == 1 and ord(input_type) == 49:
            Auto(file, count)
        elif len(input_type) == 1 and ord(input_type) == 50:
            game(file)
        else:
            print("Illegal Value")

if __name__ == '__main__':
    main()