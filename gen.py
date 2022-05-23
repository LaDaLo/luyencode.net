import sys
from datetime import datetime, timezone
_, file = sys.argv

with open(file + ".cpp", "w") as f, open("main.cpp", "r") as source:
    f.write("/*\n")
    f.write("-" * 15 + "luyencode.net" + "-" * 34 + '\n')
    f.write("-" * 15 + "Problem: " + file + "-" * 31 + '\n')
    f.write("-" * 15 + "Author: LaDaLo" + "-" * 33 + '\n')
    f.write("-" * 15 + "Time: " + str(datetime.now().astimezone())  + "-" * 9 + '\n')
    f.write("*/\n\n")
    for line in source:
        f.write(line)

    