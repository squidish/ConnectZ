
# Connect Z: Game analyser

Represents games of Connect 4 generalised to an arbitarily sized frame and win condition.


# To Run

Python version 3 required

python3 connectz.py tests/Input.txt >> Results.txt

Diagnostics will be output to Diagnostics.txt


# Input format

X Y Z
1 
2
3
4

X = Width of frame
Y = Length of frame
Z = Minimum number of counters in a straight needed to win the game

The numbers below X,Y,Z represent the columns where a counter is inserted by alternating players, assuming that player 1 goes first. 

See the contents of the directory ./test for examples and tests. Run the bash script ./runtests.sh

# Board Representation

The most efficient representation of the connect z board is a bitboard representation 
where the position of counters is represented by the position of 1s and 0s in 
the binary representation of an integer. This allows for efficient querying of board 
states. A good explanation of this can be found here. 
 
https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0

The algorithm in the method CheckForVictory() of the ConnectZ object is a generalisation of the algorithm in the function connected_four(position) in this post. 
