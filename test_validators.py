from CollectiblesCollection import valid_id, valid_price, valid_year

def test_valid_id():
    assert valid_id("12345") == True
    assert valid_id("abcde") == False
    assert valid_id("1234") == False
    assert valid_id("123456") == False
    assert valid_id("12a45") == False

def test_valid_price():
    assert valid_price("10.99") == True
    assert valid_price("10") == True
    assert valid_price("10.999") == False
    assert valid_price("abc") == False

def test_valid_year():
    assert valid_year("2020") == True
    assert valid_year("20200") == False
    assert valid_year("202") == False
    assert valid_year("abc") == False

    