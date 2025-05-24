import enum
import sys
from dmidecode import DMIDecode

## ------------------------------##
## --Nitro EC Register Class--##
# ---------------------------------##
# This class contains the register addresses for the Nitro EC.
# The addresses are used for communication with the EC (Embedded Controller).
# CAUTION: Changing or using these values on different laptops may cause
# unexpected behavior or damage to the laptop.
# Use at your own risk.
# ---------------------------------##

class ECS_AN515_46(enum.Enum):
    GPU_FAN_MODE_CONTROL = "0x21"   # Address to set GPU fan mode
    GPU_AUTO_MODE = "0x10"
    GPU_TURBO_MODE = "0x20"
    GPU_MANUAL_MODE = "0x30"
    GPU_MANUAL_SPEED_CONTROL = "0x3A"   # Address to set GPU fan speed

    CPU_FAN_MODE_CONTROL = "0x22"   # Address to set CPU fan mode
    CPU_AUTO_MODE = "0x04"
    CPU_TURBO_MODE = "0x08"
    CPU_MANUAL_MODE = "0x0C"
    CPU_MANUAL_SPEED_CONTROL = "0x37"   # Address to set CPU fan speed

    KB_30_SEC_AUTO = "0x06"     # Address to set keyboard backlight timeout
    KB_30_AUTO_OFF = "0x00"
    KB_30_AUTO_ON = "0x1E"

    CPUFANSPEEDHIGHBITS = "0x13"
    CPUFANSPEEDLOWBITS = "0x14"
    GPUFANSPEEDHIGHBITS = "0x15"
    GPUFANSPEEDLOWBITS = "0x16"

    CPUTEMP = "0xB0"
    GPUTEMP = "0xB6"
    SYSTEMP = "0xB3"

    POWERSTATUS = "0x00"        # Address to read power status
    POWERPLUGGEDIN = "0x01"
    POWERUNPLUGGED = "0x00"

    BATTERYCHARGELIMIT = "0x03" # Address to set battery charge limit
    BATTERYLIMITON = "0x51"
    BATTERYLIMITOFF = "0x11"

    BATTERYSTATUS = "0xC1"      # Address to read battery status
    BATTERYPLUGGEDINANDCHARGING = "0x02"
    BATTERYDRAINING = "0x01"
    BATTERYOFF = "0x00"

    POWEROFFUSBCHARGING = "0x08" # Address to switch USB charging on/off
    USBCHARGINGON = "0x0F"
    USBCHARGINGOFF = "0x1F"

    NITROMODE = "0x2C"          # Address to change modes
    QUIETMODE = "0x00"  
    DEFAULTMODE = "0x01"
    EXTREMEMODE = "0x04"

class ECS_AN515_44(enum.Enum):
    GPU_FAN_MODE_CONTROL = "0x21"   # Address to set GPU fan mode
    GPU_AUTO_MODE = "0x10"
    GPU_TURBO_MODE = "0x20"
    GPU_MANUAL_MODE = "0x30"
    GPU_MANUAL_SPEED_CONTROL = "0x3A"   # Address to set GPU fan speed

    CPU_FAN_MODE_CONTROL = "0x22"   # Address to set CPU fan mode
    CPU_AUTO_MODE = "0x04"
    CPU_TURBO_MODE = "0x08"
    CPU_MANUAL_MODE = "0x0C"
    CPU_MANUAL_SPEED_CONTROL = "0x37"   # Address to set CPU fan speed

    KB_30_SEC_AUTO = "0x06"     # Address to set keyboard backlight timeout
    KB_30_AUTO_OFF = "0x00"
    KB_30_AUTO_ON = "0x1E"

    CPUFANSPEEDHIGHBITS = "0x13"
    CPUFANSPEEDLOWBITS = "0x14"
    GPUFANSPEEDHIGHBITS = "0x15"
    GPUFANSPEEDLOWBITS = "0x16"

    CPUTEMP = "0xB0"
    GPUTEMP = "0xB4"
    SYSTEMP = "0xB0"

    POWERSTATUS = "0x00"        # Address to read power status
    POWERPLUGGEDIN = "0x01"
    POWERUNPLUGGED = "0x00"

    BATTERYCHARGELIMIT = "0x03" # Address to set battery charge limit
    BATTERYLIMITON = "0x40"
    BATTERYLIMITOFF = "0x00"

    BATTERYSTATUS = "0xC1"      # Address to read battery status
    BATTERYPLUGGEDINANDCHARGING = "0x02"
    BATTERYDRAINING = "0x01"
    BATTERYOFF = "0x00"

    POWEROFFUSBCHARGING = "0x08" # Address to switch USB charging on/off
    USBCHARGINGON = "0x0F"
    USBCHARGINGOFF = "0x1F"

    NITROMODE = "0x2C"          # Address to change modes
    QUIETMODE = "0x00"  
    DEFAULTMODE = "0x01"
    EXTREMEMODE = "0x04"

MODEL_TO_ECS = {
    "Nitro AN515-46": ECS_AN515_46,
    "Nitro AN515-56": ECS_AN515_46,
    "Nitro AN515-44": ECS_AN515_44,
    "Nitro AN515-58": ECS_AN515_46,
}

model = DMIDecode().model()
print(f"Detected running on: {model}")

ECS = MODEL_TO_ECS.get(model)
if ECS:
    print(f"Using registers for {model}")
else:
    print(f"Device {model} not supported!")
    sys.exit(1)
