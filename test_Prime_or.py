import pytest

import Prime_or

@pytest.mark.parametrize("a, b", [(13,True), (4,False), (7,True), (8,True), (21, True), (17, True)])
def test_prime_num_or_not(a, b):
    Res = Prime_or.Prime_or_Not(a)
    assert Res == b