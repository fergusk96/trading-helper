from src.functions.function import first_function


def test_add():
    val = first_function(None, None)
    assert val['body'] == "Hello, World!.\n This is the first function."
