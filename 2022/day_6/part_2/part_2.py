import sys
sys.path.append("../part_1/")
from part_1 import get_data

def find_start_index(buffer):
  for i in range(len(buffer)):
    seq = [buffer[i], buffer[i + 1], buffer[i + 2], buffer[i + 3], buffer[i + 4], buffer[i + 5], buffer[i + 6], buffer[i + 7], buffer[i + 8], buffer[i + 9], buffer[i + 10], buffer[i + 11], buffer[i + 12], buffer[i + 13]]

    all_unique = True
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
      if seq.count(letter) >= 2:
        all_unique = False
    
    if all_unique:
      return i + 14

def main():
  buffer = get_data("../part_1/input.txt")
  start_index = find_start_index(buffer)
  print(start_index)

if __name__ == '__main__':
  main()