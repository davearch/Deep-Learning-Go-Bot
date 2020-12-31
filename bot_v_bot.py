from dlgo import agent
from dlgo import goboard_slow
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time


def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }

    # set a sleep timer to 0.3s so moves aren't printed too fast.
    while not game.is_over():
        time.sleep(0.3)

        # clear the screen before each move so the board is always
        # printed to the same position on the command line.
        print(chr(27) + "[2j")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == "__main__":
    main()
