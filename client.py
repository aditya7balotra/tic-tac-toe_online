'''this is that of the client'''
#second player

import socket
import time
import m_tic_tac_toe as tic

# this is related to connection
ip_adrs = 'localhost'
port = 12345
adrs = (ip_adrs,port)

client = socket.socket()
print('connecting...')

try:
    client.connect(adrs)
except:
    print('network error...')
    exit()

print('connected with the server with address ',adrs)


#sending and receiving the name of players

print('getting the name of your opponent...')
plyr_2_name = client.recv(1024).decode()
print('the name of the opponnent is '+plyr_2_name)


plyr_1_name = input("Enter your name: ")
client.send(plyr_1_name.encode())

game = tic.tic_tac_toe(plyr_2_name,plyr_1_name)


# here my work with sending and receiving data starts


#defining a decoration so that it will print 'waiting for the oponnet' while he/she is making his/her move

def waiting(func):
    def inner():
        print('waiting...')
        func()
    return inner

# this method is ensuring the turn of the server or of the oponnent player
def turn_determination():
    #receiving the game board
    game.turn = 1
    board=client.recv(1024).decode()
    print(board)

    #receiving and making the move
    while True:
        #first move
        print('waiting...')
        move_plyr2 = client.recv(1024).decode()
        exec(f"game.{move_plyr2} = 'X'")
        print(game.print_board())
        if game.check_winner() == 'exit':
            client.close()
            exit()
        if game.check_draw() == 'exit':
            client.close()
            exit()

        #other moves
        move_and_board,move = game.ask_and_modify()
        client.send(move.encode())
        print(move_and_board)
        if game.check_winner() == 'exit':
            client.close()
            exit()
        if game.check_draw() == 'exit':
            client.close()
            exit()

turn_determination()
