from game.game import GAME_STATE_END, GAME_STATE_PLAY, GAME_STATE_START, Game, Observer


class TUI(Observer):
    def __init__(self, game: Game):
        game.register(self)

    def __print_screen(self, game: Game):
        pass

    def __print_end_screen(self, game: Game):
        pass

    def update(self, game: Game):
        if game.get_state() == GAME_STATE_START:
            self.__print_screen(game)
            game.play_game()

        elif game.get_state() == GAME_STATE_PLAY:
            self.__print_screen(game)

            line_no = int(input())
            while line_no not in game.get_player_available_lines(
                game.get_current_player_no()
            ):
                line_no = int(input())

            game.player_move(
                game.get_current_player_no(),
                line_no,
            )

        elif game.get_state() == GAME_STATE_END:
            self.__print_end_screen(game)
            replay = input()
            if replay == "y":
                game.start_game()
            else:
                exit()


if __name__ == "__main__":
    game = Game()
    tui = TUI(game)
    game.start_game()
