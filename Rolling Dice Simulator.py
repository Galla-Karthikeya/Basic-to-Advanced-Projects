import random
dices = [i for i in range(1,7) for j in range(2)]
random.shuffle(dices)
data = {}


def sendoff(username, flag):
    print(f'\nHii {username}')
    if flag == 1:
        return "Thanks for Playing the Game. \nVist Again."
    else:
        return 'Thank You, Visit Again.'


def game(name, turn, username):
    if data[name] == 1:
        return username if name == 'Bot' else 'Bot', 'lost'
    if (data[name] == 0):
        return name, 'win'
        
    print(f'{name} Turn: ')
    x, y = random.sample(dices, 2)
    print(f'The Dice are: {x},{y}')
    sum = x + y
    print(data[name], sum)
    if (data[name] >= sum):
        data[name] -= sum
        print(f"{name}: Total is {data[name]}\n")
    else:
        print(f"{name} cannot subtract the dice sum ({sum}) from their total.\n")
    
    turn += 1
    next_name = 'Bot' if turn%2 == 0 else username
    return game(next_name, turn, username)

    
def startgame(username):
    turn = 1
    winner = game(username, turn, username)
    return winner


if __name__ == '__main__':
    flag = 0
    rank = 0
    username = input("Enter Your Name: ").title()
    que = input("Do you want to start the game (Yes/No): ").lower()
    if que == 'yes':
        flag = 1
        data[username] = 100
        data['Bot'] = 100
        player, rank = startgame(username)
        if rank == 'win':
            print(f'The Winner is: {player}')
        else:
            print(f'{player} Lost the Game')
    else:
        player = username
    print(sendoff(player, flag))