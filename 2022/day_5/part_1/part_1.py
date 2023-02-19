import os

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return f.readlines()

def main():
  pass

if __name__ == '__main__':
  main()