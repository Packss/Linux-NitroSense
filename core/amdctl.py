from core import CommandRunner


def checkUndervoltStatus(self):
    runner = CommandRunner()
    runner.run("amdctl", ["-m", "-g", "-c0"])
    under_volt_status = runner.output
    under_volt_status = under_volt_status.splitlines()[3:]
    under_volt_status = "\n".join(
        f"{l[0]}\t{l[5]}\t{l[6].replace('.00', '')}\t{l[7]}\t{l[11]}"
        for l in (line.split() for line in under_volt_status)
        if len(l) > 11
    )
    self.undervolt = under_volt_status

def applyUndervolt(self):
    runner = CommandRunner()
    core = self.undervolt_dropdown.currentIndex()
    vid = core * 16
    if vid == 0:
        vid = 1
    runner.run("amdctl", ["-m", f"-v{vid}"])
    checkUndervoltStatus(self)

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
