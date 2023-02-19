import sys, os
sys.path.append("../part_1")
from part_1 import charcode

def chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i + n]

def get_data():
  with open(os.path.join(os.getcwd(), "../part_1/input.txt")) as f:
    lines = f.readlines()

    for i in range(len(lines)):
      lines[i] = lines[i].strip()

    return list(chunks(lines, 3))

def get_priorities(groups):
  for group in groups:
    elf1, elf2, elf3 = group
    for c in elf3:
      if c in elf1 and c in elf2:
        yield charcode(c)
        break

def main():
  groups = get_data()
  priorities = list(get_priorities(groups))
  total = sum(priorities)
  print(total)

if __name__ == '__main__':
  main()