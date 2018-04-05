
class FileUtil:
    won = False

    def write_to_file(content, count):
        with open("output"+str(count)+".txt", "a") as myfile:
            myfile.write(content)

    def write_to_visual_file(content):
        with open("VisualTrace.txt", "a") as v_file:
            v_file.write(content)

    def read_input_file(main_list, file_name):
        i = 0
        file = open(file_name, 'r')
        for row in file:
            data = row.split(" ")
            main_list[i] = {
                'board': list(map(lambda x: ' ' if x == 'e' else x and x.replace('\n', ''), data)),
                'won': False
            }
            i = i + 1
        return main_list
