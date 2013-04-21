from sys import exit

from interface import Interface


if __name__ == '__main__':
    inter = Interface()
    exit(inter.getAppHandle().exec_())
