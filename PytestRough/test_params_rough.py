import pytest
"""
py.test test_params_rough.py -v -s --html=test_params_rough_report.html
"""
# Parameterize and test their result
@pytest.mark.parametrize("num, result", [(1, 11), (2, 22), (3, 33), (4, 44)])
def test_calculation(num, result):
    assert 11*num == result

