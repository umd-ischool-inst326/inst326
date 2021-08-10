from pathlib import Path
import re

all = Path("all.txt").read_text(encoding="utf-8").splitlines()
this = []
for line in all:
    match = re.search(r"^FEDERALIST No. (\d+)$", line.strip())
    if match:
        if this:
            prev.write_text("\n".join(this).strip(), encoding="utf-8")
        this = []
        prev = Path(f"federalist_{match.group(1)}.txt")
    this.append(line.strip())

prev.write_text("\n".join(this).strip(), encoding="utf-8")
