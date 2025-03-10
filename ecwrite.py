import os
from PyQt5.QtCore import QProcess
# EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'
EC_IO_FILE = '/dev/ec' if os.system('ls /sys/kernel/debug/ec/ec0/io 2> /dev/null > /dev/null') else '/sys/kernel/debug/ec/ec0/io'

##------------------------------##
##----Class to read/write EC----##
class ECWrite:
    def __init__(self):
        self.ec_path = EC_IO_FILE
        print("Setting up EC access..." + self.ec_path)
        self.buffer = b''
        self.ec_file = None
        self.setupEC()

    def setupEC(self):
        try:
            self.ec_file = open(self.ec_path, 'rb+')  # buffering=0)
        except PermissionError:
            print('Run with sudo')
            exit(1)
        except FileNotFoundError:
            print(self.ec_path, 'not found. Check acpi_ec')
            process = QProcess()
            process.start('modprobe acpi_ec')
            process.waitForFinished()
            process.close()
            try:
                self.ec_file = open(self.ec_path, 'rb+')
            except FileNotFoundError:
                print('Failed to load acpi_ec')
                exit(1)
        except Exception as e:
            print("Error: " + str(e))

    def ec_write(self, address, value):

        try:
            self.ec_file.seek(address)
            self.ec_file.write(bytearray([value]))

        except Exception as e:
            print("Error: " + str(e))
            exit(1)

    ## Copy EC contents to buffer
    def ec_refresh(self):
        try:
            self.ec_file.seek(0)
            self.buffer = self.ec_file.read()
            # print(self.buffer)
            if self.buffer == b'':
                print("BAD BUFFER EXITING!")
                exit(1)

        except Exception as e:
            print("Error: " + str(e))
            exit(1)

    ## Read EC contents from buffer instead of going to disk
    def ec_read(self, address):
        try:
            # self.ec_file.seek(address)
            # return ord(self.ec_file.read(1))

            if self.buffer == b'':
                print("BUFFER EMPTY!")
                exit(1)

            return self.buffer[address]
            # return ord(self.buffer[int(address)])
        except Exception as e:
            print("Error: " + str(e))
            exit(1)

    def shutdownEC(self):
        self.ec_file.close()
