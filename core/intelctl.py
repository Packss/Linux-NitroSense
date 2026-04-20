from PyQt6.QtCore import QProcess


def checkUndervoltStatus(self):
    self.undervolt = "Undervolt not supported for this CPU type."


def applyUndervolt(self):
    self.undervolt = "Undervolt not supported for this CPU type."


voltage_process = QProcess()


def checkVoltage(self):
    ## https://askubuntu.com/questions/876286/how-to-monitor-the-vcore-voltage
    voltage_process.start("sudo rdmsr 0x198 -a -u --bitfield 47:32")
    voltage_process.waitForFinished()
    voltage = voltage_process.readAll()

    if voltage:
        data = [int(line) for line in voltage.data().decode("utf-8").splitlines()]
        # print(data)
        avg_v = sum(data) / len(data)
        voltage = int(avg_v) / 8192

        self.voltage = voltage

        if voltage < self.minrecordedVoltage:
            self.minrecordedVoltage = voltage
        if voltage > self.maxrecordedVoltage:
            self.maxrecordedVoltage = voltage
