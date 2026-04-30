#Problem 1 -- Compound Interest Calculator

principal = float(input("What is your principal: EX 111.11: "))
interest_rate = float(input("What is your annual interest rate Ex 5 for 5%: "))
years = int(input("How many years Ex 5 for 5 years: "))

balance = principal

print(f"Principal: {principal}")
print(f"Rate (%): {interest_rate}")
print(f"Years: {years}")

for i in range(years):
    balance = balance * (1+interest_rate/100)
    print(f"Year {i}: {balance}")

print(f"Total interest earned: ${balance-principal}")






#Problem 2 -- Caesar Cipher Encoder

def caesar_encode(text,shift):
    cipher_text = ""
    for i in text:
        if i.isalpha():
            if i.isupper():
                if ord(i) + shift > 90:
                    cipher_text += chr(ord(i) + shift - 26)
                else:
                    cipher_text += chr(ord(i)+shift)
            elif i.islower():
                if ord(i) + shift > 122:
                    cipher_text += chr(ord(i) + shift - 26)
                else:
                    cipher_text += chr(ord(i)+shift)
        else:
            cipher_text += i
    return cipher_text

print(caesar_encode("Hello, World!", 3))
print(caesar_encode("abc xyz", 2))
print(caesar_encode("Python 3", 5))


# Problem 3 -- Matrix Transpose

def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        matrix_part=[]
        for a in range(len(matrix)):            
            matrix_part.append(matrix[a][i])
        new_matrix.append(matrix_part)
    return(new_matrix)

m1 = [[1, 2, 3,],[4, 5, 6]]

m2 = [[1, 2],[3, 4],[5, 6]]

print(transpose(m1))
print(transpose(m2))

# Problem 4 -- Tic-Tac-Toe Winner Checker

def check_winner(board):
    for i in range(3):
        for a in range(3):
            if board[i][a] != "X":
                break
            if board[i][a] == "X" and a == 2:
                return "X"


    for i in range(3):
        for a in range(3):
            if board[i][a] != "O":
                break
            if board[i][a] == "O" and a == 2:
                return "O"


    for i in range(3):
        for a in range(3):
            if board[a][i] != "X":
                break
            if board[a][i] == "X" and i == 2:
                return "X"


    for i in range(3):
        for a in range(3):
            print(board[i][a])
            print(a,i)
            if board[a][i] != "O":
                pass
            elif board[a][i] == "O" and i == 2:
                return "O"



    for i in range(3):
        if board[i][i] == "X" and i == 2:
            return "X"
        if board[i][i] != "X":
            i = 3

    for i in range(3):
        if board[i][i] == "O" and i == 2:
            return "O"
        if board[i][i] != "O":
            i = 3

    for i in range(3):
        if board[i-2][i-2] == "P" and i == 2:
            return "X"
        if board[i-2][i-2] != "X":
            i = 3
    for i in range(3):
        if board[i-2][i-2] == "O" and i == 2:
            return "O"
        if board[i-2][i-2] != "O":
            i = 3
    
    for i in range(3):
        for a in range(3):
            if board[i][a] == " ":
                return "Ongoing"

    return "Draw"



board1 = [["X", "X", "X"],["O", "O", " "],[" ", " ", " "]]
print(check_winner(board1))

board2 = [["X", "O", "X"],["X", "O", " "],[" ", "O", "X"]]
print(check_winner(board2))

board3 = [["X", "O", "X"],["X", "O", "O"],["O", "X", "X"]]
print(check_winner(board3))