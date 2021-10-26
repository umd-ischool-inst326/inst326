#!/usr/bin/env python3

import io
import sh
import sys
import csv
import json

correct = {
    "Montgomery": "15",
    "Frederick": "13",
    "Anne Arundel": "11",
    "Unknown": "7",
    "Baltimore": "7",
    "Worcester": "2",
    "Prince George's": "2",
    "Cecil": "2",
    "Wicomico": "2",
    "Kent": "1",
    "Howard": "1",
    "Allegany": "1",
    "Talbot": "1",
    "Caroline": "1",
    "Washington": "1",
    "Baltimore City": "1",
    "Garrett": "1",
    "Carroll": "1",
    "Somerset": "1"
}

program = sys.argv[1]
output = sh.python3(program).stdout.decode('utf8')

results = {}
for row in csv.reader(io.StringIO(output)):
    if len(row) == 2:
        results[row[0].strip()] = str(row[1]).strip()

if json.dumps(results, sort_keys=True) == json.dumps(correct, sort_keys=True):
    print("OK")
else:
    print(output)
