import serial
import time

class UHFReader:
    def __init__(self, com_port, baud_rate):
        self.ser = serial.Serial(com_port, baud_rate, timeout=2)

    def connect(self):
        if self.ser.is_open:
            print(f"Connected to {self.ser.port} at {self.ser.baudrate} baud.")

    def disconnect(self):
        self.ser.close()
        print("Disconnected from UHF Reader.")

    def read_tag(self):
        try:
            response = self.ser.readline().decode('utf-8').strip()
            return response
        except serial.SerialException as e:
            print(f"Error reading from the UHF reader: {e}")
            return None

    def set_power_level(self, dBm):
        command = f'SET_PWR {dBm}\n'.encode('utf-8')
        self.ser.write(command)

    def set_ping_rate(self, milliseconds):
        command = f'SET_PING {milliseconds}\n'.encode('utf-8')
        self.ser.write(command)

if __name__ == "__main__":
    reader = UHFReader('COM4', 115200)
    reader.connect()
    tag_data = reader.read_tag()
    print(f"Tag Data: {tag_data}")
    reader.disconnect()