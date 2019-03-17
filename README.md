# TicTacToe

This Tic Tac Toe works for both 1 and 2 users. If you choose to play alone the CPU will decide the plays based on a tree that 
contains every possible scenario of the game. Each leaf is assigned a result that is positive if it's a CPU win, negative if 
it's a CPU loss and zero if it's undecided or a tie. Then the CPU choose the play with the best difference between positive 
results and negative results.
