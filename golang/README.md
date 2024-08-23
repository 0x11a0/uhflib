### `README.md`

```markdown
# uhflib for Go

## Overview

**uhflib** is a Go library designed to facilitate communication with UHF RFID readers via serial communication. It provides a simple API to connect to the reader, read tags, and control various settings such as power levels and ping rates.

## Installation

To install the library, use the following command:

```bash
go get github.com/lucasodra/uhflib
```

Ensure you have the `github.com/tarm/serial` package installed, as it is required for serial communication.

## Usage

### Example: Single Scan

```go
package main

import (
    "fmt"
    "github.com/lucasodra/uhflib"
)

func main() {
    reader := uhflib.NewReader("COM4", 115200)
    reader.Connect()
    tagData := reader.ReadTag()
    fmt.Println("Tag Data:", tagData)
    reader.Disconnect()
}
```

### Example: Continuous Scanning with Duplicate Removal

```go
package main

import (
    "fmt"
    "time"
    "github.com/lucasodra/uhflib"
)

func main() {
    reader := uhflib.NewReader("COM4", 115200)
    reader.Connect()

    seenTags := make(map[string]bool)

    for {
        tagData := reader.ReadTag()
        if tagData != "" && !seenTags[tagData] {
            fmt.Println("New Tag Detected:", tagData)
            seenTags[tagData] = true
        }
        time.Sleep(100 * time.Millisecond)
    }

    reader.Disconnect()
}
```

### Example: Setting Power Level

```go
package main

import (
    "github.com/lucasodra/uhflib"
)

func main() {
    reader := uhflib.NewReader("COM4", 115200)
    reader.Connect()

    // Set the power level to 30 dBm
    reader.SetPowerLevel(30)

    reader.Disconnect()
}
```

### Example: Setting Ping Rate

```go
package main

import (
    "time"
    "github.com/lucasodra/uhflib"
)

func main() {
    reader := uhflib.NewReader("COM4", 115200)
    reader.Connect()

    // Set the ping rate to 5 seconds
    reader.SetPingRate(5000)

    for {
        tagData := reader.ReadTag()
        if tagData != "" {
            fmt.Println("Tag Data:", tagData)
        }
        time.Sleep(5 * time.Second)
    }

    reader.Disconnect()
}
```

## API Reference

- **Connect()**: Establishes a connection to the UHF RFID reader.
- **Disconnect()**: Closes the connection to the UHF RFID reader.
- **ReadTag()**: Reads data from the UHF RFID tag.
- **SetPowerLevel(dBm int)**: Sets the power level of the UHF RFID reader.
- **SetPingRate(milliseconds int)**: Sets the ping rate for tag reading.

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