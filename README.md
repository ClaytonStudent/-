# Introduce of RL-Go
This is a project help to know AlphaZero algorithm by implementation of it for game Gomoku(Five-in-a-Row).
AlphaGo Zero algorithm ideas and architecture can simply realize the artificial intelligence player of Gomoku, It continue to play Gomoku, keep training, and iteratively update itself in self-training mode, so as to train an extremely high level artificial intelligence Gomoku player.

## What we have done?
1. We have a simple user interface including board and pieces(O and X for two players).
2. We design a self-training AI model using Monte Carlo Tree Search method and policy network. 
3. We store the best model after self-training. User can play against it and and feel the power AI.

### Project structure

Board: Game board initilization, piece location and board update.
Game: Game logic and rules
Human: Human input action response.
main: entry the game
MCTS: use MCTS method run simulation and train the AI.
