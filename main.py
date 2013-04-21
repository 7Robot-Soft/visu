#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from interface import Interface



if __name__ == '__main__':
    inter = Interface()
    sys.exit(inter.getAppHandle().exec_())
