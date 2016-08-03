from pip._vendor.distlib.compat import raw_input

def main():
    addToLocalizable('Helo', 'Hola')




def addToLocalizable(key, string):
    localizable = open('Localizable.strings', 'a')
    tu = (key, string)
    string = '"{0}" = "{1}";\n'.format(*tu)
    localizable.write(string)
    localizable.close()


if __name__ == '__main__':
    main()

# print("Opening the file %r" % filename)
# target = open(filename, 'r+')
# line = target.read(20)
# print(line)
# target.close()
# print("Introduce the name of the file")
# filename = raw_input("file: ")



