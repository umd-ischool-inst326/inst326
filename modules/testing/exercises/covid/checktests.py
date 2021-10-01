#!/usr/bin/env python3

import re
import sys
import pytest
import shutil
import pathlib

name = sys.argv[1]

work = pathlib.Path('.')
mfile, tfile = [f for f in sorted(work.iterdir()) if re.match(name, f.name)]

# convert uploaded filename to the filename that should be imported
module_file = re.sub(r'.+_question_\d+_\d+_(.+)$', r'\1', mfile.name)

shutil.copyfile(mfile, module_file)
print()
print(f"module_file: {module_file}")
print(f"test file: {tfile.name}")
print()
pytest.main([tfile.name])



