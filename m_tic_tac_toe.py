'''Here my code begins and here i am creating a tic tac toe game '''




class tic_tac_toe:
    def __init__(self,player1,player2):

        self.turn=0

        self.player1 = player1
        self.player1_sign = 'X'

        self.player2 = player2
        self.player2_sign = 'O'

        self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i = 0,1,2,3,4,5,6,7,8

        self.available_boxes=[0,1,2,3,4,5,6,7,8]

    def print_board(self):
        #this function is used to print the board of the tic tac toe game
        
        board=f'''

 {self.a} | {self.b} | {self.c}
 {self.d} | {self.e} | {self.f}
 {self.g} | {self.h} | {self.i} 
        
    '''
        return board
    
    # this method will ask for the input from the players and will further modify the values of the board
    def ask_and_modify(self):

        if self.turn == 0:
            print(f'{self.player1}\'s turn ')
            box=int(input('Enter the box number: '))
            if box in self.available_boxes:
                if box == 0:
                    self.a = self.player1_sign
                    self.move = 'a'
                elif box == 1:
                    self.b = self.player1_sign
                    self.move = 'b'
                elif box == 2:
                    self.c = self.player1_sign
                    self.move = 'c'
                elif box == 3:
                    self.d = self.player1_sign
                    self.move = 'd'
                elif box == 4:
                    self.e = self.player1_sign
                    self.move = 'e'
                elif box == 5:
                    self.f = self.player1_sign
                    self.move = 'f'
                elif box == 6:
                    self.g = self.player1_sign
                    self.move = 'g'
                elif box == 7:
                    self.h = self.player1_sign
                    self.move = 'h'
                elif box == 8:
                    self.i = self.player1_sign
                    self.move = 'i'


                self.available_boxes.remove(box)
                return self.print_board(),self.move



            else:
                print('this boxes is already taken')
                return self.ask_and_modify()

            
                        
        elif self.turn == 1:
            print(f'{self.player2}\'s turn ')
            box=int(input('Enter the box number: '))
            if box in self.available_boxes:

                if box == 0:
                    self.a = self.player2_sign
                    self.move = 'a'

                elif box == 1:
                    self.b = self.player2_sign
                    self.move = 'b'

                elif box == 2:
                    self.c = self.player2_sign
                    self.move = 'c'

                elif box == 3:
                    self.d = self.player2_sign
                    self.move = 'd'

                elif box == 4:
                    self.e = self.player2_sign
                    self.move = 'e'

                elif box == 5:
                    self.f = self.player2_sign
                    self.move = 'f'

                elif box == 6:
                    self.g = self.player2_sign
                    self.move = 'g'

                elif box == 7:
                    self.h = self.player2_sign
                    self.move = 'h'

                elif box == 8:
                    self.i = self.player2_sign
                    self.move = 'i'


                self.available_boxes.remove(box)
                return self.print_board(),self.move

                
                
                
            
            else:
                print('this boxes is already taken')
                return self.ask_and_modify()

    #i have made this function to continuously check for the winner of the game
    def check_winner(self):
        '''the winner will be one who will be successfull in makig a straign line using his/her alloted sign(X or O)
         {self.a} | {self.b} | {self.c}
         {self.d} | {self.e} | {self.f}
         {self.g} | {self.h} | {self.i} 
        '''
        row1=[self.a,self.b,self.c]
        row2=[self.d,self.e,self.f]
        row3=[self.g,self.h,self.i]

        col1 = [self.a,self.d,self.g]
        col2 = [self.b,self.e,self.h]
        col3 = [self.c,self.f,self.i]

        slash1 = [self.a,self.e,self.i]
        slash2 = [self.c,self.e,self.g]

        
        win1 = f'{self.player1} wins!' if any(all(cell == 'X' for cell in row) for row in [row1, row2, row3, col1, col2, col3, slash1, slash2]) else 'nope'
        win2 = f'{self.player2} wins!' if any(all(cell == 'O' for cell in row) for row in [row1, row2, row3, col1, col2, col3, slash1, slash2]) else 'nope'


        if win1 != 'nope' or win2 != 'nope':
            if win1 == 'nope':
                print(win2)
                
                return 'exit'
            elif win2 == 'nope':
                print(win1)
                return 'exit'
      
            
    def check_draw(self):
        if self.a != 0 and self.b != 1 and self.c != 2 and self.d != 3 and self.e != 4 and self.f != 5 and self.g != 6 and self.h != 7 and self.i != 8:
            print('\n \n---the game is draw--- \n \n')
            return 'exit'
        else:
            return None
            
