from app import TicTacToe


try:
    game = TicTacToe()
    game.run()
except Exception as ex:
    print(ex)