from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_data):
    assert len(filter_by_state(sample_data, "EXECUTED")) == 2
    assert len(filter_by_state(sample_data, "CANCELED")) == 1
    assert filter_by_state(sample_data, "NON_EXISTENT") == []


def test_sort_by_date(sample_data):
    sorted_desc = sort_by_date(sample_data)
    assert sorted_desc[0]["id"] == 59422347  # Самая свежая дата (август 2019)

    sorted_asc = sort_by_date(sample_data, reverse=False)
    assert sorted_asc[0]["id"] == 93979555  # Самая старая дата (июнь 2018)
