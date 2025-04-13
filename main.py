import sys
import os

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QTimer, QProcess, QObject, pyqtSignal
from PyQt6.QtGui import QPalette, QColor


from frontend import Ui_NitroSense
import keyboard
from ecwrite import *
import enum


CONFIG_FOLDER = "/etc/nitrosense/"

## ------------------------------##
## --Nitro EC Register Class--##
# ECState


class ECS(enum.Enum):
    GPU_FAN_MODE_CONTROL = "0x21"
    GPU_AUTO_MODE = "0x10"
    GPU_TURBO_MODE = "0x20"
    GPU_MANUAL_MODE = "0x30"
    GPU_MANUAL_SPEED_CONTROL = "0x3A"

    CPU_FAN_MODE_CONTROL = "0x22"
    CPU_AUTO_MODE = "0x04"
    CPU_TURBO_MODE = "0x08"
    CPU_MANUAL_MODE = "0x0C"
    CPU_MANUAL_SPEED_CONTROL = "0x37"

    KB_30_SEC_AUTO = "0x06"
    KB_30_AUTO_OFF = "0x00"
    KB_30_AUTO_ON = "0x1E"

    CPUFANSPEEDHIGHBITS = "0x13"
    CPUFANSPEEDLOWBITS = "0x14"
    GPUFANSPEEDHIGHBITS = "0x15"
    GPUFANSPEEDLOWBITS = "0x16"

    CPUTEMP = "0xB0"
    GPUTEMP = "0xB6"
    SYSTEMP = "0xB3"

    POWERSTATUS = "0x00"
    POWERPLUGGEDIN = "0x01"
    POWERUNPLUGGED = "0x00"

    BATTERYCHARGELIMIT = "0x03"
    BATTERYLIMITON = "0x51"
    BATTERYLIMITOFF = "0x11"

    BATTERYSTATUS = "0xC1"
    BATTERYPLUGGEDINANDCHARGING = "0x02"
    BATTERYDRAINING = "0x01"
    BATTERYOFF = "0x00"

    POWEROFFUSBCHARGING = "0x08"
    USBCHARGINGON = "0x0F"
    USBCHARGINGOFF = "0x1F"

    NITROMODE = "0x2C"
    QUIETMODE = "0x00"
    DEFAULTMODE = "0x01"
    EXTREMEMODE = "0x04"

    TRACKPADSTATUS = "0xA1"
    TRACKPADENABLED = "0x00"
    TRACKPADDISABLED = "0x04"


## ------------------------------##
## -------Nitro Fan Mode------##
# ProcessorFanState


class PFS(enum.Enum):
    Manual = 0
    Auto = 1
    Turbo = 2


## ------------------------------##
## ---------Undervolting---------##
COREOFFSET = 100  # mV
UPDATE_INTERVAL = 1000  # 1 sec interval

# Read the current undervoltage offsets

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
        self.process.waitForStarted()
        self.process.waitForFinished()
        self.process.close()

    def _handle_output(self):
        new_output = self.process.readAllStandardOutput().data().decode()
        self.output += new_output  # Append to stored output

    def _on_finished(self):
        self.finished.emit(self.output)  # Emit the full output


def checkUndervoltStatus(self):
    runner = CommandRunner()
    runner.run("amdctl", ["-m", "-g", "-c0"])
    underVoltStatus = runner.output

    underVoltStatus = underVoltStatus.splitlines()[3:]
    underVoltStatus = "\n".join(underVoltStatus)
    # print(underVoltStatus)
    self.undervolt = underVoltStatus


# Apply the undervoltage offsets values


def applyUndervolt(self):
    process = QProcess()
    core = self.undervolt_dropdown.currentIndex()
    vid = core * 16
    if vid == 0:
        vid = 1
    process.start(f"amdctl -m -v{vid}")
    process.waitForFinished()
    process.close()
    checkUndervoltStatus(self)


# Global process better perf instead of creating and destroying every update cycle.
voltage_process = QProcess()
# Update the current VCore


def checkVoltage(self):
    runner = CommandRunner()
    runner.run("amdctl", ["-g"])
    voltage = runner.output
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


## ------------------------------##
## -------Main QT Window---------##


class MainWindow(QtWidgets.QDialog, Ui_NitroSense):
    def __init__(self):
        super().__init__()
        self._initialize_variables()
        self.setupUi(self)
        self._initialize_ec_handler()
        self._initialize_ui()
        self.setUpdateUITimer()

    def _initialize_variables(self):
        self.turboEnabled = False
        self.cpufanspeed = 0
        self.gpufanspeed = 0
        self.cpuTemp = 0
        self.gpuTemp = 0
        self.sysTemp = 0
        self.voltage = 0.5
        self.underVolt = ""
        self.minrecordedVoltage = 2.0
        self.maxrecordedVoltage = 0
        self.selected_color = (255, 255, 255)
        self.powerPluggedIn = False
        self.onBatteryPower = False
        self.displayOverdrive = False
        self.nitroMode = ECS.DEFAULTMODE.value
        self.usbCharging = ECS.USBCHARGINGON.value
        self.cpuMode = ECS.CPU_AUTO_MODE.value
        self.gpuMode = ECS.GPU_AUTO_MODE.value
        self.cpuFanMode = PFS.Auto
        self.gpuFanMode = PFS.Auto
        self.KB30Timeout = ECS.KB_30_AUTO_OFF.value
        self.trackpad = ECS.TRACKPADENABLED.value
        self.batteryChargeLimit = ECS.BATTERYLIMITOFF.value

    def _initialize_ec_handler(self):
        self.ECHandler = ECWrite()
        self.ECHandler.ec_refresh()

    def _initialize_ui(self):
        checkUndervoltStatus(self)
        self.checkPowerTempFan()
        self.checkNitroStatus()
        self.kbLoadConfig()
        self.loadConfig()
        self.setupGUI()

    # ----------------------------------------------------
    # Initialise the frame, check all registers and set the appropriate widgets
    def setupGUI(self):
        # when any of the radio buttons are clicked, also save the current settings

        self.global_auto.clicked.connect(self.setDefaultMode)
        self.global_turbo.clicked.connect(self.setTurboMode)

        self.cpu_auto.clicked.connect(self.cpuauto)
        self.cpu_manual.clicked.connect(self.cpusetmanual)
        self.cpu_turbo.clicked.connect(self.cpumax)
        self.gpu_auto.clicked.connect(self.gpuauto)
        self.gpu_manual.clicked.connect(self.gpusetmanual)
        self.gpu_turbo.clicked.connect(self.gpumax)
        self.cpuManualSlider.valueChanged.connect(self.cpumanual)
        self.cpuManualSlider.setEnabled(True)
        self.gpuManualSlider.valueChanged.connect(self.gpumanual)
        self.gpuManualSlider.setEnabled(True)
        self.exit_button.clicked.connect(self.shutdown)

        self.undervolt_button.clicked.connect(lambda: applyUndervolt(self))
        self.color_button.clicked.connect(lambda: self.saveAndRun(self.kbSelectColor))
        self.apply_button.clicked.connect(lambda: self.saveAndRun(self.kbApplySettings))
        self.save_button.clicked.connect(lambda: self.saveAndRun(self.kbSaveConfig))
        self.load_button.clicked.connect(lambda: self.saveAndRun(self.kbLoadConfig))

        # Set the 30 sec backlight timer
        if self.KB30Timeout == int(ECS.KB_30_AUTO_OFF.value, 0):
            self.KBTimerCB.setChecked(False)
        else:
            self.KBTimerCB.setChecked(True)

        # Set the USB charging indicator
        if self.usbCharging == int(ECS.USBCHARGINGON.value, 0):
            self.usbChargingCB.setChecked(True)
        elif self.usbCharging == int(ECS.USBCHARGINGOFF.value, 0):
            self.usbChargingCB.setChecked(False)
        else:
            print("Error read EC register for USB Charging: " + str(self.usbCharging))

        # Set the charge limit indicator
        if self.batteryChargeLimit == int(ECS.BATTERYLIMITON.value, 0):
            self.chargeLimit.setChecked(True)
            self.batteryChargeLimitValue.setText("On ")
        elif self.batteryChargeLimit == int(ECS.BATTERYLIMITOFF.value, 0):
            self.chargeLimit.setChecked(False)
            self.batteryChargeLimitValue.setText("Off")
        else:
            print(
                "Error read EC register for Charge Limit: "
                + str(self.batteryChargeLimit)
            )

        self.setNitroMode()
        self.setFanMode()

        # ----------------------------------------------------

        self.quietModeCB.clicked["bool"].connect(self.setQuietMode)
        self.defaultModeCB.clicked["bool"].connect(self.setDefaultMode)
        self.extremeModeCB.clicked["bool"].connect(self.setExtremeMode)
        # self.trackpadCB.clicked['bool'].connect(self.toggletrackpad)
        self.KBTimerCB.clicked["bool"].connect(self.togglekbauto)
        self.usbChargingCB.clicked["bool"].connect(self.toggleUSBCharging)
        self.chargeLimit.clicked["bool"].connect(self.togglePowerLimit)

    # Set the current fan and turbo mode
    def setFanMode(self):
        if self.cpuMode == int(ECS.CPU_AUTO_MODE.value, 0):
            self.cpuFanMode = PFS.Auto
            self.cpu_auto.setChecked(True)
        elif self.cpuMode == int(ECS.CPU_TURBO_MODE.value, 0) or self.cpuMode == int(
            "0xA8", 0
        ):
            self.cpuFanMode = PFS.Turbo
            self.cpu_turbo.setChecked(True)
            self.turboEnabled = True
        elif self.cpuMode == int(ECS.CPU_MANUAL_MODE.value, 0):
            self.cpuFanMode = PFS.Manual
            self.cpu_manual.setChecked(True)
        else:
            print("Warning: Unknow CPU fan mode value '" + str(self.cpuMode) + "'")
            # self.cpuauto()

        if self.gpuMode == int(ECS.GPU_AUTO_MODE.value, 0) or self.gpuMode == int(
            "0x00", 0
        ):
            self.gpuFanMode = PFS.Auto
            self.gpu_auto.setChecked(True)
        elif self.gpuMode == int(ECS.GPU_TURBO_MODE.value, 0):
            self.gpuFanMode = PFS.Turbo
            self.gpu_turbo.setChecked(True)
        elif self.gpuMode == int(ECS.GPU_MANUAL_MODE.value, 0):
            self.gpuFanMode = PFS.Manual
            self.gpu_manual.setChecked(True)
        else:
            print("Warning: Unknow GPU fan mode value '" + str(self.gpuMode) + "'")
            # self.gpuauto()

        # if cpuTurboEnabled and gpuTurboEnabled:
        if self.turboEnabled:
            self.global_turbo.setChecked(True)
            self.cpu_turbo.setChecked(True)
            self.gpu_turbo.setChecked(True)
            self.nitroMode = int(ECS.EXTREMEMODE.value, 0)
            self.setTurboMode()

    # Create a timer to update the UI
    def setUpdateUITimer(self):
        print("Setting up callback timer for %d(ms)" % UPDATE_INTERVAL)
        self.my_timer = QTimer()
        self.my_timer.timeout.connect(self.updateNitroStatus)
        self.my_timer.start(UPDATE_INTERVAL)

    # ----------------------------------------------------
    # Read the various EC registers and update the GUI
    def checkNitroStatus(self):
        # self.cb = self.ECHandler.ec_read(int(COOL_BOOST_CONTROL, 0)) == 1
        self.cpuMode = self.ECHandler.ec_read(int(ECS.CPU_FAN_MODE_CONTROL.value, 0))
        self.gpuMode = self.ECHandler.ec_read(int(ECS.GPU_FAN_MODE_CONTROL.value, 0))
        self.KB30Timeout = self.ECHandler.ec_read(int(ECS.KB_30_SEC_AUTO.value, 0))
        self.usbCharging = self.ECHandler.ec_read(int(ECS.POWEROFFUSBCHARGING.value, 0))
        self.nitroMode = self.ECHandler.ec_read(int(ECS.NITROMODE.value, 0))
        self.batteryChargeLimit = self.ECHandler.ec_read(
            int(ECS.BATTERYCHARGELIMIT.value, 0)
        )
        self.trackpad = self.ECHandler.ec_read(int(ECS.TRACKPADSTATUS.value, 0))

        self.cpuFanSpeed = self.ECHandler.ec_read(
            int(ECS.CPU_MANUAL_SPEED_CONTROL.value, 0)
        )
        self.gpuFanSpeed = self.ECHandler.ec_read(
            int(ECS.GPU_MANUAL_SPEED_CONTROL.value, 0)
        )
        self.cpuManualSlider.setSliderPosition(int(self.cpuFanSpeed / 10))
        self.gpuManualSlider.setSliderPosition(int(self.gpuFanSpeed / 10))

    # ----------------------------------------------------
    # Read the newest register updates
    def checkPowerTempFan(self):
        # Refresh the EC registers first before reading values
        # -optimisation, read EC registers once per update, prevents hangs/unresponsive GUI
        self.ECHandler.ec_refresh()

        self.cpuMode = self.ECHandler.ec_read(int(ECS.CPU_FAN_MODE_CONTROL.value, 0))
        self.gpuMode = self.ECHandler.ec_read(int(ECS.GPU_FAN_MODE_CONTROL.value, 0))
        self.powerPluggedIn = self.ECHandler.ec_read(int(ECS.POWERSTATUS.value, 0))
        self.onBatteryPower = self.ECHandler.ec_read(int(ECS.BATTERYSTATUS.value, 0))
        self.nitroMode = self.ECHandler.ec_read(int(ECS.NITROMODE.value, 0))
        self.batteryChargeLimit = self.ECHandler.ec_read(
            int(ECS.BATTERYCHARGELIMIT.value, 0)
        )

        self.cpuTemp = self.ECHandler.ec_read(int(ECS.CPUTEMP.value, 0))
        self.gpuTemp = self.ECHandler.ec_read(int(ECS.GPUTEMP.value, 0))
        self.sysTemp = self.ECHandler.ec_read(int(ECS.SYSTEMP.value, 0))

        cpufanspeedHighBits = self.ECHandler.ec_read(
            int(ECS.CPUFANSPEEDHIGHBITS.value, 0)
        )
        cpufanspeedLowBits = self.ECHandler.ec_read(
            int(ECS.CPUFANSPEEDLOWBITS.value, 0)
        )
        # example
        # cpufanspeed = '0x068B'
        # 1675
        self.cpufanspeed = cpufanspeedLowBits << 8 | cpufanspeedHighBits

        gpufanspeedHighBits = self.ECHandler.ec_read(
            int(ECS.GPUFANSPEEDHIGHBITS.value, 0)
        )
        gpufanspeedLowBits = self.ECHandler.ec_read(
            int(ECS.GPUFANSPEEDLOWBITS.value, 0)
        )
        self.gpufanspeed = gpufanspeedLowBits << 8 | gpufanspeedHighBits
        # print("cpufanspeed: " + str(cpufanspeed))
        # print("gpufanspeed: " + gpufanspeed)

    # ---------Radio Button callback functions------------
    def setQuietMode(self):
        self.ECHandler.ec_write(
            int(ECS.NITROMODE.value, 0), int(ECS.QUIETMODE.value, 0)
        )
        self.setGlobalAuto()

    def setDefaultMode(self):
        self.ECHandler.ec_write(
            int(ECS.NITROMODE.value, 0), int(ECS.DEFAULTMODE.value, 0)
        )
        self.setGlobalAuto()

    def setExtremeMode(self):
        self.ECHandler.ec_write(
            int(ECS.NITROMODE.value, 0), int(ECS.EXTREMEMODE.value, 0)
        )
        self.setGlobalAuto()

    def setTurboMode(self):
        self.ECHandler.ec_write(
            int(ECS.NITROMODE.value, 0), int(ECS.EXTREMEMODE.value, 0)
        )
        self.setGlobalAuto()

    def setGlobalAuto(self):
        if self.turboEnabled:
            self.turboEnabled = False

            self.cpuauto()
            self.gpuauto()

            self.global_auto.setChecked(True)
            self.cpu_auto.setChecked(True)
            self.gpu_auto.setChecked(True)

    def setGlobalTurbo(self):
        if not self.turboEnabled:
            self.turboEnabled = True

            self.cpumax()
            self.gpumax()

            self.global_turbo.setChecked(True)
            self.cpu_turbo.setChecked(True)
            self.gpu_turbo.setChecked(True)

    def cpuauto(self):
        self.ECHandler.ec_write(
            int(ECS.CPU_FAN_MODE_CONTROL.value, 0), int(ECS.CPU_AUTO_MODE.value, 0)
        )
        self.cpuFanMode = PFS.Auto

    def cpumax(self):
        self.ECHandler.ec_write(
            int(ECS.CPU_FAN_MODE_CONTROL.value, 0), int(ECS.CPU_TURBO_MODE.value, 0)
        )
        self.cpuFanMode = PFS.Turbo

    def cpusetmanual(self):
        self.ECHandler.ec_write(
            int(ECS.CPU_FAN_MODE_CONTROL.value, 0), int(ECS.CPU_MANUAL_MODE.value, 0)
        )
        self.cpuFanMode = PFS.Manual

    def cpumanual(self, level):
        # print(str(level * 10), end=', ')
        # print(hex(level * 10))
        self.ECHandler.ec_write(int(ECS.CPU_MANUAL_SPEED_CONTROL.value, 0), level * 10)

    def gpuauto(self):
        self.ECHandler.ec_write(
            int(ECS.GPU_FAN_MODE_CONTROL.value, 0), int(ECS.GPU_AUTO_MODE.value, 0)
        )
        self.gpuFanMode = PFS.Auto

    def gpumax(self):
        self.ECHandler.ec_write(
            int(ECS.GPU_FAN_MODE_CONTROL.value, 0), int(ECS.GPU_TURBO_MODE.value, 0)
        )
        self.gpuFanMode = PFS.Turbo

    def gpusetmanual(self):
        self.ECHandler.ec_write(
            int(ECS.GPU_FAN_MODE_CONTROL.value, 0), int(ECS.GPU_MANUAL_MODE.value, 0)
        )
        self.gpuFanMode = PFS.Manual

    def gpumanual(self, level):
        # print(level * 10, end=', ')
        # print(hex(level * 10))
        self.ECHandler.ec_write(int(ECS.GPU_MANUAL_SPEED_CONTROL.value, 0), level * 10)

    # Toggle 30 seconds keyboard backlight timer
    def togglekbauto(self, tog):
        if not tog:
            self.ECHandler.ec_write(
                int(ECS.KB_30_SEC_AUTO.value, 0), int(ECS.KB_30_AUTO_OFF.value, 0)
            )
        else:
            self.ECHandler.ec_write(
                int(ECS.KB_30_SEC_AUTO.value, 0), int(ECS.KB_30_AUTO_ON.value, 0)
            )

    # USB charging whilst off
    def toggleUSBCharging(self, tog):
        if tog:
            self.ECHandler.ec_write(
                int(ECS.POWEROFFUSBCHARGING.value, 0), int(ECS.USBCHARGINGON.value, 0)
            )
        else:
            self.ECHandler.ec_write(
                int(ECS.POWEROFFUSBCHARGING.value, 0), int(ECS.USBCHARGINGOFF.value, 0)
            )

    # Toggle Power Limit
    def togglePowerLimit(self, tog):
        if tog:
            self.ECHandler.ec_write(
                int(ECS.BATTERYCHARGELIMIT.value, 0), int(ECS.BATTERYLIMITON.value, 0)
            )
        else:
            self.ECHandler.ec_write(
                int(ECS.BATTERYCHARGELIMIT.value, 0), int(ECS.BATTERYLIMITOFF.value, 0)
            )

    # ----------------------------------------------------

    # Update the Battery status
    def setBatteryStatus(self):
        batteryStat = "Discharging"
        if self.onBatteryPower == int(ECS.BATTERYPLUGGEDINANDCHARGING.value, 0):
            batteryStat = "Charging"
        elif self.onBatteryPower == int(ECS.BATTERYDRAINING.value, 0):
            batteryStat = "Discharging"
        elif self.onBatteryPower == int(ECS.BATTERYOFF.value, 0):
            batteryStat = "Battery Not In Use"
        else:
            print(
                "Error read EC register for Battery Status: "
                + str(hex(self.onBatteryPower))
            )

        self.batteryStatusValue.setText(batteryStat)

        # Set the battery charge indicator
        if self.batteryChargeLimit == int(ECS.BATTERYLIMITON.value, 0):
            self.batteryChargeLimitValue.setText("On")
        elif self.batteryChargeLimit == int(ECS.BATTERYLIMITOFF.value, 0):
            self.batteryChargeLimitValue.setText("Off")

    # Update the Nitro state
    def setNitroMode(self):
        # print("nitroModeValue: " + str(self.nitroMode))
        if self.nitroMode == int(ECS.QUIETMODE.value, 0):
            self.nitroModeValue.setText("Quiet\t")
            self.quietModeCB.setChecked(True)
        elif self.nitroMode == int(ECS.DEFAULTMODE.value, 0):
            self.nitroModeValue.setText("Default\t")
            self.defaultModeCB.setChecked(True)
        elif self.nitroMode == int(ECS.EXTREMEMODE.value, 0):
            self.nitroModeValue.setText("Extreme\t")
            self.extremeModeCB.setChecked(True)
        else:
            print("Error read EC register for Nitro Mode: " + str(self.nitroMode))

    # keyboard
    def kbSelectColor(self):
        # open color dialog with current color selected
        color = QtWidgets.QColorDialog.getColor(
            initial=QtGui.QColor.fromRgb(*self.selected_color)
        )
        if color.isValid():
            self.selected_color = (color.red(), color.green(), color.blue())

    def kbApplySettings(self):
        mode = self.mode_combo.currentIndex()
        zone = self.zone_combo.currentIndex()
        speed = self.speed_spin.value()
        brightness = self.brightness_spin.value()
        direction = self.direction_combo.currentIndex() + 1
        red, green, blue = self.selected_color

        keyboard.set_mode(mode, zone, speed, brightness, direction, red, green, blue)

    def kbSaveConfig(self):
        if not os.path.exists(CONFIG_FOLDER + "rbg.conf"):
            os.system(f"mkdir -p {CONFIG_FOLDER}")
            os.system(f"touch {CONFIG_FOLDER + 'rbg.conf'}")
        path = f"{CONFIG_FOLDER + 'rbg.conf'}"
        with open(path, "w") as f:
            f.write(f"{self.mode_combo.currentIndex()}\n")
            f.write(f"{self.zone_combo.currentIndex()}\n")
            f.write(f"{self.speed_spin.value()}\n")
            f.write(f"{self.brightness_spin.value()}\n")
            f.write(f"{self.direction_combo.currentIndex()}\n")
            f.write(f"{self.selected_color[0]}\n")
            f.write(f"{self.selected_color[1]}\n")
            f.write(f"{self.selected_color[2]}\n")

    def kbLoadConfig(self):
        if not os.path.exists(CONFIG_FOLDER + "rbg.conf"):
            return
        path = f"{CONFIG_FOLDER + 'rbg.conf'}"
        with open(path, "r") as f:
            self.mode_combo.setCurrentIndex(int(f.readline()))
            self.zone_combo.setCurrentIndex(int(f.readline()))
            self.speed_spin.setValue(int(f.readline()))
            self.brightness_spin.setValue(int(f.readline()))
            self.direction_combo.setCurrentIndex(int(f.readline()))
            self.selected_color = (
                int(f.readline()),
                int(f.readline()),
                int(f.readline()),
            )
        self.kbApplySettings()

    def saveConfig(self):
        if not os.path.exists(CONFIG_FOLDER + "nitrosense.conf"):
            os.system(f"mkdir -p {CONFIG_FOLDER}")
            os.system(f"touch {CONFIG_FOLDER + 'nitrosense.conf'}")
        path = f"{CONFIG_FOLDER + 'nitrosense.conf'}"
        with open(path, "w") as f:
            f.write(f"{self.cpuMode}\n")
            f.write(f"{self.gpuMode}\n")
            f.write(f"{self.KB30Timeout}\n")
            f.write(f"{self.usbCharging}\n")
            f.write(f"{self.nitroMode}\n")
            f.write(f"{self.batteryChargeLimit}\n")

    def loadConfig(self):
        if not os.path.exists(CONFIG_FOLDER + "nitrosense.conf"):
            return
        path = f"{CONFIG_FOLDER + 'nitrosense.conf'}"
        with open(path, "r") as f:
            self.cpuMode = int(f.readline())
            self.gpuMode = int(f.readline())
            self.KB30Timeout = int(f.readline())
            self.usbCharging = int(f.readline())
            self.nitroMode = int(f.readline())
            self.batteryChargeLimit = int(f.readline())
        self.setFanMode()
        self.setNitroMode()
        self.checkPowerTempFan()
        self.setBatteryStatus()

    def saveAndRun(self, function):
        function()
        self.saveConfig()

    # Update the UI state
    def updateNitroStatus(self):
        checkVoltage(self)
        # print(self.voltage)
        minmaxVoltages = (
            str("%1.2f" % self.minrecordedVoltage)
            + " / "
            + str("%1.2f" % self.maxrecordedVoltage)
        )
        # print(minmaxVoltages)
        self.voltageValue.setText(str("%1.2f" % self.voltage))
        self.voltageMinMaxValue.setText(minmaxVoltages)

        self.undervoltStatus.setText(self.undervolt)

        self.checkPowerTempFan()

        if (
            self.cpuMode == int(ECS.CPU_TURBO_MODE.value, 0)
            or self.cpuMode == int("0xA8", 0)
        ) and self.gpuMode == int(ECS.GPU_TURBO_MODE.value, 0):
            if not self.turboEnabled:
                print("Turbo enabled")
                self.setTurboMode()

        if self.cpuMode == int(ECS.CPU_AUTO_MODE.value, 0) and self.gpuMode == int(
            ECS.GPU_AUTO_MODE.value, 0
        ):
            if self.turboEnabled:
                print("Turbo disabled")
                self.setDefaultMode()

        self.setBatteryStatus()
        self.setNitroMode()

        #self.voltageChart.update(float("%1.2f" % self.voltage))
        #self.cpuChart.update(self.cpuTemp)
        #self.gpuChart.update(self.gpuTemp)
        #self.sysChart.update(self.sysTemp)
        #self.cpuFanChart.update(self.cpufanspeed)
        #self.gpuFanChart.update(self.gpufanspeed)
#
        self.cpuFanSpeedValue.setText(str(self.cpufanspeed) + " RPM")
        self.gpuFanSpeedValue.setText(str(self.gpufanspeed) + " RPM")
        self.cpuTempValue.setText(str(self.cpuTemp) + "°")
        self.gpuTempValue.setText(str(self.gpuTemp) + "°")
        self.sysTempValue.setText(str(self.sysTemp) + "°")
#
        self.powerStatusValue.setText(str(self.powerPluggedIn))

    # ----------------------------------------------------
    # Exit the program cleanly
    def shutdown(self):
        print("Cleaning up..")
        self.ECHandler.shutdown_ec()
        voltage_process.close()
        print("Exiting")
        exit(0)


app = QtWidgets.QApplication(sys.argv)
application = MainWindow()
app.setApplicationName("Linux NitroSense")
# Makes the window not resizeable
application.setFixedSize(500, 700)

application.setWindowIcon(QtGui.QIcon("nitro-sense.ico"))
# Set global window opacity
# application.setWindowOpacity(0.97)

# Dark theme implementation
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
palette.setColor(QPalette.ColorRole.NoRole, QColor(53, 53, 53))
app.setPalette(palette)
application.setPalette(palette)
application.show()
app.exec()
sys.exit()
