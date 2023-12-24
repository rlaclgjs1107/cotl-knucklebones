PLAYER_ONE_PRINT = """
  0   1   2
+---+---+---+
| {b02} | {b12} | {b22} |       dice
+---+---+---+       +---+
| {b01} | {b11} | {b21} |       | {d} |
+---+---+---+       +---+
| {b00} | {b10} | {b20} |
+---+---+---+
 {l0:2d}  {l1:2d}  {l2:2d}  {t:3d}
"""

VS_PRINT = "      vs"

PLAYER_TWO_PRINT = """
 {l0:2d}  {l1:2d}  {l2:2d}  {t:3d}
+---+---+---+
| {b02} | {b12} | {b22} |       dice
+---+---+---+       +---+
| {b01} | {b11} | {b21} |       | {d} |
+---+---+---+       +---+
| {b00} | {b10} | {b20} |
+---+---+---+
  0   1   2
"""

UI_PRINT = """
Player {playing_player_no}'s turn
Available line: {available_lines}
Choose line to place the dice:
> 
"""
