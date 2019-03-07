from datetime import date

from more_itertools import take

from kexr.utils import date_iterator
from test.util_for_test import assert_equal


def test_date_iterator_take5():
    assert_equal((date(2018, 1, 1), date(2018, 1, 2), date(2018, 1, 3), date(2018, 1, 4), date(2018, 1, 5)),
                 take(5, date_iterator(date(2018, 1, 1))))


def test_date_iterator_util():
    assert_equal((date(2018, 1, 1), date(2018, 1, 2), date(2018, 1, 3), date(2018, 1, 4), date(2018, 1, 5)),
                 date_iterator(date(2018, 1, 1), date(2018, 1, 5)))
