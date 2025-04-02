"""
Function for stair calculations
"""

import math


def number_risers(
    total_rise: float,
    max_riser_height: float
    ) -> float:
    """
    Calculate the number of risers (steps) between the upper and lower finish
    levels.

    Parameters
    ----------
    total_rise : float
        The vertical distance between the finished flooring of the upper and
        the lower levels.
    max_riser_height : float
        The maximum riser height (usually from the building code).

    Returns
    -------
    no_risers
        The number of risers.

    Example
    -------

    >>> import bricoleur as bric
    >>> total_rise_datum = 100
    >>> max_riser_height_datum = 7.5
    >>> number_risers = bric.number_risers(
    >>>     total_rise = total_rise_datum,
    >>>     max_riser_height = max_riser_height_datum
    >>> )
    >>> print(number_risers)
    14

    """
    no_risers = math.ceil(total_rise / max_riser_height)
    return no_risers


def riser_height(
    total_rise: float,
    number_risers: int
    ) -> float:
    """
    Calculate the exact riser height.

    Parameters
    ----------
    total_rise : float
        The vertical distance between the finished flooring of the upper and
        the lower levels.
    number_risers : int
        The maximum riser height (usually from the building code).

    Returns
    -------
    riser_height
        The riser height.

    Example
    -------

    >>> import bricoleur as bric
    >>> total_rise_datum = 100
    >>> number_risers_datum = 14
    >>> riser_height = bric.riser_height(
    >>>     total_rise = total_rise_datum,
    >>>     number_risers = number_risers_datum
    >>> )
    >>> print(riser_height)
    7.142857142857143
    """
    riser_height = total_rise / number_risers
    return riser_height


__all__ = (
    "number_risers",
    "riser_height"
)
