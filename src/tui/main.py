from game.board import EMPTY
from game.game import GAME_STATE_END, GAME_STATE_PLAY, GAME_STATE_START, Game, Observer
from tui.template import PLAYER_ONE_PRINT, PLAYER_TWO_PRINT, UI_PRINT, VS_PRINT


class TUI(Observer):
    def __init__(self, game: Game):
        game.register(self)
        self.game = game

    def __print_start_screen(self, game: Game):
        print("start screen")

    def __print_screen(self, game: Game):
        state = game.get_state()
        p1_board = game.get_player_board_values(0)
        p1_line_scores = [
            game.get_player_line_score(0, i) for i in range(len(p1_board))
        ]
        p1_total_score = game.get_player_total_score(0)

        p2_board = game.get_player_board_values(1)
        p2_line_scores = [
            game.get_player_line_score(1, i) for i in range(len(p2_board))
        ]
        p2_total_score = game.get_player_total_score(1)

        if state == GAME_STATE_START:
            dice = EMPTY
        else:
            dice = game.get_dice_value()

        playing_player_no = game.get_current_player_no()

        print(
            PLAYER_ONE_PRINT.format(
                b00=p1_board[0][0] if p1_board[0][0] != EMPTY else " ",
                b01=p1_board[0][1] if p1_board[0][1] != EMPTY else " ",
                b02=p1_board[0][2] if p1_board[0][2] != EMPTY else " ",
                b10=p1_board[1][0] if p1_board[1][0] != EMPTY else " ",
                b11=p1_board[1][1] if p1_board[1][1] != EMPTY else " ",
                b12=p1_board[1][2] if p1_board[1][2] != EMPTY else " ",
                b20=p1_board[2][0] if p1_board[2][0] != EMPTY else " ",
                b21=p1_board[2][1] if p1_board[2][1] != EMPTY else " ",
                b22=p1_board[2][2] if p1_board[2][2] != EMPTY else " ",
                l0=p1_line_scores[0],
                l1=p1_line_scores[1],
                l2=p1_line_scores[2],
                d=dice if playing_player_no == 0 else " ",
                t=p1_total_score,
            )
        )
        print(VS_PRINT)
        print(
            PLAYER_TWO_PRINT.format(
                b00=p2_board[0][0] if p2_board[0][0] != EMPTY else " ",
                b01=p2_board[0][1] if p2_board[0][1] != EMPTY else " ",
                b02=p2_board[0][2] if p2_board[0][2] != EMPTY else " ",
                b10=p2_board[1][0] if p2_board[1][0] != EMPTY else " ",
                b11=p2_board[1][1] if p2_board[1][1] != EMPTY else " ",
                b12=p2_board[1][2] if p2_board[1][2] != EMPTY else " ",
                b20=p2_board[2][0] if p2_board[2][0] != EMPTY else " ",
                b21=p2_board[2][1] if p2_board[2][1] != EMPTY else " ",
                b22=p2_board[2][2] if p2_board[2][2] != EMPTY else " ",
                l0=p2_line_scores[0],
                l1=p2_line_scores[1],
                l2=p2_line_scores[2],
                d=dice if playing_player_no == 1 else " ",
                t=p2_total_score,
            )
        )

        if state == GAME_STATE_PLAY:
            print(
                UI_PRINT.format(
                    playing_player_no=playing_player_no + 1,
                    available_lines=game.get_player_available_lines(playing_player_no),
                )
            )

    def __print_end_screen(self, game: Game):
        print("winner is player", game.get_winner() + 1)

    def update(self, game: Game):
        if game.get_state() == GAME_STATE_START:
            self.__print_start_screen(game)

        elif game.get_state() == GAME_STATE_PLAY:
            self.__print_screen(game)

        elif game.get_state() == GAME_STATE_END:
            self.__print_end_screen(game)

    def main(self):
        self.game.start_game()
        replay = True
        while replay:
            self.game.play_game()
            while self.game.get_state() == GAME_STATE_PLAY:
                line_no = int(input())
                self.game.player_move(self.game.get_current_player_no(), line_no)
            replay = input("replay? y/n") == "y"


if __name__ == "__main__":
    game = Game()
    tui = TUI(game)
    tui.main()
