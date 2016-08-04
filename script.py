from tempfile import mkstemp
from shutil import move
from os import remove, close
import re
import sys
from shutil import copyfile

keys = []


def main():
    fileCorrect = False

    while not fileCorrect:
        filename = input("Name of the file: ")
        try:
            file = open(filename, 'r')
            file.close()
            copyfile(filename, filename + '_copia')
            fileCorrect = True
        except (OSError, IOError, FileNotFoundError):
            print(Colors.FAIL + "File " + filename + " not found  \n" + Colors.ENDC)

        try:
            localizable = open('Localizable.strings', 'r')
            # global keys
            # keys = localizable.readlines()
            localizable.close()

        except (OSError, IOError):
            print(Colors.FAIL + "Localizable.strings not found  \n" + Colors.ENDC)
            sys.exit()



    find_in_file(filename)


def add_to_localizable(key, string):
    localizable = open('Localizable.strings', 'a')
    tupla = (key, string)
    string = '"{0}" = "{1}";\n'.format(*tupla)
    localizable.write(string)
    localizable.close()


def find_in_file(filename):
    r = r'\@"(.*?)\"'

    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'r+') as new_file:
        with open(filename, 'r+') as old_file:
            list_lines = old_file.readlines()
            for i, line in enumerate(list_lines):
                matchList = re.findall(r, line, flags=0)
                if not matchList == []:

                    replacer_line = line
                    for string in matchList:
                        # print the founded string
                        print(list_lines[i - 1])
                        print(replacer_line.replace('@"' + string + '"',
                                                    Colors.WARNING + '@"' + string + '"' + Colors.ENDC))
                        print(list_lines[i + 1])

                        print('\n')
                        print(Colors.BOLD + 'There\'s a string in the code. Choose an option\n' + Colors.ENDC)
                        print('     1. New string. This string is not in Localizable.strings\n')
                        print('     2. Use a existent string in Localizable.strings\n')
                        print('     3. Continue')
                        print('\n')

                        validNumber = False
                        while not validNumber:
                            try:
                                mode = int(input('Option: '))
                                if mode > 3:
                                    raise ValueError('Option out of range')
                                else:
                                    validNumber = True
                            except ValueError:
                                print('That\'s not a valid option')

                        if mode == 1:
                            nombre = input('String key: ')

                            replacer_line = replacer_line.replace('@"' + string + '"',
                                                                  'NSLocalizedString(@"' + nombre + '", nil)')
                            add_to_localizable(nombre, string)
                        if mode == 2:
                            nombre = input('String key: ')
                            replacer_line = replacer_line.replace('@"' + string + '"',
                                                                  'NSLocalizedString(@"' + nombre + '", nil)')
                        if mode == 3:
                            continue

                    new_file.write(replacer_line)
                else:
                    new_file.write(line)

    close(fh)

    remove(filename)

    # Move new file
    move(abs_path, filename)


# Method that check if the key is already in Localizable.strings. For future versions
# def check_key_in_localizable(key):
#    for string in keys:
#        if string == '"'+key+'"':
#            print(key + " is already in Localizable.strings. Choose another one")

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    main()
