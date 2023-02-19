import os

class ElfCleanup(object):
  start: int
  end: int

  def __init__(self, site_range: str):
    site_range = site_range.split("-")
    self.start = int(site_range[0])
    self.end = int(site_range[1])

  def __repr__(self):
    return f"<ElfCleanup START: {self.start}, END: {self.end}>"

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return [[ElfCleanup(line.split(",")[0]), ElfCleanup(line.split(",")[1])] for line in f.readlines()]

def find_fully_contained_elf_pairs(elf_pairs):
  for [elf1, elf2] in elf_pairs:
    if (elf1.start <= elf2.start and elf1.end >= elf2.end) or (elf2.start <= elf1.start and elf2.end >= elf1.end):
      yield [elf1, elf2]

def main():
  elf_pairs = get_data()
  fully_contained_elf_pairs_count = len(list(find_fully_contained_elf_pairs(elf_pairs)))
  print(fully_contained_elf_pairs_count)

if __name__ == '__main__':
  main()