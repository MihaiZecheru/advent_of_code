import os

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return f.read()

def find_start_index(buffer):
  for i in range(len(buffer)):
    seq = [buffer[i], buffer[i + 1], buffer[i + 2], buffer[i + 3]]

    all_unique = True
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
      if seq.count(letter) >= 2:
        all_unique = False
    
    if all_unique:
      return i + 4

def main():
  buffer = get_data()
  start_index = find_start_index(buffer)
  print(start_index)

if __name__ == '__main__':
  main()