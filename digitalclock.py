import sys
import time
from timeutils import get_current_time
from display import format_display
import sevseg  # Ensure sevseg.py is in the same folder.


def main():
    """Main function to run the digital clock."""
    try:
        while True:  # Main program loop.
            print('\n' * 60)  # Clear the screen.

            # Get the current time:
            hours, minutes, seconds = get_current_time()

            # Format the display string:
            display = format_display(sevseg)

            # Print the time:
            print(display)
            print()
            print("Press Ctrl-C to quit.")

            # Wait until the second changes:
            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != int(seconds):
                    break
    except KeyboardInterrupt:
        # Handle program exit gracefully.
        print("Digital Clock, by Al Sweigart al@inventwithpython.com")
        sys.exit()
