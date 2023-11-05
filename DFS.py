def SafeColumnPosition(board, row, column):
    # Kiểm tra xem có thể đặt quân hậu tại board[row][col] không
    
    # Kiểm tra cùng cột
    i = row
    while i >= 0:
        if board[i][column] == 1:
            return False
        i -= 1

    for k in range(row + 1, len(board)):
        if board[k][column] == 1:
            return False

    return True

def SafePosition(board, row, column):
    # Kiểm tra xem có thể đặt quân hậu tại board[row][col] không

    # Kiểm tra cùng hàng
    for j in range(column):
        if board[row][j] == 1:
            return False

    # Kiểm tra đường chéo trái trên
    i, j = row, column
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Kiểm tra đường chéo trái dưới
    i, j = row + 1, column - 1
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def SolveNQueens(board, column):
    # Kiểm tra vị trí đặt thêm 1 quân hậu ở các cột đã có 1 quân hậu trước đó
    oneQueenInOneColumn = True
    for j in range(column):
        for i in range(len(board)):
            if SafeColumnPosition(board, i, j):
                board[i][j] = 1     # Đặt quân hậu vào ô này
                oneQueenInOneColumn = False

    if oneQueenInOneColumn:
        for row in range(len(board)):
            if SafePosition(board, row, column):
                board[row][column] = 1     # Đặt quân hậu vào ô này

                # Điều kiện dừng của đệ quy: đã đặt được quân hậu vào cột cuối cùng
                if column == len(board) - 1:
                    return True
                        
                # Đệ quy để tiếp tục đặt quân hậu vào cột tiếp theo
                if SolveNQueens(board, column + 1):
                    return True

                # Nếu không tìm được giải pháp tại đây, quay lui và thử lại
                board[row][column] = 0

    # Nếu không có cách để đặt quân hậu an toàn trong cột này, trả về False
    return False

def PrintBoard(board):
    for row in board:
        print(" ".join(map(str, row)))      # In kết quả ra màn hình

def SolveNQueensMain(N):
    board = [[0] * N for _ in range(N)]
    if SolveNQueens(board, 0):
        print("Solution found with DFS:", N, "Queens")
        if N <= 10:
            PrintBoard(board)
        resultString = ""
        for j in range(N):
            for i in range(N):
                if board[i][j] == 1:
                    resultString += str(i)
                    if j < N - 1:
                        resultString += "-"
                    break
        print(resultString)     # Chuỗi kết quả cho quân hậu nằm ở hàng i (0 <= i <= N - 1) từ cột 0 đến cột N - 1

    else:
        print("No solution exists with DFS:", N, "Queens")

if __name__ == "__main__":
    N = 18      # Số lượng quân hậu và kích thước bàn cờ
    SolveNQueensMain(N)
