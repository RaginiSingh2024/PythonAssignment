#Matrix Addition
def matrix_addition(matrix1, matrix2):
  """Performs matrix addition."""
  rows = len(matrix1)
  cols = len(matrix1[0])
  result = [[0 for _ in range(cols)] for _ in range(rows)]
  for i in range(rows):
    for j in range(cols):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result
