from app import add, sub, multi, divide

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(10,4) == 6

def test_multi():
    assert multi(3,3) == 9

def test_divide():
    assert divide(10,2) == 5
