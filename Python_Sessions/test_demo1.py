import pytest

def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"
@pytest.mark.login
def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM", "Test passed as selenium upcase is SELENIUM"

def test_m3():
    assert True

@pytest.mark.login
def test_m4():
    assert False

def test_m5():
    assert 100 == 100

@pytest.mark.login
def test_m6():
    assert "Naveen"=="Naveen"

@pytest.mark.login
def test_login():
    assert "admin"=="admin"