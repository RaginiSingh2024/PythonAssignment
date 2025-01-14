#Matrix Transpose
def matrix_transpose(matrix):
  """Finds the transpose of a matrix."""
  rows = len(matrix)
  cols = len(matrix[0])
  result = [[0 for _ in range(rows)] for _ in range(cols)]
  for i in range(rows):
    for j in range(cols):
      result[j][i] = matrix[i][j]
  return result