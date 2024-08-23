<?php

namespace Uhflib;

class UHFReader
{
    private $serialPort;

    public function __construct($comPort, $baudRate)
    {
        $this->serialPort = fopen($comPort, "w+b");

        if (!$this->serialPort) {
            throw new \Exception("Unable to open the COM port: $comPort");
        }

        stream_set_blocking($this->serialPort, 0);
        stream_set_timeout($this->serialPort, 2);

        // Assuming baud rate can be set by stty command
        exec("stty -F $comPort $baudRate");
    }

    public function connect()
    {
        if ($this->serialPort) {
            echo "Connected to UHF Reader.\n";
        }
    }

    public function disconnect()
    {
        if ($this->serialPort) {
            fclose($this->serialPort);
            echo "Disconnected from UHF Reader.\n";
        }
    }

    public function readTag()
    {
        if ($this->serialPort) {
            $data = stream_get_contents($this->serialPort);
            return trim($data);
        }
        return null;
    }

    public function setPowerLevel($dBm)
    {
        if ($this->serialPort) {
            $command = "SET_PWR $dBm\n";
            fwrite($this->serialPort, $command);
        }
    }

    public function setPingRate($milliseconds)
    {
        if ($this->serialPort) {
            $command = "SET_PING $milliseconds\n";
            fwrite($this->serialPort, $command);
        }
    }
}