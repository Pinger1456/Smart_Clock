# Digital Clock Project

This is a Python-based digital clock application that uses a **seven-segment display** style to represent the current time in the console. The project is modular, making it easy to extend and test individual components.

---

## Features

- Displays the current time in **HH:MM:SS** format.
- Uses a **seven-segment display** to represent digits in a visually appealing style.
- Modular code structure:
  - `timeutils.py`: Handles time-related utilities.
  - `display.py`: Formats the time for display.
  - `sevseg.py`: Generates the seven-segment display representation.
- Includes a comprehensive suite of **unit tests** to ensure code reliability.
- PEP8, Pylint, and Flake8 compliant.

---

## Directory Structure

```
project/
│
├── main.py             # Entry point to run the digital clock.
├── timeutils.py        # Handles time fetching and formatting.
├── display.py          # Formats and displays the time.
├── sevseg.py           # Generates seven-segment string representations.
├── requirements.txt    # Dependencies file (currently empty, uses built-in libraries).
├── tests/              # Unit tests for all modules.
│   ├── __init__.py
│   ├── test_timeutils.py
│   ├── test_display.py
│   ├── test_sevseg.py
└── README.md           # Project documentation.
```

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd digitalclock
   ```

2. **Optional: Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   There are no external dependencies required. All modules are from Python's standard library. However, you can still install from `requirements.txt` to ensure future compatibility:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Digital Clock**:
   Execute the `main.py` file:
   ```bash
   python main.py
   ```

---

## Running Tests

The project includes a suite of unit tests in the `tests` directory. To run all tests:

```bash
python -m unittest discover -s tests
```

---

## Modules Overview

### `timeutils.py`
Handles all time-related functionality:
- Fetches the current system time.
- Returns time as `hours`, `minutes`, and `seconds` in string format.

### `display.py`
Formats the current time into a visually appealing style using the seven-segment display provided by `sevseg.py`.

### `sevseg.py`
Generates seven-segment representations of numeric characters. For example:
```
 _ 
|_|
|_|
```

### `tests/`
Contains unit tests for each module to ensure reliability and maintainability of the project.

---

## Code Example

Here's a sample of the output from the clock:
```
  __    __   __ 
 |__|  |__| |__|
    |     |    |
```

This corresponds to **12:34:56**.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

1. Fork the project.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add YourFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Acknowledgments

- Inspiration for the seven-segment display style.
- Python’s standard library for making this project lightweight and dependency-free.
