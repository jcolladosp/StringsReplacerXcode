from pip._vendor.distlib.compat import raw_input
from tempfile import mkstemp
from shutil import move
from os import remove, close
import re


def main():
    fileCorrect = False

    while not fileCorrect:
        filename = raw_input("Name of the file: ")
        try:
            findInFile(filename)
        except (OSError, IOError) as e:
            print("File not found  \n")




def addToLocalizable(key, string):
    localizable = open('Localizable.strings', 'a')
    tupla = (key, string)
    string = '"{0}" = "{1}";\n'.format(*tupla)
    localizable.write(string)
    localizable.close()

def findInFile(filename):
    r= r'\@"(.*?)\"'

    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'r+') as new_file:
        with open(filename,'r+') as old_file:
            list_lines = old_file.readlines()
            for i,line in enumerate(list_lines):
                matchList = re.findall(r, line, flags=0)
                if matchList!=[]:

                    replacer_line = line
                    for string in matchList:
                        #print the founded string
                        print(list_lines[i - 1])
                        print(replacer_line.replace('@"'+string+'"', colors.WARNING +'@"'+string+'"'+ colors.ENDC ))
                        print(list_lines[i +1])

                        print('\n')
                        print(colors.BOLD +'String en código encontrada. ¿Que quieres hacer?\n'+colors.ENDC)
                        print('     1. Crear nuevo string. Este string no existia antes en Localizable.strings\n')
                        print('     2. Usar un string existente de Localizable.strings\n')
                        print('     3. No hacer nada')
                        print('\n')

                        try:
                            mode = int(raw_input('Opción: '))
                        except ValueError:
                            print('Tu ópcion introducida no es valida')

                        if mode == 1:
                            nombre = raw_input('Key del string: ')
                            replacer_line = replacer_line.replace('@"' + string + '"', 'NSLocalizedString(@"'+nombre+'", nil)')
                            addToLocalizable(nombre,string)
                        if mode == 2:
                            nombre = raw_input('Key del string: ')
                            replacer_line = replacer_line.replace('@"' + string + '"','NSLocalizedString(@"' + nombre + '", nil)')
                        if mode == 3:
                            continue





                    new_file.write(replacer_line)
                else:
                    new_file.write(line)


    close(fh)

    # remove(filename)

    # Move new file
    move(abs_path, 'modificado')



class colors:
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



