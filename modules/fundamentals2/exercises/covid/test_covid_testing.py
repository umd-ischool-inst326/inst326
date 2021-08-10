#!/usr/bin/env python3

import os
import sys

from subprocess import Popen, PIPE, STDOUT

data = '''Ed Summers
y
1
2
Kesa Summers
n
1
3
Maeve Summers
n
.96
2
Charles Summers
n
.96
2
Graham Summers
n
.98
2
stop
'''

if os.path.isfile('covid-results.csv'):
    os.remove('covid-results.csv')

prog = sys.argv[1]
pipe = Popen(['python3', prog], stdout=PIPE, stdin=PIPE, stderr=PIPE)
pipe.communicate(input=data.encode('utf8'))[0]

expected = '''Ed Summers,1,1.0,2
Kesa Summers,0,1.0,3
Maeve Summers,0,0.96,2
Charles Summers,0,0.96,2
Graham Summers,0,0.98,2
'''

found = open('covid-results.csv').read()

if found != expected:
    print("Error")
    print(found)
