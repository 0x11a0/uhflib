package com.uhflib;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import gnu.io.CommPortIdentifier;
import gnu.io.SerialPort;
import gnu.io.SerialPortEvent;
import gnu.io.SerialPortEventListener;

public class UHFReader {
    private SerialPort serialPort;
    private InputStream inputStream;
    private OutputStream outputStream;

    public UHFReader(String comPort, int baudRate) {
        try {
            CommPortIdentifier portIdentifier = CommPortIdentifier.getPortIdentifier(comPort);
            serialPort = (SerialPort) portIdentifier.open("UHFReader", 2000);
            serialPort.setSerialPortParams(baudRate, SerialPort.DATABITS_8, SerialPort.STOPBITS_1, SerialPort.PARITY_NONE);
            inputStream = serialPort.getInputStream();
            outputStream = serialPort.getOutputStream();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void connect() {
        System.out.println("Connected to UHF Reader.");
    }

    public void disconnect() {
        try {
            serialPort.close();
            System.out.println("Disconnected from UHF Reader.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public String readTag() {
        try {
            byte[] buffer = new byte[1024];
            int length = inputStream.read(buffer);
            return new String(buffer, 0, length, StandardCharsets.UTF_8).trim();
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public void setPowerLevel(int dBm) {
        try {
            String command = "SET_PWR " + dBm + "\n";
            outputStream.write(command.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void setPingRate(int milliseconds) {
        try {
            String command = "SET_PING " + milliseconds + "\n";
            outputStream.write(command.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}