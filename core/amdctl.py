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
    runner = CommandRunner()
    runner.run("amdctl", ["-m", "-g", "-c0"])
    underVoltStatus = runner.output
    # remove the first 3 lines which are not needed
    underVoltStatus = underVoltStatus.splitlines()[3:]
    # we only want column 0, 5, 6, 7, 10 and 11
    underVoltStatus = '\n'.join(f"{l[0]}\t{l[5]}\t{l[6].replace('.00', '')}\t{l[7]}\t{l[11]}" for l in (line.split() for line in underVoltStatus) if len(l) > 11)

    self.undervolt = underVoltStatus


# Apply the undervoltage offsets values
def applyUndervolt(self):
    runner = CommandRunner()
    core = self.undervolt_dropdown.currentIndex()
    vid = core * 16
    if vid == 0:
        vid = 1
    runner.run("amdctl", ["-m", f"-v{vid}"])
    checkUndervoltStatus(self)


# Global process better perf instead of creating and destroying every update cycle.
# Update the current VCore
voltage_process = CommandRunner()
def checkVoltage(self):
    voltage_process.run("amdctl", ["-g", "-c0"])
    voltage = voltage_process.output
    voltages = []
    for line in voltage:
        if "mV" in line:
            line = line.split(" ")
            for comp in line:
                if "mV" in comp:
                    voltages.append(int(comp.replace("mV", "")) / 1000)

    if voltages:
        avg_v = sum(voltages) / len(voltages)

        self.voltage = avg_v

        if avg_v < self.minrecordedVoltage:
            self.minrecordedVoltage = avg_v
        if avg_v > self.maxrecordedVoltage:
            self.maxrecordedVoltage = avg_v
