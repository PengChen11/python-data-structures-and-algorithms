from dsa.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation as mv

def test_multi_bracket_validation_1():
    assert mv("{}")==True

def test_multi_bracket_validation_2():
    assert mv("{}(){}")==True

def test_multi_bracket_validation_3():
    assert mv("()[[Extra Characters]]")==True

def test_multi_bracket_validation_4():
    assert mv("(){}[[]]")==True

def test_multi_bracket_validation_5():
    assert mv("{}{Code}[Fellows](())")==True

def test_multi_bracket_validation_6():
    assert mv("[({}]")==False

def test_multi_bracket_validation_7():
    assert mv("(](")==False

def test_multi_bracket_validation_8():
    assert mv("{(})")==False

def test_multi_bracket_validation_9():
    assert mv("][[[][]]")==False
