''' this is that of the server'''
#first player

import socket
import time
import m_tic_tac_toe as tic


#this is related to connection
#replace the localhost by the respective ip_address
ip_adrs = 'localhost'
port = 12345
adrs = (ip_adrs,port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('searching...')
try:
    server.bind(adrs)
except:
    print('network error...')
    exit()
server.listen(2)
plyr2,adrs = server.accept()
print(f'connected with {adrs}')

#sending and receiving the name of players

plyr_1_name = input("Enter your name: ")
plyr2.send(plyr_1_name.encode())

print('getting the name of your opponent...')
plyr_2_name = plyr2.recv(1024).decode()
print('the name of the opponnent is '+plyr_2_name)

game = tic.tic_tac_toe(plyr_1_name,plyr_2_name)



# here my work with sending and receiving data starts


#defining a decoration so that it will print 'waiting for the oponnet' while he/she is making his/her move

def waiting(func):
    def inner():
        print('waiting...')
        func()
    return inner

# this method is ensuring the turn of the server or of the oponnent player
def  turn_determination():
    game.turn = 0
    #sending the game board
    print(game.print_board())
    plyr2.send(game.print_board().encode())

    #making and receiving the move
    while True:

        #first move
        move_and_board,move = game.ask_and_modify()
        plyr2.send(move.encode())
        print(move_and_board)
        
        if game.check_winner() == 'exit':
            plyr2.close()
            server.close()
            exit()
        if game.check_draw() == 'exit':
            plyr2.close()
            server.close()
            exit()


        #other moves

        print('waiting...')
        move_plyr2 = plyr2.recv(1024).decode()
        exec(f"game.{move_plyr2} = 'O'")
        print(game.print_board())
        if game.check_winner() == 'exit':
            plyr2.close()
            server.close()
            exit()
        if game.check_draw() == 'exit':
            plyr2.close()
            server.close()
            exit()
        

        
turn_determination()
