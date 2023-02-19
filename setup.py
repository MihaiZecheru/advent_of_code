"""
Setup the file structure for one day in the advent of code
"""

import os, sys

def main():
  print()

  if len(sys.argv) != 3:
    year = input("Year: ")
    day = input("Day: ")
  else:
    year = sys.argv[1]
    day = sys.argv[2]

  path = f"{year}/day_{day}"

  os.makedirs(f'{path}/part_1')
  os.makedirs(f'{path}/part_2')

  with open(f"{path}/part_1/part_1.py", "w") as f:
    f.write("import os\n\ndef get_data(path=\"input.txt\"):\n  with open(os.path.join(os.getcwd(), path)) as f:\n    return f.readlines()\n\ndef main():\n  data = get_data()\n\nif __name__ == '__main__':\n  main()")

  with open(f"{path}/part_1/input.txt", "w") as f: pass
  with open(f"{path}/part_1/prompt.md", "w") as f: pass
  with open(f"{path}/part_1/answer.txt", "w") as f: pass

  with open(f"{path}/part_2/part_2.py", "w") as f:
    f.write("import sys\nsys.path.append(\"../part_1/\")\nfrom part_1 import get_data\n\ndef main():\n  data = get_data(\"../part_1/index.txt\")\n\nif __name__ == '__main__':\n  main()")

  with open(f"{path}/part_2/prompt.md", "w") as f: pass
  with open(f"{path}/part_2/answer.txt", "w") as f: pass

if __name__ == '__main__':
  main()