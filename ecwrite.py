import os
from PyQt6.QtCore import QProcess

# Determine the path of the EC_IO_FILE
EC_IO_FILE = (
    '/dev/ec'
    if os.system('ls /sys/kernel/debug/ec/ec0/io 2> /dev/null > /dev/null')
    else '/sys/kernel/debug/ec/ec0/io'
)

class ECWrite:
    def __init__(self):
        """Initializes access to the EC (Embedded Controller)."""
        self.ec_path = EC_IO_FILE
        self.buffer = b''
        self.ec_file = None
        print(f"Setting up access to the EC at: {self.ec_path}")
        self._setup_ec()

    def _setup_ec(self):
        """Sets up access to the EC file."""
        try:
            self.ec_file = open(self.ec_path, 'rb+')
        except PermissionError:
            print("Error: Run the program with administrator privileges (sudo).")
            exit(1)
        except FileNotFoundError:
            print(f"Error: {self.ec_path} not found. Attempting to load the 'acpi_ec' module.")
            self._load_acpi_ec_module()
        except Exception as e:
            print(f"Unexpected error while setting up the EC: {e}")
            exit(1)

    def _load_acpi_ec_module(self):
        """Attempts to load the 'acpi_ec' module if the EC file is not found."""
        process = QProcess()
        process.start('modprobe acpi_ec')
        process.waitForFinished()
        process.close()

        try:
            self.ec_file = open(self.ec_path, 'rb+')
        except FileNotFoundError:
            print("Error: Failed to load the 'acpi_ec' module.")
            exit(1)

    def ec_write(self, address: int, value: int):
        """Writes a value to a specific EC address."""
        try:
            self.ec_file.seek(address)
            self.ec_file.write(bytearray([value]))
        except Exception as e:
            print(f"Error writing to the EC: {e}")
            exit(1)

    def ec_refresh(self):
        """Refreshes the local buffer with data from the EC."""
        try:
            self.ec_file.seek(0)
            self.buffer = self.ec_file.read()
            if not self.buffer:
                print("Error: Empty buffer! Exiting.")
                exit(1)
        except Exception as e:
            print(f"Error refreshing the EC buffer: {e}")
            exit(1)

    def ec_read(self, address: int) -> int:
        """Reads a value from a specific address in the EC buffer."""
        try:
            if not self.buffer:
                print("Error: Empty buffer! Make sure to call 'ec_refresh()' before reading.")
                exit(1)
            return self.buffer[address]
        except Exception as e:
            print(f"Error reading from the EC buffer: {e}")
            exit(1)

    def shutdown_ec(self):
        """Closes the EC file safely."""
        if self.ec_file:
            self.ec_file.close()
            print("EC access successfully terminated.")
