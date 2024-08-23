### `README.md`

# uhflib for C#

## Overview

**uhflib** is a C# library designed to facilitate communication with UHF RFID readers via serial communication. It provides a straightforward API for connecting to the reader, reading tags, and controlling various settings like power levels and ping rates.

## Installation

To use the `uhflib` library in your project, ensure that your environment is set up with .NET 5.0 or higher.

### Adding to Your Project

1. **Create a new project** (if you don't have one already):

   ```bash
   dotnet new console -n YourProjectName
   cd YourProjectName
   ```

2. **Add the `uhflib` library to your project**:

   Copy the `Uhflib.csproj` and `Uhflib/UHFReader.cs` files into your project, or include the library as a dependency in your project.

3. **Restore dependencies**:

   ```bash
   dotnet restore
   ```

## Usage

### Example: Single Scan

```csharp
using System;
using Uhflib;

class Program
{
    static void Main(string[] args)
    {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.Connect();
        string tagData = reader.ReadTag();
        Console.WriteLine("Tag Data: " + tagData);
        reader.Disconnect();
    }
}
```

### Example: Continuous Scanning with Duplicate Removal

```csharp
using System;
using System.Collections.Generic;
using System.Threading;
using Uhflib;

class Program
{
    static void Main(string[] args)
    {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.Connect();

        HashSet<string> seenTags = new HashSet<string>();

        while (true)
        {
            string tagData = reader.ReadTag();
            if (!string.IsNullOrEmpty(tagData) && !seenTags.Contains(tagData))
            {
                Console.WriteLine("New Tag Detected: " + tagData);
                seenTags.Add(tagData);
            }
            Thread.Sleep(100); // Adjust the scan rate as needed
        }

        reader.Disconnect();
    }
}
```

### Example: Setting Power Level

```csharp
using System;
using Uhflib;

class Program
{
    static void Main(string[] args)
    {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.Connect();

        // Set the power level to 30 dBm
        reader.SetPowerLevel(30);

        reader.Disconnect();
    }
}
```

### Example: Setting Ping Rate

```csharp
using System;
using System.Threading;
using Uhflib;

class Program
{
    static void Main(string[] args)
    {
        UHFReader reader = new UHFReader("COM4", 115200);
        reader.Connect();

        // Set the ping rate to 5 seconds
        reader.SetPingRate(5000);

        while (true)
        {
            string tagData = reader.ReadTag();
            if (!string.IsNullOrEmpty(tagData))
            {
                Console.WriteLine("Tag Data: " + tagData);
            }
            Thread.Sleep(5000); // Adjust the ping rate as needed
        }

        reader.Disconnect();
    }
}
```

## API Reference

- **Connect()**: Establishes a connection to the UHF RFID reader.
- **Disconnect()**: Closes the connection to the UHF RFID reader.
- **ReadTag()**: Reads data from the UHF RFID tag.
- **SetPowerLevel(int dBm)**: Sets the power level of the UHF RFID reader.
- **SetPingRate(int milliseconds)**: Sets the ping rate for tag reading.

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
