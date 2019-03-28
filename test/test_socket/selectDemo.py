# -*- coding:utf-8 -*-

import select
import threading
import sys

while True:
    readable, writeable, error = select.select([sys.stdin, ], [], [], 1)
    if sys.stdin in readable:
        print('select get stdin', sys.stdin.readline())