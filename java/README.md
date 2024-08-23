### `README.md`

```markdown
# uhflib for Java

## Overview

**uhflib** is a Java library designed to facilitate communication with UHF RFID readers via serial communication. It provides a straightforward API for connecting to the reader, reading tags, and controlling various settings like power levels and ping rates.

## Installation

### Maven

Add the following dependency to your `pom.xml` file:

```xml
<dependency>
    <groupId>com.github.lucasodra</groupId>
    <artifactId>uhflib</artifactId>
    <version>1.0.0</version>
</dependency>
```

### Manual Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lucasodra/uhflib.git
    ```

2. Navigate to the `java` directory:

    ```bash
    cd uhflib/java
    ```

3. Build the project using Maven:

    ```bash
    mvn clean install
    ```

## Usage

### Example: Single Scan

```java
import com.uhflib.UHFReader;

public class Main {
    public static void main(String[] args) {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.connect();
        String tagData = reader.readTag();
        System.out.println("Tag Data: " + tagData);
        reader.disconnect();
    }
}
```

### Example: Continuous Scanning with Duplicate Removal

```java
import com.uhflib.UHFReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.connect();

        Set<String> seenTags = new HashSet<>();

        while (true) {
            String tagData = reader.readTag();
            if (tagData != null && !seenTags.contains(tagData)) {
                System.out.println("New Tag Detected: " + tagData);
                seenTags.add(tagData);
            }
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        reader.disconnect();
    }
}
```

### Example: Setting Power Level

```java
import com.uhflib.UHFReader;

public class Main {
    public static void main(String[] args) {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.connect();

        // Set the power level to 30 dBm
        reader.setPowerLevel(30);

        reader.disconnect();
    }
}
```

### Example: Setting Ping Rate

```java
import com.uhflib.UHFReader;

public class Main {
    public static void main(String[] args) {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.connect();

        // Set the ping rate to 5 seconds
        reader.setPingRate(5000);

        while (true) {
            String tagData = reader.readTag();
            if (tagData != null) {
                System.out.println("Tag Data: " + tagData);
            }
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        reader.disconnect();
    }
}
```

## API Reference

- **connect()**: Establishes a connection to the UHF RFID reader.
- **disconnect()**: Closes the connection to the UHF RFID reader.
- **readTag()**: Reads data from the UHF RFID tag.
- **setPowerLevel(int dBm)**: Sets the power level of the UHF RFID reader.
- **setPingRate(int milliseconds)**: Sets the ping rate for tag reading.

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