"""
Command to Run the test and generate the report in html format
pytest -v -s pytest_rough1.py --html=pytest_rough1_report.html

PARALLEL MODE:
pytest pytest_rough1.py -v -s n 2 --html=pytest_rough1_report.html
"""


def test_total_divisible_by_5(input_total):
    assert input_total%5 == 0

def test_total_divisible_by_10(input_total):
    assert input_total%10 == 0

def test_total_divisible_by_9(input_total):
    assert input_total%9 == 0
