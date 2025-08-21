from src.lib.utils import add, to_title

def test_add_basic():
    assert add(2, 3) == 5

def test_to_title():
    assert to_title('hello world') == 'Hello World'
