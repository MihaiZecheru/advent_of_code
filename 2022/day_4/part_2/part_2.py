import sys
sys.path.append("../part_1/")
from part_1 import get_data

def get_all_cleanup_sites(start: int, end: int):
  return range(start, end + 1)

def find_overlapping_elf_pairs(elf_pairs):
  for [elf1, elf2] in elf_pairs:
    elf1_sites = set(get_all_cleanup_sites(elf1.start, elf1.end))
    elf2_sites = set(get_all_cleanup_sites(elf2.start, elf2.end))
    if elf1_sites & elf2_sites: # same as elf1_sites.intersection(elf2_sites)
      yield [elf1, elf2]

def main():
  elf_pairs = get_data("../part_1/input.txt")
  find_overlapping_elf_pairs_count = len(list(find_overlapping_elf_pairs(elf_pairs)))
  print(find_overlapping_elf_pairs_count)

if __name__ == '__main__':
  main()