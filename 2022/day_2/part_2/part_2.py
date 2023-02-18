import sys
sys.path.append("../part_1/")
from part_1 import get_data

# 3 = scissors, 2 = paper, 1 = rock
# x = lose, y = tie, z = win
# find what is needed to get the result designated by X, Y, or Z
results = {
  "AX": 3 + 0, "AY": 1 + 3, "AZ": 2 + 6,
  "BX": 1 + 0, "BY": 2 + 3, "BZ": 3 + 6,
  "CX": 2 + 0, "CY": 3 + 3, "CZ": 1 + 6,
}

def calculate_score(games):
  return sum(results[game] for game in games)

def main():
  games = get_data("../part_1/input.txt")
  score = calculate_score(games)
  print(score)
  

if __name__ == '__main__':
  main()