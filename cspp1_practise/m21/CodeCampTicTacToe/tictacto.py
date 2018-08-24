'''
Author:Viswas
Date: 24-8-2018
'''
def tic_tac_toe(game):
    '''
    Sub Function
    '''
    gammer = []
    for row in game:
        if row[0] == row[1] == row[2]:
            gammer.append(row[0])
    for i in range(0, 3):
        if game[0][i] == game[1][i] == game[2][i]:
            gammer.append(game[0][i])
    if game[0][0] == game[1][1] == game[2][2]:
        gammer.append(game[0][0])
    if game[2][0] == game[1][1] == game[0][2]:
        gammer.append(game[0][2])
    if len(gammer) == 0:
        print('draw')
        return None
    if len(gammer) == 1:
        if gammer[0] == 'x' or gammer[0] == 'o':
            print(gammer[0])
        else:
            print("invalid input")
        return gammer[0]
    else:
        print("invalid game")
        return None
def main():
    '''
    Main Function
    '''
    game = []
    for _ in range(0, 3):
        col_1 = input().split(' ')
        game.append(col_1)
    tic_tac_toe(game)
if __name__ == '__main__':
    main()