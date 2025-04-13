import os
from PyQt6.QtCore import QProcess

class ECWrite:
    EC_IO_FILE = (
        '/dev/ec'
        if os.system('ls /sys/kernel/debug/ec/ec0/io 2> /dev/null > /dev/null')
        else '/sys/kernel/debug/ec/ec0/io'
    )

    def __init__(self):
        self.ec_path = self.EC_IO_FILE
        self.buffer = b''
        self.ec_file = None
        print(f"Setting up access to the EC at: {self.ec_path}")
        self._setup_ec()

    def _setup_ec(self):
        try:
            self.ec_file = open(self.ec_path, 'rb+')
        except PermissionError:
            self._handle_error("Run the program with administrator privileges (sudo).")
        except FileNotFoundError:
            print(f"{self.ec_path} not found. Attempting to load the 'acpi_ec' module.")
            self._load_acpi_ec_module()
        except Exception as e:
            self._handle_error(f"Unexpected error while setting up the EC: {e}")

    def _load_acpi_ec_module(self):
        process = QProcess()
        process.start('modprobe acpi_ec')
        process.waitForFinished()
        process.close()

        try:
            self.ec_file = open(self.ec_path, 'rb+')
        except FileNotFoundError:
            self._handle_error("Failed to load the 'acpi_ec' module.")

    def ec_write(self, address: int, value: int):
        try:
            if self.ec_file is None:
                self._handle_error("EC file is not initialized. Ensure '_setup_ec()' was successful.")
            self.ec_file.seek(address)
            self.ec_file.write(bytearray([value]))
        except Exception as e:
            self._handle_error(f"Error writing to the EC: {e}")

    def ec_refresh(self):
        try:
            if self.ec_file is None:
                self._handle_error("EC file is not initialized. Ensure '_setup_ec()' was successful.")
            self.ec_file.seek(0)
            self.buffer = self.ec_file.read()
            if not self.buffer:
                self._handle_error("Empty buffer! Exiting.")
        except Exception as e:
            self._handle_error(f"Error refreshing the EC buffer: {e}")

    def ec_read(self, address: int) -> int:
        try:
            if not self.buffer:
                self._handle_error("Empty buffer! Make sure to call 'ec_refresh()' before reading.")
            return self.buffer[address]
        except Exception as e:
            self._handle_error(f"Error reading from the EC buffer: {e}")

    def shutdown_ec(self):
        if self.ec_file:
            self.ec_file.close()
            print("EC access successfully terminated.")

    def _handle_error(self, message):
        print(f"Error: {message}")
        exit(1)
