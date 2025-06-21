import os
import sys


class ECWrite:
    def __init__(self):
        self.buffer = b""
        self.ec_file = None
        self._load_acpi_ec_module()
        if self.ec_file and not self.ec_file.writable():
            self._handle_error(
                "EC file is not writable. Ensure you have the necessary permissions."
            )

    def _load_acpi_ec_module(self):
        os.system("modprobe -r ec_sys")
        os.system("modprobe ec_sys write_support=y")
        if os.path.exists("/sys/kernel/debug/ec/ec0/io"):
            self.ec_file = open("/sys/kernel/debug/ec/ec0/io", "wb+")
            print("Loaded 'ec_sys' module successfully.")
            return
        else:
            print(
                "Failed to load 'ec_sys' module. Attempting to load 'acpi_ec' module."
            )

        os.system("modprobe acpi_ec")
        if os.path.exists("/dev/ec"):
            self.ec_file = open("/dev/ec", "wb+")
            print("Loaded 'acpi_ec' module successfully.")
        else:
            self._handle_error("Failed to load 'acpi_ec' module.")

    def ec_write(self, address: int, value: int):
        if address is None:
            print("Function not supported for this device.")
            return -1
        try:
            if self.ec_file is None:
                self._handle_error(
                    "EC file is not initialized. Ensure '_setup_ec()' was successful."
                )
            self.ec_file.seek(address)
            self.ec_file.write(bytearray([value]))
        except Exception as e:
            self._handle_error(f"Error writing to the EC: {e}")

    def ec_refresh(self):
        try:
            if self.ec_file is None:
                self._handle_error(
                    "EC file is not initialized. Ensure '_setup_ec()' was successful."
                )
            self.ec_file.seek(0)
            self.buffer = self.ec_file.read()
            if not self.buffer:
                self._handle_error("Empty buffer! Exiting.")
        except Exception as e:
            self._handle_error(f"Error refreshing the EC buffer: {e}")

    def ec_read(self, address: int) -> int:
        if address is None:
            print("Function not supported for this device.")
            return -1
        try:
            if not self.buffer:
                self._handle_error(
                    "Empty buffer! Make sure to call 'ec_refresh()' before reading."
                )
            return self.buffer[address]
        except Exception as e:
            self._handle_error(f"Error reading from the EC buffer: {e}")

    def shutdown_ec(self):
        if self.ec_file:
            self.ec_file.close()
            print("EC access successfully terminated.")

    def _handle_error(self, message):
        print(f"Error: {message}")
        sys.exit(1)
