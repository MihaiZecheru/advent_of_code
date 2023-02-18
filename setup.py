"""
Setup the file structure for one day in the advent of code
"""

import os

def main():
  print()
  year = input("Year: ")
  day = input("Day: ")
  path = f"{year}/day_{day}"

  os.makedirs(f'{path}/part_1')
  os.makedirs(f'{path}/part_2')

  with open(f"{path}/part_1/part_1.py", "w") as f:
    f.write("\n\ndef main():\n  pass\n\nif __name__ == '__main__':\n  main()")

  with open(f"{path}/part_1/input.txt", "w") as f: pass
  with open(f"{path}/part_1/prompt.md", "w") as f: pass
  with open(f"{path}/part_1/answer.txt", "w") as f: pass

  with open(f"{path}/part_2/part_2.py", "w") as f:
    f.write("import sys\nsys.path.append(\"../part_1/\")\n\ndef main():\n  pass\n\nif __name__ == '__main__':\n  main()")

  with open(f"{path}/part_2/prompt.md", "w") as f: pass
  with open(f"{path}/part_2/answer.txt", "w") as f: pass

if __name__ == '__main__':
  main()