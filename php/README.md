### `README.md`

# uhflib for PHP

## Overview

**uhflib** is a PHP library designed to facilitate communication with UHF RFID readers via serial communication. It provides a simple API to connect to the reader, read tags, and control various settings such as power levels and ping rates.

## Installation

To install the library, use the following command:

```bash
composer require lucasodra/uhflib
```

## Usage

### Example: Single Scan

```php
<?php

require 'vendor/autoload.php';

use Uhflib\UHFReader;

$reader = new UHFReader('/dev/ttyUSB0', 115200);
$reader->connect();
$tagData = $reader->readTag();
echo "Tag Data: $tagData\n";
$reader->disconnect();
```

### Example: Continuous Scanning with Duplicate Removal

```php
<?php

require 'vendor/autoload.php';

use Uhflib\UHFReader;

$reader = new UHFReader('/dev/ttyUSB0', 115200);
$reader->connect();

$seenTags = [];

while (true) {
    $tagData = $reader->readTag();
    if ($tagData && !in_array($tagData, $seenTags)) {
        echo "New Tag Detected: $tagData\n";
        $seenTags[] = $tagData;
    }
    usleep(100000);  // Adjust the scan rate as needed
}

$reader->disconnect();
```

### Example: Setting Power Level

```php
<?php

require 'vendor/autoload.php';

use Uhflib\UHFReader;

$reader = new UHFReader('/dev/ttyUSB0', 115200);
$reader->connect();

// Set the power level to 30 dBm
$reader->setPowerLevel(30);

$reader->disconnect();
```

### Example: Setting Ping Rate

```php
<?php

require 'vendor/autoload.php';

use Uhflib\UHFReader;

$reader = new UHFReader('/dev/ttyUSB0', 115200);
$reader->connect();

// Set the ping rate to 5 seconds
$reader->setPingRate(5000);

while (true) {
    $tagData = $reader->readTag();
    if ($tagData) {
        echo "Tag Data: $tagData\n";
    }
    usleep(5000000);  // Adjust the ping rate as needed
}

$reader->disconnect();
```

## API Reference

- **connect()**: Establishes a connection to the UHF RFID reader.
- **disconnect()**: Closes the connection to the UHF RFID reader.
- **readTag()**: Reads data from the UHF RFID tag.
- **setPowerLevel($dBm)**: Sets the power level of the UHF RFID reader.
- **setPingRate($milliseconds)**: Sets the ping rate for tag reading.

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
