### `README.md`

```markdown
# uhflib for JavaScript (Node.js)

## Overview

**uhflib** is a JavaScript library designed to facilitate communication with UHF RFID readers via serial communication. It provides a simple API to connect to the reader, read tags, and control various settings such as power levels and ping rates.

## Installation

To install the library, use the following command:

```bash
npm install uhflib
```

Ensure you have `serialport` installed, as it is required for serial communication.

## Usage

### Example: Single Scan

```javascript
const UHFReader = require('uhflib/UHFReader');

const reader = new UHFReader('COM4', 115200);
reader.connect();

reader.readTag((tagData) => {
    console.log("Tag Data:", tagData);
    reader.disconnect();
});
```

### Example: Continuous Scanning with Duplicate Removal

```javascript
const UHFReader = require('uhflib/UHFReader');

const reader = new UHFReader('COM4', 115200);
reader.connect();

const seenTags = new Set();

function scan() {
    reader.readTag((tagData) => {
        if (tagData && !seenTags.has(tagData)) {
            console.log("New Tag Detected:", tagData);
            seenTags.add(tagData);
        }
        setTimeout(scan, 100); // Adjust the scan rate as needed
    });
}

scan();
```

### Example: Setting Power Level

```javascript
const UHFReader = require('uhflib/UHFReader');

const reader = new UHFReader('COM4', 115200);
reader.connect();

// Set the power level to 30 dBm
reader.setPowerLevel(30);

reader.disconnect();
```

### Example: Setting Ping Rate

```javascript
const UHFReader = require('uhflib/UHFReader');

const reader = new UHFReader('COM4', 115200);
reader.connect();

// Set the ping rate to 5 seconds
reader.setPingRate(5000);

function scan() {
    reader.readTag((tagData) => {
        if (tagData) {
            console.log("Tag Data:", tagData);
        }
        setTimeout(scan, 5000); // Adjust the ping rate as needed
    });
}

scan();
```

## API Reference

- **connect()**: Establishes a connection to the UHF RFID reader.
- **disconnect()**: Closes the connection to the UHF RFID reader.
- **readTag(callback)**: Reads data from the UHF RFID tag. The `callback` function receives the tag data as a parameter.
- **setPowerLevel(dBm)**: Sets the power level of the UHF RFID reader.
- **setPingRate(milliseconds)**: Sets the ping rate for tag reading.

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