import os, contextlib

class Stack:
  def __init__(self):
    self.a = []
    self.b = []
    self.c = []
    self.d = []
    self.e = []
    self.f = []
    self.g = []
    self.h = []
    self.i = []

  def __str__(self):
    return f"{self.a} {self.b} {self.c} {self.d} {self.e} {self.f} {self.g} {self.h} {self.i}"

  def __repr__(self):
    return self.__str__()

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return f.read().split(' 1   2   3   4   5   6   7   8   9 \n\n')

def format_stack(stack):
  rows = stack.split('\n')
  rows = [row.split(" ") for row in rows]
  stack = Stack()
  
  # looks like this:
  """
    [['[T]', '', '', '', '', '[Q]', '', '', '', '', '', '', '', '', '', '', '', '', '[S]' ...
  """
  # notice four empty strings translates to one skipped column
  
  # replace four empty strings with one empty string
  for row in rows:
    i = 0
    while i < len(row):
      with contextlib.suppress(IndexError):
        if row[i] == '' and row[i+1] == '' and row[i+2] == '' and row[i+3] == '':
          row[i] = 'skip'
          i += 3
      i += 1

  # now looks like this:
  """
    [['[T]', 'skip', '', '', '', '[Q]', 'skip', '', '', '', 'skip', '', '', '', 'skip', '', '', '', '[S]' ...
  """
  # remove the empty strings
  for row in rows:
    while '' in row:
      row.remove('')
    if len(row) == 0:
      rows.remove(row)

  for row in rows:
    col = 1
    for block in row:
      if block == 'skip':
        col += 1
        continue
      # add block to stack
      match col:
        case 1:
          stack.a.append(block)
        case 2:
          stack.b.append(block)
        case 3:
          stack.c.append(block)
        case 4:
          stack.d.append(block)
        case 5:
          stack.e.append(block)
        case 6:
          stack.f.append(block)
        case 7:
          stack.g.append(block)
        case 8:
          stack.h.append(block)
        case 9:
          stack.i.append(block)
      col += 1
      
  return stack

def execute(instructions, stack):
  # an instruction looks like this:
  # move 12 from 9 to 6
  for instruction in instructions:
    amount = int(instruction[5:instruction.index(' ', 5)])
    origin = int(instruction[instruction.index('from') + 5:instruction.index(' ', instruction.index('from') + 5)])
    to = int(instruction[instruction.index('to') + 3:])

    # access the stack's rows as a dict
    # 96 + 1 = 97 = 'a'
    # to_column = stack.__dict__[chr(to + 96)]
    # origin_column = stack.__dict__[chr(origin + 96)]

    # move the blocks
    for block in stack.__dict__[chr(origin + 96)][:amount]:
      stack.__dict__[chr(to + 96)].insert(0, block)

    # remove the blocks from the origin column
    for _ in range(amount):
      stack.__dict__[chr(origin + 96)].pop(0)

  return stack

def main():
  [stack, instructions] = get_data()
  stack = format_stack(stack)
  instructions = instructions.split('\n')
  stack = execute(instructions, stack)
  top_crates = ''.join([stack.a[0], stack.b[0], stack.c[0], stack.d[0], stack.e[0], stack.f[0], stack.g[0], stack.h[0], stack.i[0]]).replace('[', '').replace(']', '')
  print(top_crates)

if __name__ == '__main__':
  main()