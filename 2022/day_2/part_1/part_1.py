import os

# A,X = 1; B,Y = 2; C,Z = 3; win = 6; tie = 3; loss = 0
results = {
  "AX": 1 + 3, "AY": 2 + 6, "AZ": 3 + 0,
  "BX": 1 + 0, "BY": 2 + 3, "BZ": 3 + 6,
  "CX": 1 + 6, "CY": 2 + 0, "CZ": 3 + 3,
}

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return [line.strip().replace(" ", "") for line in f.readlines()]

def calculate_score(games):
  return sum(results[game] for game in games)


def main():
  games = get_data()
  score = calculate_score(games)
  print(score)

if __name__ == '__main__':
  main()