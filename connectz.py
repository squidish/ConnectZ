#Code copyright Christopher Francis Williams (2020): Please do not distribute without the author's permission
#christopherfwilliams@yahoo.co.uk

import array as arr
import csv
import sys
import string 

class ConnectZ(object):

  def __init__(self, player=1,win=4,move=0,rows=6,cols=7,board=0):
    #if no board given defaults to standard game 
    if (board == 0):     
       board = [[0 for i in range(cols)] for j in range(rows)] 
       self.rows = rows
       self.cols = cols
    else:
       self.rows = len(board)
       self.cols = len(board[0])
    self.win = win
    self.move = move
    self.player = player
    position_st, mask_st = '', ''
    for j in range(self.cols-1, -1, -1):
     #sentinal row
     mask_st += '0'
     position_st += '0'
     for i in range(self.rows-1,-1,-1):
       mask_st += ['0', '1'][board[i][j] != 0]
       position_st += ['0', '1'][board[i][j] == player]
       self.pos = int(position_st, 2)
       self.ma =int(mask_st, 2) 
    #print(position_st)
    #print(mask_st)

  def PrintIntegerRep(self):
       stlen = (self.rows+1)*self.cols
       fmt = "{0:0" + str(stlen)  + "b}"
       print("Position is " + str(fmt.format(self.pos)))
       print("Position is " + str(self.pos))    
       print("Mask is "  + str(fmt.format(self.ma)))
       print("Mask is " + str(self.ma))

  def CheckForVictory(self):
       victory = False
       #horizonal, vertical,diag down, diag up
       offsets=[self.cols,1,self.cols-1,self.cols+1]  
       victory = [False,False,False,False]
       for l in range(0,4):
            #Since player has just moved position will be in terms of opponent so flip
            #m = self.pos
            m = self.pos ^ self.ma
            for k in range(0,self.win-1): 
              n = (m >> offsets[l])  
              m = m & n
              if (m):
                victory[l] = True
              else:
                victory[l] = False
       result = False
       if any(victory) == True:       
            result = True
       return result

  def OpponentPosition(self):
       stlen = (self.rows+1)*self.cols
       fmt = "{0:0" + str((self.rows+1)*self.cols)  + "b}"
       op_position = self.pos ^ self.ma
       op_string = fmt.format(op_position)
       print("Opponent Position is:")
       for j in range(0,self.rows+1):
          display = ""
          for i in range(stlen-(self.rows+1),-(self.rows+1),-(self.rows+1)):
              display += op_string[i+j]
          print(display)
       return op_position      

  def PrintPosition(self,filename):
      filename.write("The Player "+ str(self.player) + " position is: \n")
      fmt = "{0:0" + str((self.rows+1)*self.cols)  + "b}"
      pos_st = fmt.format(self.pos)
      stlen = (self.rows+1)*self.cols
      #print(len(pos_st))
      #print(pos_st)
      for j in range(0,self.rows+1):
        display = ""
        for i in range(stlen-(self.rows+1),-(self.rows+1),-(self.rows+1)):
            #print(i+j) 
            display += pos_st[i+j]
        filename.write(display + "\n")
      filename.write("The mask is: \n")
      mask_st = fmt.format(self.ma)
      for j in range(0,self.rows+1):
         display = ""
         for i in range(stlen-(self.rows+1),-(self.rows+1),-(self.rows+1)):
             display += mask_st[i+j]
         filename.write(display + "\n")

  def ResetBoard(self):
      fmt = "'{0:0" + str((self.rows+1)*self.cols)  + "b}'"
      blank = fmt.format(0)
      self.pos = int(blank, 2)
      self.ma = int(blank, 2)

  def MakeMove(self,play):
     #print("Player " + str(self.player) + " plays in column " + str(play+1))
     self.pos = self.pos ^ self.ma 
     self.ma =  self.ma | (self.ma + (1 << (play*(self.rows+1)))) 
     if ((self.player + 1) % 2  == 1):
        self.player = 1
     elif((self.player + 1) % 2  == 0):
        self.player = 2
     self.move += 11
  
  def CurrentPlayer(self):
    return self.player
 

#Begin Main Script Here
#----------------------
if (len(sys.argv) != 2):
   #No file abort
   print("Error 9:File Error")
   sys.exit()

#Process file
filename = str(sys.argv[1])
#print("Reading file " + str(sys.argv[1]))
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    line_count = 0
    game_moves = []
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            game_header = row
            if (len(game_header) != 3):
                print("Error 8:Invalid File")
                exit()
            line_count += 1
        else:
            if(len(row)  != 1):
                print("Error 8:Invalid File")
                exit()
            game_moves.append(int(row[0]))
            line_count += 1
    #print(f'Processed {line_count} lines.')  

#Open file for diagonstics of the simulation
outFile = open('Diagnostics.txt', 'w')

boardcols = int(game_header[0])
boardrows = int(game_header[1]) 
boardwin = int(game_header[2])
#Before we play check that the game can be won
if ((boardwin > boardrows) and  (boardwin > boardcols )):
    print("Error 7: Illegal game")
    exit()
heights = [0 for i in range(boardcols)]
#Create Board and simulate game
#board_rep = ConnectZ(player = 1, cols = int(game_header[0]), rows=int(game_header[1]),win=int(game_header[2]) )
board_rep = ConnectZ(player = 1, cols = boardcols, rows=boardrows,win=boardwin )
board_rep.PrintPosition(outFile)
for k in range(0,len(game_moves)):
    cp = board_rep.CurrentPlayer()
    outFile.write("Player " + str(cp) + " plays in column " + str(game_moves[k]) + "\n")
    if(game_moves[k] > int(game_header[0])):
       print("Error 6:Illegal Column")
       sys.exit()
    #Move valid so update heights
    heights[game_moves[k]-1] += 1
    if (heights[game_moves[k]-1] > boardrows ):
       print("Error 5:Illegal Row")
       exit() 
    board_rep.MakeMove(game_moves[k]-1)
    board_rep.PrintPosition(outFile)
    vict = board_rep.CheckForVictory()
    outFile.write("Player " + str(cp) + " won? " + str(vict) + "\n")
    if(vict == True and k == (len(game_moves)-1)):
      #Read to the end and there was a result 1 or 2
      print("A victory for player " + str(cp) + "   ")
      sys.exit()
    elif(vict == True):
      #moves after end illegal continue
      print("Error 4:Illegal continue")
      sys.exit()  
 #if there have been no illegal moves and all possibl
if(len(game_moves) == int(game_header[0])*int(game_header[1])):
   print("Game resulted in a draw 0")
   sys.exit()
#if not true then the game must have been incomplete 
print("Error 3:Game Incomplete")
#close diagnostics file
outFile.close()
