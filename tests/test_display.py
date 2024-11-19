"""
Unit tests for the display module.
Tests the functionality of format_display using sevseg.
"""

import unittest
from display import format_display
import sevseg


class TestDisplay(unittest.TestCase):
    """Tests for display.py."""

    def test_format_display_output(self):
        """Test if format_display outputs a correctly formatted string."""
        hours, minutes, seconds = "12", "34", "56"
        result = format_display(sevseg)

        # Split into lines and verify structure:
        lines = result.splitlines()
        self.assertEqual(len(lines), 3)  # Top, middle, bottom rows

    def test_format_display_with_mock_sevseg(self):
        """Test format_display with a mocked sevseg module."""
        class MockSevSeg:
            """Test cases for the display module."""
            @staticmethod
            def get_sev_segstr():
                """Ensure format_display returns a well-structured string."""
                return " _ \n|_|\n|_|"

        hours, minutes, seconds = "12", "34", "56"
        result = format_display(MockSevSeg())
        self.assertIn(" _ ", result)  # Mocked sevseg behavior


if __name__ == "__main__":
    unittest.main()
