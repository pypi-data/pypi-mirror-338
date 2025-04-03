from pytest import approx, mark

import bricoleur as bric


@mark.parametrize(
    "total_rise, max_riser_height, expected",
    [
        (77.5, 7, 12),
        (77, 7, 11),
        (100, 7.5, 14)
    ],
)
def test_number_risers(total_rise, max_riser_height, expected):
    result = bric.number_risers(
        total_rise=total_rise, max_riser_height=max_riser_height
    )
    assert result == expected


@mark.parametrize(
    "total_rise, number_risers, expected",
    [
        (100, 14, 7.142857142857143)
    ],
)
def test_riser_height(total_rise, number_risers, expected):
    result = bric.riser_height(
        total_rise=total_rise, number_risers=number_risers
    )
    assert result == expected


@mark.parametrize(
    "number_risers, tread_depth, expected",
    [
        (14, 11, 143)
    ],
)
def test_total_run(number_risers, tread_depth, expected):
    result = bric.total_run(
        number_risers=number_risers, tread_depth=tread_depth
    )
    assert result == expected
