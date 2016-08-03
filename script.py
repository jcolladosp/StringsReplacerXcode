from pip._vendor.distlib.compat import raw_input
from tempfile import mkstemp
from shutil import move
from os import remove, close
import re


def main():
    filename = raw_input("Name of the file: ")
    findInFile(filename)




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
                    print(list_lines[i-1])
                    print(colors.WARNING + list_lines[i]+ colors.ENDC)
                    print(list_lines[i-1])
                    for string in matchList:
                        replacer_line = line.replace('@"'+string+'"', 'Hola')
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

# print("Opening the file %r" % filename)
# target = open(filename, 'r+')
# line = target.read(20)
# print(line)
# target.close()
# print("Introduce the name of the file")
#
#print (colors.OKGREEN + "Warning: No active frommets remain. Continue?" + colors.ENDC)

