# UART EPC CLASS UHF RFID for R200 & E200
import serial
import time

# Base class for UHF readers that provides common functionality
class UHFReaderBase:
    def __init__(self, com_port, baud_rate=115200, timeout=2):
        """
        Initialize the UHFReaderBase class with common parameters.

        Parameters:
        com_port (str): The COM port to which the UHF reader is connected (e.g., 'COM4').
        baud_rate (int): The baud rate for the serial communication (default is 115200).
        timeout (int): Timeout for serial communication in seconds (default is 2 seconds).
        """
        self.ser = None
        self.com_port = com_port
        self.baud_rate = baud_rate
        self.timeout = timeout

    def connect(self):
        """
        Establish a connection to the UHF reader via the specified COM port.
        """
        try:
            self.ser = serial.Serial(self.com_port, self.baud_rate, timeout=self.timeout)
            if self.ser.is_open:
                print(f"Connected to {self.ser.port} at {self.ser.baudrate} baud.")
            return True
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return False

    def disconnect(self):
        """
        Close the connection to the UHF reader.
        """
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Disconnected from UHF Reader.")

    def send_command(self, command, retries=3):
        """
        Send a command to the UHF reader and read the raw response.

        Parameters:
        command (bytes): The command to be sent to the UHF reader.
        retries (int): Number of retries in case of communication failure (default is 3).

        Returns:
        bytes: The raw response data from the UHF reader, or None if communication fails.
        """
        for attempt in range(retries):
            try:
                print(f"Sending command: {command} (Attempt {attempt + 1}/{retries})")
                self.ser.write(command)
                time.sleep(0.5)  # Allow time for response
                response = self.ser.read_all()  # Read the entire response
                if response:
                    print(f"Received response: {response.hex()}")
                    return response
                else:
                    print("No response received.")
            except serial.SerialException as e:
                print(f"Error communicating with the device: {e}")
                self.reconnect()
            time.sleep(1)  # Wait before retrying
        return None

    def reconnect(self):
        """
        Attempt to reconnect to the UHF reader in case of a communication failure.
        """
        while True:
            try:
                print(f"Attempting to reconnect to {self.com_port}...")
                self.ser = serial.Serial(self.com_port, self.baud_rate, timeout=self.timeout)
                if self.ser.is_open:
                    print(f"Reconnected to {self.com_port} at {self.baud_rate} baud.")
                    break
            except serial.SerialException as e:
                print(f"Reconnection failed: {e}")
            time.sleep(5)

    def scan(self):
        """
        Placeholder method for sending a scan command to the UHF reader.
        This method should be overridden by subclasses to provide device-specific functionality.
        """
        raise NotImplementedError("This method should be overridden by subclasses")


# Implementation for R200 UHF Reader
class R200Reader(UHFReaderBase):
    CMD_SINGLE_POLL_INSTRUCTION = 0x22

    def build_command_frame(self, command, params=[]):
        """
        Build a command frame specific to the R200 UHF reader.

        Parameters:
        command (int): The command code to send.
        params (list): Optional parameters to include in the command frame.

        Returns:
        bytes: The complete command frame to be sent to the R200 reader.
        """
        frame = [
            0xAA,  # Frame header
            0x00,  # Frame type: Command
            command,  # Command
            len(params) >> 8, len(params) & 0xFF  # Parameter length (2 bytes)
        ]
        frame.extend(params)  # Add any parameters
        frame.append(sum(frame[1:]) & 0xFF)  # Checksum
        frame.append(0xDD)  # Frame end
        return bytes(frame)

    def scan(self):
        """
        Send a scan command to the R200 reader and return the raw response.

        Users can modify the scan command or parameters by editing the command
        or using additional methods in the class to build custom commands.
        """
        command_frame = self.build_command_frame(self.CMD_SINGLE_POLL_INSTRUCTION)
        return self.send_command(command_frame)


# Implementation for E200 UHF Reader
class E200Reader(UHFReaderBase):
    SCAN_COMMAND = b'\x55\x00\x07\x97\x83\x03\x01\x07\x08\x00\xc2\x0d'

    def scan(self):
        """
        Send a scan command to the E200 reader and return the raw response.

        Users can modify the scan command by changing the SCAN_COMMAND attribute
        or creating new methods to handle custom commands and return raw data.
        """
        return self.send_command(self.SCAN_COMMAND)


# Example usage
if __name__ == "__main__":
    # Example usage for R200Reader
    r200_reader = R200Reader(com_port='COM7')
    if r200_reader.connect():
        raw_data = r200_reader.scan()
        print(f"Raw Data (R200): {raw_data}")
        r200_reader.disconnect()

    # Example usage for E200Reader
    e200_reader = E200Reader(com_port='COM8', baud_rate=9600)
    if e200_reader.connect():
        raw_data = e200_reader.scan()
        print(f"Raw Data (E200): {raw_data}")
        e200_reader.disconnect()
