"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
>>> tic_tac_toe_checker([["х", "-", "o"], ["х", "-", "o"], ["х", "o", "x"]])
'х wins!'
>>> tic_tac_toe_checker([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]])
'x wins!'
>>> tic_tac_toe_checker([["-", "-", "o"], ["x", "o", "o"], ["o", "x", "x"]])
'o wins!'
>>> tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["o", "x", "x"]])
'unfinished!'
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    for i in enumerate(board):
        if "-" in i[1]:
            unfinished = True

        if board[i[0]][0] == board[i[0]][1] == board[i[0]][1] != "-":
            return f"{i[1][0]} wins!"

        elif board[0][i[0]] == board[1][i[0]] == board[2][i[0]] != "-":
            return f"{i[1][i[0]]} wins!"

    if (board[0][0] == board[1][1] == board[2][2] != "-"
            or board[0][2] == board[1][1] == board[2][0] != "-"):
        return f"{board[1][1]} wins!"

    if unfinished:
        return "unfinished!"

    else:
        return "draw!"
