using System;
using System.IO.Ports;

namespace Uhflib
{
    public class UHFReader
    {
        private SerialPort serialPort;

        public UHFReader(string comPort, int baudRate)
        {
            serialPort = new SerialPort(comPort, baudRate)
            {
                Parity = Parity.None,
                DataBits = 8,
                StopBits = StopBits.One,
                Handshake = Handshake.None
            };
        }

        public void Connect()
        {
            serialPort.Open();
            Console.WriteLine("Connected to UHF Reader.");
        }

        public void Disconnect()
        {
            serialPort.Close();
            Console.WriteLine("Disconnected from UHF Reader.");
        }

        public string ReadTag()
        {
            return serialPort.ReadLine();
        }

        public void SetPowerLevel(int dBm)
        {
            serialPort.WriteLine($"SET_PWR {dBm}");
        }

        public void SetPingRate(int milliseconds)
        {
            serialPort.WriteLine($"SET_PING {milliseconds}");
        }
    }
}