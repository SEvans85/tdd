from fuel import convert, gauge
import pytest

def test_convert_float():
    assert convert("3/4") == 75

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("4/3")

def test_convert_zerovaluerrror():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge_1():
    assert gauge(1) == "E"

def test_gauge_prints_percent():
    assert gauge(50) == "50%"

def test_gauge_100():
    assert gauge(99) == "F"
