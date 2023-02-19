import os

class File(object):
  name: str
  parent: any # Dir object
  size: int

  def __init__(self, name, size, parent=None):
    self.name = name
    self.parent = parent
    self.size = size

  def __repr__(self):
    return f"{self.name}: {self.size}"

class Dir(object):
  name: str
  parent: any # Dir object
  children: list # Dir objects
  size: int

  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.children = []
    self.size = 0

  def __repr__(self):
    return f"{self.name}: {self.size}"

  def add_child(self, child: File or any): # File or Dir
    self.children.append(child)
    self.size += child.size

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return f.readlines()

def main():
  data = get_data()

if __name__ == '__main__':
  main()