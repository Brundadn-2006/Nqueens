from tkinter import *
from tkinter import messagebox

def is_safe(board, row, col, n):
    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, col + 1, n):
                return True

            board[row][col] = 0

    return False

def display_board(board):
    for widget in frame.winfo_children():
        widget.destroy()

    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                text = "Q"
            else:
                text = ""

            Label(frame,
                  text=text,
                  width=4,
                  height=2,
                  relief="solid",
                  font=("Arial", 16)).grid(row=i, column=j)

def solve_nqueen():
    try:
        n = int(entry.get())

        if n < 4:
            messagebox.showinfo("Error", "Enter N = 4 or greater")
            return

        board = [[0] * n for _ in range(n)]

        if solve(board, 0, n):
            display_board(board)
        else:
            messagebox.showinfo("Result", "No Solution Found")

    except ValueError:
        messagebox.showinfo("Error", "Enter a valid number")

# GUI
root = Tk()
root.title("N-Queen Solver")
root.geometry("600x600")

Label(root, text="N-Queen Problem", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Enter N:").pack()

entry = Entry(root)
entry.pack()

Button(root, text="Solve", command=solve_nqueen).pack(pady=10)

frame = Frame(root)
frame.pack()

root.mainloop()