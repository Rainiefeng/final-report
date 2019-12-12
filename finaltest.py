import finalmain

def test_celcius():
    assert finalmain.celcius(45) == -228
    assert finalmain.celcius(738) == 465
    assert finalmain.celcius(232.32) == -41

def test_fahrenheit():
    assert finalmain.fahrenheit(342) == 154
    assert finalmain.fahrenheit(32332) == 57736
    assert finalmain.fahrenheit(3423) == 5700

