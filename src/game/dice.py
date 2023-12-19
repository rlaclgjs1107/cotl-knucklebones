from secrets import randbelow


def is_dice_value(value: int) -> bool:
    return 1 <= value <= 6


def roll_dice() -> int:
    return randbelow(6) + 1
