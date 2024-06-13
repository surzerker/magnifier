# magnifier

This is a simple tool built with Python and Tkinter to help users magnify a specific area of their screen across multiple monitors. It captures the area around the cursor and enlarges it in a separate window, which can be useful for accessibility or detailed graphical work.

## Installation

Before running the Screen Magnifier App, you need to install the required Python libraries. You can install these dependencies using the following command:

```bash
pip install pillow mss
```

## Usage

To use the Screen Magnifier App, simply run the script from your command line. Make sure you are in the directory where the `magnifier.py` script is located, or provide the full path to the script:

```bash
python magnifier.py
```

The application will open a window displaying the magnified portion of the screen around your cursor. This window will update periodically to reflect the current area under the cursor. You can move this window to any position on your screen as needed.

### Features

- Real-time magnification of the area around the mouse cursor.
- Support for multiple monitor setups.
- Adjustable magnification and window size within the script.

### Configuration

You can adjust the magnification scale and the size of the magnification window by modifying the following lines in the `magnifier.py` script:

```python
scaling_factor=3  # Increase or decrease to change magnification level
window_size=300   # Adjust the size of the magnifier window
```

### Contributions

Contributions to the Screen Magnifier App are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

### License

This project is open source and available under the [MIT License](LICENSE.md).
```

