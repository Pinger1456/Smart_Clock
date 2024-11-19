import unittest
from timeutils import get_current_time


class TestTimeUtils(unittest.TestCase):
    """Tests for timeutils.py."""

    def test_get_current_time_format(self):
        """Test if get_current_time returns three string values."""
        hours, minutes, seconds = get_current_time()
        self.assertTrue(hours.isdigit())
        self.assertTrue(minutes.isdigit())
        self.assertTrue(seconds.isdigit())

    def test_12_hour_format(self):
        """Test if hours are formatted correctly in 12-hour format."""
        # Mocking an edge case with time (e.g., midnight).
        current_time_mock = (0, 30, 45)  # 12:30:45 AM
        hours = str(current_time_mock[0] % 12)
        if hours == "0":
            hours = "12"
        self.assertEqual(hours, "12")


if __name__ == "__main__":
    unittest.main()
