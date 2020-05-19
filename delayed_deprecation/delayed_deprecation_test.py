import warnings
import unittest
from datetime import date, timedelta

from delayed_deprecation import DelayedDeprecation


class TestDelayedDeprecation(unittest.TestCase):
    def test_raises_no_date(self):
        with self.assertRaises(ValueError):
            DelayedDeprecation("foo", "not a date")

    def test_in_past(self):
        today = date.today()

        with warnings.catch_warnings(record=True):
            # If a warning is raised it'll be an exception
            warnings.simplefilter("error")

            DelayedDeprecation("Temporary fix", today)
            DelayedDeprecation("Temporary fix", today + timedelta(days=1))
            DelayedDeprecation("Temporary fix", today + timedelta(days=400))

    def test_warning_raises(self):
        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")

            DelayedDeprecation("Temporary fix", date(2000, 2, 1))
            DelayedDeprecation("Temporary fix", date(2000, 3, 2), "Bob")

        self.assertEqual(len(caught_warnings), 2)
        self.assertEqual(caught_warnings[0].category, DeprecationWarning)
        self.assertEqual(
            str(caught_warnings[0].message),
            '"Temporary fix" to be reconsidered on 2000-02-01 is overdue.',
        )
        self.assertEqual(
            str(caught_warnings[1].message),
            '"Temporary fix" to be reconsidered on 2000-03-02 is overdue. Owner of this task: Bob',
        )


if __name__ == "__main__":
    unittest.main()
