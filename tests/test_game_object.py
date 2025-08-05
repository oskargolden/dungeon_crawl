from game_logic.game_object import GameObject


game_obj1 = GameObject('test_object', 'T', 'This is a test object')


def test_game_object():
    assert type(game_obj1.name) is str
    assert type(game_obj1.symbol) is str
    assert type(game_obj1.description) is str


def test_game_object_repr():
    """
    Tests that the string representation of the GameObject is correct.
    """
    expected_repr = (
        "GameObject(name='test_object', symbol='T', "
        "description='This is a test object')"
    )

    assert repr(game_obj1) == expected_repr
