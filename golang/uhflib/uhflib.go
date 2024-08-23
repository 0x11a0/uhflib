package uhflib

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/tarm/serial"
)

type UHFReader struct {
	port *serial.Port
}

func NewReader(comPort string, baudRate int) *UHFReader {
	c := &serial.Config{Name: comPort, Baud: baudRate, ReadTimeout: time.Second * 2}
	s, err := serial.OpenPort(c)
	if err != nil {
		log.Fatal(err)
	}
	return &UHFReader{port: s}
}

func (r *UHFReader) Connect() {
	fmt.Println("Connected to UHF Reader.")
}

func (r *UHFReader) Disconnect() {
	r.port.Close()
	fmt.Println("Disconnected from UHF Reader.")
}

func (r *UHFReader) ReadTag() string {
	reader := bufio.NewReader(r.port)
	tagData, err := reader.ReadString('\n')
	if err != nil {
		log.Println("Error reading tag:", err)
		return ""
	}
	return tagData
}

func (r *UHFReader) SetPowerLevel(dBm int) {
	cmd := fmt.Sprintf("SET_PWR %d\n", dBm)
	r.port.Write([]byte(cmd))
}

func (r *UHFReader) SetPingRate(milliseconds int) {
	cmd := fmt.Sprintf("SET_PING %d\n", milliseconds)
	r.port.Write([]byte(cmd))
}