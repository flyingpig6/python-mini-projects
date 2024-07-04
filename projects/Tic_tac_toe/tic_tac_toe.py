# 初始设置
board_template = '''
  0 | 1 | 2
  {0} | {1} | {2}
 -----------
 3 | 4 | 5
  {3} | {4} | {5}
 -----------
  6 | 7 | 8
  {6} | {7} | {8}
'''

win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # 横排
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # 竖排
    (0, 4, 8), (2, 4, 6)             # 斜线
]

def check_win(squares, player):
    for a, b, c in win_conditions:
        if squares[a] == squares[b] == squares[c] == player:
            return True
    return False

def print_board(squares):
    print(board_template.format(*squares))

def main():
    squares = [' '] * 9
    players = 'XO'
    
    while True:
        print_board(squares)
        if check_win(squares, players[1]):
            print(f'{players[1]} is the winner!')
            break
        if ' ' not in squares:
            print('Cats game!')
            break
        move = input(f'{players[0]} to move [0-8] > ')
        if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
            print('Invalid move!')
            continue
        squares[int(move)], players = players[0], players[::-1]

if __name__ == "__main__":
    main()

    