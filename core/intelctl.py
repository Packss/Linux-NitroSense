from PyQt6.QtCore import QObject, QProcess, pyqtSignal


class CommandRunner(QObject):
    finished = pyqtSignal(str)  # Emits the full output when done

    def __init__(self):
        super().__init__()
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self._handle_output)
        self.process.finished.connect(self._on_finished)
        self.output = ""  # Store output here

    def run(self, cmd, args):
        self.output = ""  # Reset output
        self.process.start(cmd, args)
        self.process.waitForFinished()

    def _handle_output(self):
        new_output = self.process.readAllStandardOutput().data().decode()
        self.output += new_output  # Append to stored output

    def _on_finished(self):
        self.finished.emit(self.output)  # Emit the full output

    def close(self):
        self.process.close()


def checkUndervoltStatus(self):
    self.undervolt = "Undervolt not supported for this CPU type."


def applyUndervolt(self):
    self.undervolt = "Undervolt not supported for this CPU type."


voltage_process = QProcess()


def checkVoltage(self):
    ## https://askubuntu.com/questions/876286/how-to-monitor-the-vcore-voltage
    voltage_process.start("sudo rdmsr 0x198 -a -u --bitfield 47:32")  # All processors
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

