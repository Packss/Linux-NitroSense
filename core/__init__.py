from PyQt6.QtCore import QObject, QProcess, pyqtSignal

class CommandRunner(QObject):
    finished = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self._handle_output)
        self.process.finished.connect(self._on_finished)
        self.output = ""

    def run(self, cmd, args):
        self.output = ""  # Reset output
        self.process.start(cmd, args)
        self.process.waitForFinished()

    def _handle_output(self):
        new_output = self.process.readAllStandardOutput().data().decode()
        self.output += new_output

    def _on_finished(self):
        self.finished.emit(self.output)

    def close(self):
        self.process.close()