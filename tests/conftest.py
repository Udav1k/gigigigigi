import pytest


@pytest.fixture
def sample_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512357"},
        {"id": 93979555, "state": "EXECUTED", "date": "2018-06-16T12:12:02.617133"},
        {"id": 59422347, "state": "CANCELED", "date": "2019-08-26T10:50:58.294041"},
    ]
