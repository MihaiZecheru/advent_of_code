import sys
sys.path.append("../part_1/")
from part_1 import get_data, format_stack

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
    for block in stack.__dict__[chr(origin + 96)][:amount][::-1]: # the only change is the [::-1] to reverse the list
      stack.__dict__[chr(to + 96)].insert(0, block)

    # remove the blocks from the origin column
    for _ in range(amount):
      stack.__dict__[chr(origin + 96)].pop(0)

  return stack

def main():
  [stack, instructions] = get_data("../part_1/input.txt")
  stack = format_stack(stack)
  instructions = instructions.split('\n')
  stack = execute(instructions, stack)
  top_crates = ''.join([stack.a[0], stack.b[0], stack.c[0], stack.d[0], stack.e[0], stack.f[0], stack.g[0], stack.h[0], stack.i[0]]).replace('[', '').replace(']', '')
  print(top_crates)

if __name__ == '__main__':
  main()