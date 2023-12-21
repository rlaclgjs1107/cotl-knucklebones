from game.dice import is_dice_value, roll_dice


def test_is_dice_value():
    assert not is_dice_value(0)
    for i in range(1, 6):
        assert is_dice_value(i)
    assert not is_dice_value(7)


def test_roll_dice():
    for _ in range(100):
        assert is_dice_value(roll_dice())
