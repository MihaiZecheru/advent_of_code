import os

def get_data(path="input.txt"):
  # split each line in half
  with open(os.path.join(os.getcwd(), path)) as f:
    lines = []
    for line in f:
      line = line.strip()
      half = len(line) // 2
      lines.append([line[:half], line[half:]])
    return lines

def charcode(char):
  return ord(char) - 38 if char.isupper() else ord(char) - 96

def get_priority_numbers(backpacks):
  nums = []

  # compartments
  for [c1, c2] in backpacks:
    for char in c2:
      if char in c1:
        nums.append(charcode(char))
        break

  return nums

def main():
  backpacks = get_data()
  priority_numbers = get_priority_numbers(backpacks)
  total = sum(priority_numbers)
  print(total)

if __name__ == '__main__':
  main()