## NitroSense™ "clone" for linux
### Controls fan speed, gaming modes and undervolting on Linux.
<img src="https://github.com/user-attachments/assets/6bb2a8e8-4816-4b86-ac8d-e882fb464f15" width="400" />
<img src="https://github.com/user-attachments/assets/9b91a2f9-94e8-4f72-bb1b-cb8978ae20cd" width="400" />

## Current supported devices:
- AN515-44
- AN515-46
- AN515-56
- AN515-58

_[OPTIONAL]_
- Install ```amdctl``` for undervolt and voltage readings on amd.
- Install [acer-predator-module](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module) for keyboard rgb control

## Binary release:
- Get the latest binary [here](https://github.com/Packss/Linux-NitroSense/releases/latest)
- Download ```nitrosense```
- Execute ```sudo -E ./nitrosense```
- No dependencies needed

## Dependencies [Development]:
* All:
  ```sh
  pip install -r requirements.txt
  ```

* Ubuntu / Linux Mint:
  ```sh
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```

* Arch Linux:
  ```sh
  # amdctl and acpi_ec can be installed via git, or from the AUR
  paru -Syu amdctl acpi_ec-dkms-git
  sudo modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```

## Usage:
### COMMAND LINE

 - ```sudo``` is required in order to access the Super I/O EC registers and apply undervolt offsets.
  - From the command line run the main script as root:
    ```sh
    sudo -E python3 main.py
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

Packages:
* ```Python Qt6``` -> [PyQt6](https://pypi.org/project/PyQt6/)
* ```acpi_ec``` -> [acpi_ec by musikid](https://github.com/musikid/acpi_ec/)
