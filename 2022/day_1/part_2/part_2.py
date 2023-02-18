import sys
sys.path.append("../part_1/")
from part_1 import get_data, format_data, count_calories

def top_three(elf_calories):
  top_elves = []

  for _ in range(3):
    top_elf = max(elf_calories)
    top_elves.append(top_elf)
    elf_calories.remove(top_elf)

  return top_elves

def main():
  data = get_data("../part_1/input.txt")
  elves = format_data(data)
  elf_calories = count_calories(elves)
  top_elves = top_three(elf_calories)
  total_calories = sum(top_elves)
  print(total_calories)

if __name__ == '__main__':
  main()