#from project_cse111_2 import populate_main_window, calculate_moneypayment, calculate_moneysaving
from calculate_money import calculate_moneypayment, calculate_moneysaving
from pytest import approx
import pytest
import math


def test_calculate_moneypayment():
    assert calculate_moneypayment(4.5,20,200000) == approx(1265.30, abs=0.01)
    assert calculate_moneypayment(8.5,10,300000) == approx(3719.57, abs=0.01)
    assert calculate_moneypayment(6.5,30,500000) == approx(3160.34, abs=0.01)
    assert calculate_moneypayment(3.8,15,400000) == approx(2918.82, abs=0.01)
    assert calculate_moneypayment(10.5,30,100000) == approx(914.74, abs=0.01)
    
def test_calculate_moneysaving():
    assert calculate_moneysaving(4.5,20,500000) == approx(1288.25, abs=0.01)
    assert calculate_moneysaving(8.5,25,800000) == approx(775.15, abs=0.01)
    assert calculate_moneysaving(6,30,1000000) == approx(995.51, abs=0.01)
    assert calculate_moneysaving(9.4,15,1200000) == approx(3058.39, abs=0.01)
    assert calculate_moneysaving(10.5,30,2000000) == approx(794.79, abs=0.01)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])