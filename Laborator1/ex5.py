# Given a square matrix of characters, write a script
# that prints the string obtained by going through the
# matrix in spiral order

def spiral_trav(matrix, rows, columns):
    left = 0
    right = columns - 1
    top = 0
    bottom = rows - 1
    final_word = ""
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            final_word += matrix[top][i]
        top += 1

        for i in range(top, bottom + 1):
            final_word += matrix[i][right]
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                final_word += matrix[bottom][i]
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                final_word += matrix[i][left]
            left += 1
    return final_word


m_rows = int(input("Give number of rows: "))
m_columns = int(input("Give number of columns: "))

word_matrix = []
print("Give word matrix: ")

for i in range(m_rows):
    row = []
    for j in range(m_columns):
        row.append(input())
    word_matrix.append(row)

print(spiral_trav(word_matrix, m_rows, m_columns))
