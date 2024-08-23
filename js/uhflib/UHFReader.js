const SerialPort = require('serialport');
const Readline = require('@serialport/parser-readline');

class UHFReader {
    constructor(comPort, baudRate) {
        this.port = new SerialPort(comPort, { baudRate: baudRate });
        this.parser = this.port.pipe(new Readline({ delimiter: '\n' }));
    }

    connect() {
        this.port.on('open', () => {
            console.log('Connected to UHF Reader.');
        });
    }

    disconnect() {
        this.port.close(() => {
            console.log('Disconnected from UHF Reader.');
        });
    }

    readTag(callback) {
        this.parser.once('data', (data) => {
            callback(data.trim());
        });
    }

    setPowerLevel(dBm) {
        this.port.write(`SET_PWR ${dBm}\n`);
    }

    setPingRate(milliseconds) {
        this.port.write(`SET_PING ${milliseconds}\n`);
    }
}

module.exports = UHFReader;