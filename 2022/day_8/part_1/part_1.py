import os

def get_data(path="input.txt"):
  with open(os.path.join(os.getcwd(), path)) as f:
    matrix = [list(l.strip()) for l in f.readlines()]
    for item in matrix:
      for j in range(len(item)):
        item[j] = int(item[j])
    return matrix

def check_top(tree_matrix, x: int, y: int, original_tree_height: int = -1, first_time: bool = True) -> bool:
  """
    Check if the tree at x, y can be seen from the top

    returns True if the tree is taller than the tree above it
  """

  print(tree_matrix[x][y], x, y, original_tree_height, original_tree_height > tree_matrix[x][y])

  # if x = 0, then we are at the top
  if x == 0: return True

  # original tree height is the height of the first tree in the recursive loop
  if original_tree_height == -1: original_tree_height = tree_matrix[x][y]

  if first_time:
    return tree_matrix[x][y] > tree_matrix[x - 1][y] and check_top(tree_matrix, x - 1, y, original_tree_height, False)
  else:
    return original_tree_height > tree_matrix[x][y] and check_top(tree_matrix, x - 1, y, original_tree_height, False)

def check_bottom(tree_matrix, x: int, y: int, original_tree_height: int = -1, first_time: bool = True) -> bool:
  """
    Check if the tree at x, y can be seen from the bottom

    returns True if the tree is taller than the tree below it
  """
  
  # if x = len(tree_matrix) - 1, then we are at the bottom
  if x == len(tree_matrix) - 1: return True

  # original tree height is the height of the first tree in the recursive loop
  if original_tree_height == -1: original_tree_height = tree_matrix[x][y]

  if first_time:
    return tree_matrix[x][y] > tree_matrix[x + 1][y] and check_bottom(tree_matrix, x + 1, y, original_tree_height, False)
  else:
    return original_tree_height > tree_matrix[x][y] and check_bottom(tree_matrix, x + 1, y, original_tree_height, False)

def check_right(tree_matrix, x: int, y: int, original_tree_height: int = -1, first_time: bool = True) -> bool:
  """
    Check if the tree at x, y can be seen from the right

    returns True if the tree is taller than the tree to the right of it
  """
  
  # if y = len(tree_matrix[x]) - 1, then we are at the right
  if y == len(tree_matrix[x]) - 1: return True

  # original tree height is the height of the first tree in the recursive loop
  if original_tree_height == -1: original_tree_height = tree_matrix[x][y]

  if first_time:
    return tree_matrix[x][y] > tree_matrix[x][y + 1] and check_right(tree_matrix, x, y + 1, original_tree_height, False)
  else:
    return original_tree_height > tree_matrix[x][y] and check_right(tree_matrix, x, y + 1, original_tree_height, False)

def check_left(tree_matrix, x: int, y: int, original_tree_height: int = -1, first_time: bool = True) -> bool:
  """
    Check if the tree at x, y can be seen from the left

    returns True if the tree is taller than the tree to the left of it
  """
  
  # if y = 0, then we are at the left
  if y == 0: return True

  # original tree height is the height of the first tree in the recursive loop
  if original_tree_height == -1: original_tree_height = tree_matrix[x][y]

  if first_time:
    return tree_matrix[x][y] > tree_matrix[x][y - 1] and check_left(tree_matrix, x, y - 1, original_tree_height, False)
  else:
    return original_tree_height > tree_matrix[x][y] and check_left(tree_matrix, x, y - 1, original_tree_height, False)

def can_be_seen(tree_matrix, x, y) -> bool:
  return check_top(tree_matrix, x, y) or check_bottom(tree_matrix, x, y) or check_right(tree_matrix, x, y) or check_left(tree_matrix, x, y)

def count_visible_trees(tree_matrix) -> int:
  count = 0
  for x in range(len(tree_matrix)):
    for y in range(len(tree_matrix[x])):
      count += can_be_seen(tree_matrix, x, y)
  return count

def main():
  tree_matrix = get_data()
  visible_trees = count_visible_trees(tree_matrix)
  print(visible_trees)

if __name__ == '__main__':
  main()