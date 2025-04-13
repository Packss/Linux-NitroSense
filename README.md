## NitroSense™ clone for ```AN515-46```
### Controls fan speed, gaming modes and undervolting on Linux. This application is intended for Acer Nitro 5 AN515-46 model.

## Disclaimer:
* Secure Boot **IS** \* supported if you only use the ```acpi_ec``` package.
* Secure Boot is **NOT** \* supported if you want to control CPU voltage offsets using the ```msr-tools``` and ```amdctl``` packages.
* Using this application with other laptops may potentially damage them. Proceed at your discretion.


## Dependencies [Development]:
* Ubuntu / Linux Mint:
  ```
  sudo apt-get install python3-pyqt6, python3-pyqt6.qtchart
  ```

  ```
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```
 
* Fedora:
  ```
  sudo dnf install python3-qt6
  sudo dnf install python3-pyqtchart
  ```
  Make sure SecureBoot is off.

  ```
  sudo dnf install dkms
  
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```
_[OPTIONAL]_
- Install ```amdctl``` for undervolt and voltage readings
- Install [acer-predator-module](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module) for keyboard rgb control

## Install:
- From the command line
```sh
git clone https://github.com/Packss/Linux-NitroSense/
cd Linux-NitroSense/
```

## Usage:
### COMMAND LINE

 - ```sudo``` is required in order to access the Super I/O EC registers and apply undervolt offsets.
  - From the command line run the main script as root:
  ```sh
  sudo python3 main.py
  ```

### ICON
 - Alternatively you can copy the .desktop file to your applications folder and launch the program via it's icon.
  - Open ```nitro-sense.desktop``` in a text editor.
  - Set ```<path_to_NitroSense>``` to the directory where you downloaded this project.
  ```sh
  Exec=sh -c "pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY sh -c 'cd <path_to_NitroSense> && python3 main.py'"
  Icon=<path_to_NitroSense>/app_icon.ico
  ```
  - Copy the file to the application directory
  ```sh
  sudo cp nitro-sense.desktop /usr/share/applications/
  ```
  - Now launch via the application and on initialization it will prompt for the user password.


### NVIDIA-POWERD
- After switching nitro modes \* **YOU MAY NEED TO RESTART NVIDIA-POWERD SERVICE IN ORDER TO DETECT NEW TGP** \*
```sh
sudo systemctl restart nvidia-powerd
```
- You can check the current GPU TGP via
```
nvidia-smi
```

## Dependencies [Development]:
* Ubuntu / Linux Mint:
  ```sh
  sudo apt-get install python3-pyqt6, python3-pyqt6.qtchart
  ```

  ```sh
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```

  ```sh
  [OPTIONAL]
  pip install git+https://github.com/georgewhewell/undervolt.git
  sudo apt-get install msr-tools
  ```
  
* Fedora:
  ```sh
  sudo dnf install python3-qt6
  sudo dnf install python3-pyqtchart
  ```
  Make sure SecureBoot is off.

  ```sh
  sudo dnf install dkms

  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```

  ```sh
  [OPTIONAL]
  pip install git+https://github.com/georgewhewell/undervolt.git
  sudo dnf install msr-tools
  ```
* Arch Linux:
 ```sh
 sudo pacman -Syu linux-headers

 #amdctl and acpi_ec can be installed via git, or from the AUR
 sudo yay -Syu amdctl acpi_ec-dkms-git
 sudo modprobe acpi_ec
 sudo cat /dev/ec #confirm access to EC

 #install python dependencies with venv
 python3 -m venv ./venv
 source ./venv/bin/activate
 pip install PyQt6 PyQtChart
 ```
Packages:
* ```Python Qt6``` -> [PyQt6](https://pypi.org/project/PyQt6/)
* ```acpi_ec``` -> [acpi_ec by musikid](https://github.com/musikid/acpi_ec/)
* ```msr-tools``` -> [msr-tools by intel](https://github.com/intel/msr-tools)

## This is a fork of [PredatorSense by snowyoneill](https://github.com/snowyoneill/Linux-PredatorSense), customized for ```AN515-46-R5WF```

## Changelog:

Nothing yet
