#!/usr/bin/env python3

import re

from pathlib import Path

root = Path(__file__).absolute().parents[1]


def get_title(exercise):
    index = exercise / "index.adoc"
    text = index.open().read()
    match = re.match(r'^= (Exercise: )?(.+?)\n', text, re.DOTALL) 
    if match:
        return match.group(2)
    else:
        return None


def write_exercise_index(module, module_title, exercise_list):
    index_file = module / "exercises" / "index.adoc"
    with index_file.open("w") as fh:
        fh.write(f"""= {module_title} 
:includedir: ../../../includes
:source-highlighter: rouge
:stem:
:toc: left

++++
include::{{includedir}}/navigation.html[]
++++

== Exercises

""")
        for exercise_name, exercise_title in exercise_list:
            fh.write(f'- link:{exercise_name}/index.html[{exercise_title}]\n')

    print(f'wrote {index_file}')


for module in (root / 'modules').iterdir():
    if module.is_file(): continue

    module_title = get_title(module)

    exercises = module / "exercises"
    exercise_list = []
    for exercise in exercises.iterdir():
        if exercise.is_file(): continue

        exercise_title = get_title(exercise)
        exercise_list.append((exercise.name, exercise_title))

    if len(exercise_list) > 0:
        write_exercise_index(module, module_title, exercise_list)
