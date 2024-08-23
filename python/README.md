### `README.md`

```markdown
# uhflib for Python

## Overview

**uhflib** is a Python library designed to facilitate communication with UHF RFID readers via serial communication. It provides a simple API to connect to the reader, read tags, and control various settings such as power levels and ping rates.

## Installation

To install the library, use the following command:

```bash
pip install git+https://github.com/lucasodra/uhflib.git
```

Ensure you have `pyserial` installed, as it is required for serial communication.

## Usage

### Example: Single Scan

```python
from uhflib import UHFReader

reader = UHFReader('COM4', 115200)
reader.connect()
tag_data = reader.read_tag()
print(f"Tag Data: {tag_data}")
reader.disconnect()
```

### Example: Continuous Scanning with Duplicate Removal

```python
from uhflib import UHFReader
import time

reader = UHFReader('COM4', 115200)
reader.connect()

seen_tags = set()

while True:
    tag_data = reader.read_tag()
    if tag_data and tag_data not in seen_tags:
        print(f"New Tag Detected: {tag_data}")
        seen_tags.add(tag_data)
    time.sleep(0.1)  # Adjust the scan rate as needed

reader.disconnect()
```

### Example: Setting Power Level

```python
from uhflib import UHFReader

reader = UHFReader('COM4', 115200)
reader.connect()

# Set the power level to 30 dBm
reader.set_power_level(30)

reader.disconnect()
```

### Example: Setting Ping Rate

```python
from uhflib import UHFReader
import time

reader = UHFReader('COM4', 115200)
reader.connect()

# Set the ping rate to 5 seconds
reader.set_ping_rate(5000)

while True:
    tag_data = reader.read_tag()
    if tag_data:
        print(f"Tag Data: {tag_data}")
    time.sleep(5)  # Adjust the ping rate as needed

reader.disconnect()
```

## API Reference

- **connect()**: Establishes a connection to the UHF RFID reader.
- **disconnect()**: Closes the connection to the UHF RFID reader.
- **read_tag()**: Reads data from the UHF RFID tag.
- **set_power_level(dBm)**: Sets the power level of the UHF RFID reader.
- **set_ping_rate(milliseconds)**: Sets the ping rate for tag reading.

## Contribution

We welcome contributions from the community! Please follow these steps:

1. **Fork the repository.**
2. **Create a feature branch:** `git checkout -b feature/YourFeature`
3. **Commit your changes:** `git commit -m 'Add YourFeature'`
4. **Push to the branch:** `git push origin feature/YourFeature`
5. **Open a Pull Request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` provides a detailed guide for using the Python implementation of `uhflib`, including installation instructions, usage examples, and an API reference. It should help developers quickly integrate UHF RFID functionality into their Python applications.