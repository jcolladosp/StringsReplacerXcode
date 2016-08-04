from tempfile import mkstemp
from shutil import move
from os import remove, close
import re
import sys


def main():
    fileCorrect = False

    while not fileCorrect:
        filename = input("Name of the file: ")
        try:
            file = open(filename, 'r')
            file.close()
            fileCorrect = True
        except (OSError, IOError,FileNotFoundError):
            print(Colors.FAIL + "File " + filename + " not found  \n" + Colors.ENDC)


        try:
            localizable = open('Localizable.strings', 'r')
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
                        print(Colors.BOLD + 'String en código encontrada. ¿Que quieres hacer?\n' + Colors.ENDC)
                        print('     1. Crear nuevo string. Este string no existia antes en Localizable.strings\n')
                        print('     2. Usar un string existente de Localizable.strings\n')
                        print('     3. No hacer nada')
                        print('\n')

                        try:
                            mode = int(input('Opción: '))
                        except ValueError:
                            print('Tu ópcion introducida no es valida')

                        if mode == 1:
                            nombre = input('Key del string: ')
                            replacer_line = replacer_line.replace('@"' + string + '"',
                                                                  'NSLocalizedString(@"' + nombre + '", nil)')
                            add_to_localizable(nombre, string)
                        if mode == 2:
                            nombre = input('Key del string: ')
                            replacer_line = replacer_line.replace('@"' + string + '"',
                                                                  'NSLocalizedString(@"' + nombre + '", nil)')
                        if mode == 3:
                            continue

                    new_file.write(replacer_line)
                else:
                    new_file.write(line)

    close(fh)

    # remove(filename)

    # Move new file
    move(abs_path, 'modificado')


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
