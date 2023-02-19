import os

class File(object):
  name: str
  parent: any # Dir object
  size: int

  def __init__(self, name, size, parent):
    self.name = name
    self.parent = parent
    self.size = size

  def __repr__(self):
    return f"FILE {self.name}: {self.size}"

  def __lt__(self, other):
    return self.size < other.size

  def __gt__(self, other):
    return self.size > other.size

  def __ge__(self, other):
    return self.size >= other.size

  def __le__(self, other):
    return self.size <= other.size

class Dir(object):
  name: str
  parent: any # Dir object
  children: list # Dir objects

  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.children = []

  def __repr__(self):
    return f"DIR {self.name}: {self.size()}\n  - {[f'FILE {c.name}' if isinstance(c, File) else f'DIR {c.name}' for c in self.children]}"

  def add_child(self, child: File or any): # File or Dir
    self.children.append(child)

  def size(self) -> int:
    return sum(c.size() if isinstance(c, Dir) else c.size for c in self.children)

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    return [l.strip() for l in f.readlines()]

def execute_commands(cmds) -> Dir:
  # first command is "$ cd /"
  base_dir = Dir("root")
  current_dir = base_dir
  cmds.pop(0)

  # cmds = [
  #   "$ ls",
  #   "150555 bch.lht",
  #   "276291 ccqfdznj.sqg",
  #   "dir csmqbhjv",
  #   "dir czdqfr",
  #   "dir fpfwfzrt",
  #   "192660 qnbzgp",
  #   "142026 rpphgdhp.jfr",
  #   "dir sqphfslv",
  #   "38077 tvpzh",
  #   "$ cd csmqbhjv",
  #   "$ ls",
  #   "52822 bch.lht",
  #   "dir dgj",
  #   "dir fmmblb",
  #   "dir hjwwtw",
  #   "dir mtmhst",
  #   "dir njsccfms",
  #   "dir wmjsvq",
  #   "$ cd dgj",
  #   "$ ls",
  #   "266484 bch.lht",
  #   "dir brwncbh",
  #   "dir dtdzsqps",
  #   "216678 gvmdvcs.fmq",
  #   "225948 mdjrhmhf",
  #   "$ cd ..",
  # ]

  for cmd in cmds:
    if cmd.startswith("$ cd"):
      # change directory
      cd_to = cmd.split(" ")[2]

      if cd_to == "..":
        # go up a directory
        current_dir = current_dir.parent
      elif cd_to == "/":
        current_dir = base_dir
      elif cd_to in [d.name for d in current_dir.children]:
        current_dir = [d for d in current_dir.children if d.name == cd_to][0]
    elif cmd.startswith("$ ls"):
      # the next files will be added to the current_dir
      continue
    else:
      # add file or dir as a child of current_dir
      # because the previous command was $ ls
      if cmd.startswith("dir"):
        dir_name = cmd.split(" ")[1]
        if dir_name not in [d.name for d in current_dir.children]:
          # add dir
          new_dir = Dir(dir_name, current_dir)
          current_dir.add_child(new_dir)
      else:
        file_size, file_name = cmd.split(" ")
        if file_name not in [f.name for f in current_dir.children]:
          # add file
          new_file = File(file_name, int(file_size), current_dir)
          current_dir.add_child(new_file)

  return base_dir

def find_less_than_100k(base_dir: Dir) -> list:
  lt = []
  for c in base_dir.children:
    if isinstance(c, Dir):
      if c.size() < 100000:
        lt.append(c)
      lt.extend(find_less_than_100k(c))
  return lt

def get_total_size(files: list[File or Dir]) -> int:
  return sum(f.size if isinstance(f, File) else f.size() for f in files)

def main():
  cmds = get_data()
  base_dir = execute_commands(cmds)
  # files and dirs smaller than 100KB
  less_than_100k = find_less_than_100k(base_dir)
  total_size = get_total_size(less_than_100k)
  print(total_size)

if __name__ == '__main__':
  main()