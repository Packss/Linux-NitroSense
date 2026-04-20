from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_NitroSense(object):
    def __init__(self):
        self.quietModeCB = None
        self.defaultModeCB = None
        self.extremeModeCB = None
        self.nitroModeValue = None
        self.batteryChargeLimitValue = None
        self.nitroModeLabel = None
        self.batteryChargeLimitLabel = None
        self.batteryStatusValue = None
        self.batteryStatusLabel = None
        self.powerStatusValue = None
        self.formLayout_2 = None
        self.predMode = None
        self.horizontalLayout_7 = None
        self.temp_box = None
        self.gridLayout_2 = None
        self.cpuTempValue = None
        self.gpuTempValue = None
        self.sysTempLabel = None
        self.sysTempValue = None
        self.gpuTempLabel = None
        self.cpuTempLabel = None
        self.fan_box = None
        self.gridLayout_6 = None
        self.gpuFanSpeedValue = None
        self.gpuFanSpeedLabel = None
        self.cpuFanSpeedLabel = None
        self.cpuFanSpeedValue = None
        self.KB_box = None
        self.miscLayout = None
        self.KBTimerCB = None
        self.usbChargingCB = None
        self.chargeLimit = None
        self.undervolt_box = None
        self.gridLayout_5 = None
        self.voltageMinMaxValue = None
        self.voltageMinMaxLabel = None
        self.voltageValue = None
        self.undervoltStatus = None
        self.voltageLabel = None
        self.horizontalLayout_2 = None
        self.cpu_box = None
        self.horizontalLayout_4 = None
        self.verticalLayout_4 = None
        self.cpu_auto = None
        self.cpu_manual = None
        self.cpu_turbo = None
        self.cpuManualSlider = None
        self.verticalLayout_6 = None
        self.undervolt_dropdown = None
        self.undervolt_button = None
        self.global_box = None
        self.globalLayout = None
        self.global_auto = None
        self.global_turbo = None
        self.exit_button = None
        self.gpu_box = None
        self.horizontalLayout_5 = None
        self.verticalLayout_5 = None
        self.gpu_auto = None
        self.gpu_manual = None
        self.gpu_turbo = None
        self.gpuManualSlider = None
        self.keyboard_box = None
        self.keyboardBoxLayout = None
        self.verticalLayout_8 = None
        self.formLayout = None
        self.mode_label = None
        self.mode_combo = None
        self.zone_label = None
        self.zone_combo = None
        self.speed_label = None
        self.speed_spin = None
        self.brightness_label = None
        self.brightness_spin = None
        self.direction_label = None
        self.direction_combo = None
        self.color_button = None
        self.apply_button = None
        self.load_button = None
        self.save_button = None
        self.powerStatusLabel = None
        self.verticalLayout_2 = None
        self.verticalLayout_3 = None
        self.horizontalLayout_3 = None
        self.status_box = None
        self.keyboard_tab = None
        self.tab = None
        self.verticalLayout_7 = None
        self.verticalLayout_9 = None
        self.fan_control_tab = None
        self.verticalLayout = None

    @staticmethod
    def _apply_size_policy(widget: QtWidgets.QWidget,
                           h_policy: QtWidgets.QSizePolicy.Policy,
                           v_policy: QtWidgets.QSizePolicy.Policy) -> None:
        size_policy = QtWidgets.QSizePolicy(h_policy, v_policy)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(size_policy)

    @staticmethod
    def _create_font(family: str = "TT Squares", point_size: int = 11,
                     bold: bool = False, italic: bool = False) -> QtGui.QFont:
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(point_size)
        font.setBold(bold)
        font.setItalic(italic)
        return font

    @staticmethod
    def _setup_label(label: QtWidgets.QLabel,
                     font: QtGui.QFont = None,
                     size_policy: tuple = None,
                     object_name: str = "") -> None:
        if size_policy:
            h_policy, v_policy = size_policy
            Ui_NitroSense._apply_size_policy(label, h_policy, v_policy)
        if font:
            label.setFont(font)
        label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        if object_name:
            label.setObjectName(object_name)

    @staticmethod
    def _setup_group_box(group_box: QtWidgets.QGroupBox,
                         h_policy: QtWidgets.QSizePolicy.Policy,
                         v_policy: QtWidgets.QSizePolicy.Policy,
                         font: QtGui.QFont = None,
                         object_name: str = "") -> None:
        Ui_NitroSense._apply_size_policy(group_box, h_policy, v_policy)
        if font:
            group_box.setFont(font)
        group_box.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        if object_name:
            group_box.setObjectName(object_name)

    @staticmethod
    def _setup_button_widget(widget: QtWidgets.QWidget,
                             font: QtGui.QFont = None,
                             object_name: str = "",
                             checked: bool = False) -> None:
        Ui_NitroSense._apply_size_policy(widget,
                                         QtWidgets.QSizePolicy.Policy.Preferred,
                                         QtWidgets.QSizePolicy.Policy.Preferred)
        if font:
            widget.setFont(font)
        widget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        if object_name:
            widget.setObjectName(object_name)
        if isinstance(widget, (QtWidgets.QRadioButton, QtWidgets.QCheckBox)):
            widget.setChecked(checked)

    @staticmethod
    def _setup_radio_button(radio_button: QtWidgets.QRadioButton,
                            font: QtGui.QFont = None,
                            object_name: str = "",
                            checked: bool = False) -> None:
        Ui_NitroSense._setup_button_widget(radio_button, font, object_name, checked)

    @staticmethod
    def _setup_checkbox(checkbox: QtWidgets.QCheckBox,
                        font: QtGui.QFont = None,
                        object_name: str = "",
                        checked: bool = False) -> None:
        Ui_NitroSense._setup_button_widget(checkbox, font, object_name, checked)

    @staticmethod
    def _setup_slider(slider: QtWidgets.QSlider,
                      font: QtGui.QFont = None,
                      object_name: str = "",
                      maximum: int = 20,
                      value: int = 20,
                      vertical: bool = True,
                      enabled: bool = False) -> None:
        slider.setEnabled(enabled)
        Ui_NitroSense._apply_size_policy(slider,
                                         QtWidgets.QSizePolicy.Policy.Maximum,
                                         QtWidgets.QSizePolicy.Policy.Maximum)
        if vertical:
            slider.setMaximumSize(QtCore.QSize(16777215, 180))
        else:
            slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        if font:
            slider.setFont(font)
        slider.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        slider.setMaximum(maximum)
        slider.setProperty("value", value)
        slider.setTracking(True)
        if vertical:
            slider.setOrientation(QtCore.Qt.Orientation.Vertical)
            slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        else:
            slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
            slider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        slider.setTickInterval(1)
        if object_name:
            slider.setObjectName(object_name)

    @staticmethod
    def _apply_common_properties(widget: QtWidgets.QWidget,
                                 h_policy: QtWidgets.QSizePolicy.Policy,
                                 v_policy: QtWidgets.QSizePolicy.Policy,
                                 font: QtGui.QFont = None,
                                 object_name: str = "",
                                 max_size: tuple = None) -> None:
        Ui_NitroSense._apply_size_policy(widget, h_policy, v_policy)
        if max_size:
            widget.setMaximumSize(QtCore.QSize(*max_size))
        if font:
            widget.setFont(font)
        widget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        widget.setStyleSheet("")
        if object_name:
            widget.setObjectName(object_name)

    @staticmethod
    def _setup_combobox(combobox: QtWidgets.QComboBox,
                        h_policy: QtWidgets.QSizePolicy.Policy,
                        v_policy: QtWidgets.QSizePolicy.Policy,
                        font: QtGui.QFont = None,
                        object_name: str = "",
                        max_size: tuple = None) -> None:
        Ui_NitroSense._apply_common_properties(combobox, h_policy, v_policy, font, object_name, max_size)

    @staticmethod
    def _setup_pushbutton(button: QtWidgets.QPushButton,
                          h_policy: QtWidgets.QSizePolicy.Policy,
                          v_policy: QtWidgets.QSizePolicy.Policy,
                          font: QtGui.QFont = None,
                          object_name: str = "",
                          max_size: tuple = None) -> None:
        Ui_NitroSense._apply_common_properties(button, h_policy, v_policy, font, object_name, max_size)

    def setupUi(self, NitroSense):
        NitroSense.setObjectName("NitroSense")
        NitroSense.resize(488, 688)
        self._apply_size_policy(NitroSense, QtWidgets.QSizePolicy.Policy.Maximum,
                               QtWidgets.QSizePolicy.Policy.Maximum)
        NitroSense.setMaximumSize(QtCore.QSize(488, 688))

        NitroSense.setStyleSheet("""* {
            color: white;
            selection-background-color: rgb(255, 0, 0);
        }
        QWidget #tab, #monitoring_tab, #keyboard_tab {
            background-repeat: no-repeat;
            background-position: top center;
            background-color: #252525;
        }
        QPushButton, QComboBox {
            background-repeat: no-repeat;
            background-position: top center;
            background-color: #535353;
        }
        QGroupBox {
            color: blue;
            font: bold;
            border: 1px solid silver;
            border-radius: 6px;
            margin-top: 6px;
        }
        QGroupBox #monitoring_box {
            border: 0px dotted gray;
            margin: 0 0 0 0;
        }
        QGroupBox #powerStatusLabel, #batteryStatusLabel, #batteryChargeLimitLabel,
        #nitroModeLabel, #cpuTempLabel, #gpuTempLabel, #sysTempLabel,
        #cpuFanSpeedLabel, #gpuFanSpeedLabel, #voltageLabel, #voltageMinMaxLabel,
        #mode_label, #zone_label, #speed_label, #brightness_label, #direction_label,
        #undervolt_box {
            color: gray;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            color: white;
        }
        QRadioButton::indicator {
            border: 2px solid gray;
        }
        QRadioButton::indicator:checked {
            background-color: red;
        }
        QCheckBox::indicator {
            border: 2px solid gray;
        }
        QCheckBox::indicator:checked {
            background-color: red;
        }""")

        self.verticalLayout = QtWidgets.QVBoxLayout(NitroSense)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fan_control_tab = QtWidgets.QTabWidget(parent=NitroSense)
        self._apply_size_policy(self.fan_control_tab, QtWidgets.QSizePolicy.Policy.Maximum,
                               QtWidgets.QSizePolicy.Policy.Maximum)
        self.fan_control_tab.setMinimumSize(QtCore.QSize(480, 680))
        self.fan_control_tab.setMaximumSize(QtCore.QSize(480, 680))
        self.fan_control_tab.setFont(self._create_font("TT Squares", 12))
        self.fan_control_tab.setObjectName("fan_control_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, -1, 10, 10)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.status_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.status_box, QtWidgets.QSizePolicy.Policy.Maximum,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "status_box")
        self.status_box.setMaximumSize(QtCore.QSize(340, 125))
        self.formLayout_2 = QtWidgets.QFormLayout(self.status_box)
        self.formLayout_2.setContentsMargins(4, 8, 4, 4)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.powerStatusLabel = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.powerStatusLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="powerStatusLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.powerStatusLabel)
        self.powerStatusValue = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.powerStatusValue, font=self._create_font("TT Squares", 11),
                         object_name="powerStatusValue")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.powerStatusValue)
        self.batteryStatusLabel = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.batteryStatusLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="batteryStatusLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batteryStatusLabel)
        self.batteryStatusValue = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.batteryStatusValue, font=self._create_font("TT Squares", 11),
                         object_name="batteryStatusValue")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batteryStatusValue)
        self.batteryChargeLimitLabel = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.batteryChargeLimitLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="batteryChargeLimitLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batteryChargeLimitLabel)
        self.batteryChargeLimitValue = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.batteryChargeLimitValue, font=self._create_font("TT Squares", 11),
                         object_name="batteryChargeLimitValue")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batteryChargeLimitValue)
        self.nitroModeLabel = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.nitroModeLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="nitroModeLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nitroModeLabel)
        self.nitroModeValue = QtWidgets.QLabel(parent=self.status_box)
        self._setup_label(self.nitroModeValue, font=self._create_font("TT Squares", 11),
                         object_name="nitroModeValue")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nitroModeValue)
        self.horizontalLayout_3.addWidget(self.status_box)
        self.predMode = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.predMode, QtWidgets.QSizePolicy.Policy.Maximum,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "predMode")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.predMode)
        self.verticalLayout_2.setContentsMargins(4, 10, 4, 4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quietModeCB = QtWidgets.QRadioButton(parent=self.predMode)
        self._setup_radio_button(self.quietModeCB, font=self._create_font("TT Squares", 11),
                                object_name="quietModeCB")
        self.verticalLayout_2.addWidget(self.quietModeCB)
        self.defaultModeCB = QtWidgets.QRadioButton(parent=self.predMode)
        self._setup_radio_button(self.defaultModeCB, font=self._create_font("TT Squares", 11),
                                object_name="defaultModeCB", checked=True)
        self.verticalLayout_2.addWidget(self.defaultModeCB)
        self.extremeModeCB = QtWidgets.QRadioButton(parent=self.predMode)
        self._setup_radio_button(self.extremeModeCB, font=self._create_font("TT Squares", 11),
                                object_name="extremeModeCB")
        self.verticalLayout_2.addWidget(self.extremeModeCB)
        self.horizontalLayout_3.addWidget(self.predMode)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.temp_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.temp_box, QtWidgets.QSizePolicy.Policy.Minimum,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "temp_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.temp_box)
        self.gridLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cpuTempLabel = QtWidgets.QLabel(parent=self.temp_box)
        self._setup_label(self.cpuTempLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="cpuTempLabel")
        self.gridLayout_2.addWidget(self.cpuTempLabel, 0, 0, 1, 1)
        self.cpuTempValue = QtWidgets.QLabel(parent=self.temp_box)
        self._setup_label(self.cpuTempValue, font=self._create_font("TT Squares", 11),
                         object_name="cpuTempValue")
        self.gridLayout_2.addWidget(self.cpuTempValue, 0, 1, 1, 1)
        self.gpuTempLabel = QtWidgets.QLabel(parent=self.temp_box)
        self._setup_label(self.gpuTempLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="gpuTempLabel")
        self.gridLayout_2.addWidget(self.gpuTempLabel, 2, 0, 1, 1)
        self.gpuTempValue = QtWidgets.QLabel(parent=self.temp_box)
        self._setup_label(self.gpuTempValue, font=self._create_font("TT Squares", 11),
                         object_name="gpuTempValue")
        self.gridLayout_2.addWidget(self.gpuTempValue, 2, 1, 1, 1)
        self.sysTempLabel = QtWidgets.QLabel(parent=self.temp_box)
        self._setup_label(self.sysTempLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="sysTempLabel")
        self.gridLayout_2.addWidget(self.sysTempLabel, 4, 0, 1, 1)
        self.sysTempValue = QtWidgets.QLabel(parent=self.temp_box)
        self._setup_label(self.sysTempValue, font=self._create_font("TT Squares", 11),
                         object_name="sysTempValue")
        self.gridLayout_2.addWidget(self.sysTempValue, 4, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.temp_box)
        self.fan_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.fan_box, QtWidgets.QSizePolicy.Policy.Preferred,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "fan_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fan_box)
        self.gridLayout_6.setContentsMargins(-1, 10, 4, -1)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cpuFanSpeedLabel = QtWidgets.QLabel(parent=self.fan_box)
        self._setup_label(self.cpuFanSpeedLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="cpuFanSpeedLabel")
        self.gridLayout_6.addWidget(self.cpuFanSpeedLabel, 0, 0, 1, 1)
        self.cpuFanSpeedValue = QtWidgets.QLabel(parent=self.fan_box)
        self._setup_label(self.cpuFanSpeedValue, font=self._create_font("TT Squares", 11),
                         object_name="cpuFanSpeedValue")
        self.gridLayout_6.addWidget(self.cpuFanSpeedValue, 0, 1, 1, 1)
        self.gpuFanSpeedLabel = QtWidgets.QLabel(parent=self.fan_box)
        self._setup_label(self.gpuFanSpeedLabel, font=self._create_font("TT Squares", 11, bold=True),
                         object_name="gpuFanSpeedLabel")
        self.gridLayout_6.addWidget(self.gpuFanSpeedLabel, 2, 0, 1, 1)
        self.gpuFanSpeedValue = QtWidgets.QLabel(parent=self.fan_box)
        self._setup_label(self.gpuFanSpeedValue, font=self._create_font("TT Squares", 11),
                         object_name="gpuFanSpeedValue")
        self.gridLayout_6.addWidget(self.gpuFanSpeedValue, 2, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.fan_box)
        self.KB_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.KB_box, QtWidgets.QSizePolicy.Policy.Preferred,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "KB_box")
        self.miscLayout = QtWidgets.QVBoxLayout(self.KB_box)
        self.miscLayout.setContentsMargins(-1, 10, -1, -1)
        self.miscLayout.setObjectName("miscLayout")
        self.KBTimerCB = QtWidgets.QCheckBox(parent=self.KB_box)
        self._setup_checkbox(self.KBTimerCB, font=self._create_font("TT Squares", 11),
                            object_name="KBTimerCB")
        self.miscLayout.addWidget(self.KBTimerCB)
        self.usbChargingCB = QtWidgets.QCheckBox(parent=self.KB_box)
        self._setup_checkbox(self.usbChargingCB, font=self._create_font("TT Squares", 11),
                            object_name="usbChargingCB")
        self.miscLayout.addWidget(self.usbChargingCB)
        self.chargeLimit = QtWidgets.QCheckBox(parent=self.KB_box)
        self._setup_checkbox(self.chargeLimit, font=self._create_font("TT Squares", 11),
                            object_name="chargeLimit", checked=True)
        self.miscLayout.addWidget(self.chargeLimit)
        self.horizontalLayout_7.addWidget(self.KB_box)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.undervolt_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.undervolt_box, QtWidgets.QSizePolicy.Policy.Preferred,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "undervolt_box")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.undervolt_box)
        self.gridLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.voltageLabel = QtWidgets.QLabel(parent=self.undervolt_box)
        self._setup_label(self.voltageLabel, font=self._create_font("TT Squares", 11),
                         object_name="voltageLabel")
        self.gridLayout_5.addWidget(self.voltageLabel, 0, 0, 1, 1)
        self.voltageValue = QtWidgets.QLabel(parent=self.undervolt_box)
        self._setup_label(self.voltageValue, font=self._create_font("TT Squares", 11),
                         object_name="voltageValue")
        self.gridLayout_5.addWidget(self.voltageValue, 0, 1, 1, 1)
        self.voltageMinMaxLabel = QtWidgets.QLabel(parent=self.undervolt_box)
        self._setup_label(self.voltageMinMaxLabel, font=self._create_font("TT Squares", 11),
                         object_name="voltageMinMaxLabel")
        self.gridLayout_5.addWidget(self.voltageMinMaxLabel, 0, 2, 1, 1)
        self.voltageMinMaxValue = QtWidgets.QLabel(parent=self.undervolt_box)
        self._setup_label(self.voltageMinMaxValue, font=self._create_font("TT Squares", 11),
                         object_name="voltageMinMaxValue")
        self.gridLayout_5.addWidget(self.voltageMinMaxValue, 0, 3, 1, 1)
        self.undervoltStatus = QtWidgets.QTextBrowser(parent=self.undervolt_box)
        self.undervoltStatus.setFont(self._create_font("TT Squares", 8))
        self.undervoltStatus.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.undervoltStatus.setObjectName("undervoltStatus")
        self.gridLayout_5.addWidget(self.undervoltStatus, 4, 0, 1, 4)
        self.verticalLayout_7.addWidget(self.undervolt_box)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cpu_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.cpu_box, QtWidgets.QSizePolicy.Policy.Preferred,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "cpu_box")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.cpu_box)
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cpu_auto = QtWidgets.QRadioButton(parent=self.cpu_box)
        self._setup_radio_button(self.cpu_auto, font=self._create_font("TT Squares", 11),
                                object_name="cpu_auto", checked=True)
        self.verticalLayout_4.addWidget(self.cpu_auto)
        self.cpu_manual = QtWidgets.QRadioButton(parent=self.cpu_box)
        self._setup_radio_button(self.cpu_manual, font=self._create_font("TT Squares", 11),
                                object_name="cpu_manual")
        self.verticalLayout_4.addWidget(self.cpu_manual)
        self.cpu_turbo = QtWidgets.QRadioButton(parent=self.cpu_box)
        self._setup_radio_button(self.cpu_turbo, font=self._create_font("TT Squares", 11),
                                object_name="cpu_turbo")
        self.verticalLayout_4.addWidget(self.cpu_turbo)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.cpuManualSlider = QtWidgets.QSlider(parent=self.cpu_box)
        self._setup_slider(self.cpuManualSlider, font=self._create_font("TT Squares", 11),
                          object_name="cpuManualSlider", maximum=20, value=20,
                          vertical=True, enabled=False)
        self.horizontalLayout_4.addWidget(self.cpuManualSlider)
        self.horizontalLayout_2.addWidget(self.cpu_box)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.undervolt_dropdown = QtWidgets.QComboBox(parent=self.tab)
        self._setup_combobox(self.undervolt_dropdown, QtWidgets.QSizePolicy.Policy.Preferred,
                            QtWidgets.QSizePolicy.Policy.Maximum,
                            self._create_font("TT Squares", 11),
                            object_name="undervolt_dropdown", max_size=(200, 30))
        self.undervolt_dropdown.addItem("0mV")
        self.undervolt_dropdown.addItem("-100mV")
        self.undervolt_dropdown.addItem("-200mV")
        self.undervolt_dropdown.addItem("-300mV")
        self.undervolt_dropdown.addItem("-400mV")
        self.undervolt_dropdown.addItem("-500mV")
        self.undervolt_dropdown.addItem("-600mV")
        self.undervolt_dropdown.addItem("-700mV")
        self.verticalLayout_6.addWidget(self.undervolt_dropdown)
        self.undervolt_button = QtWidgets.QPushButton(parent=self.tab)
        self._setup_pushbutton(self.undervolt_button, QtWidgets.QSizePolicy.Policy.Preferred,
                              QtWidgets.QSizePolicy.Policy.Maximum,
                              self._create_font("TT Squares", 11),
                              object_name="undervolt_button", max_size=(200, 30))
        self.verticalLayout_6.addWidget(self.undervolt_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.global_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.global_box, QtWidgets.QSizePolicy.Policy.Preferred,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "global_box")
        self.globalLayout = QtWidgets.QVBoxLayout(self.global_box)
        self.globalLayout.setContentsMargins(-1, 10, -1, -1)
        self.globalLayout.setSpacing(2)
        self.globalLayout.setObjectName("globalLayout")
        self.global_auto = QtWidgets.QRadioButton(parent=self.global_box)
        self._setup_radio_button(self.global_auto, font=self._create_font("TT Squares", 11),
                                object_name="global_auto", checked=True)
        self.globalLayout.addWidget(self.global_auto)
        self.global_turbo = QtWidgets.QRadioButton(parent=self.global_box)
        self._setup_radio_button(self.global_turbo, font=self._create_font("TT Squares", 11),
                                object_name="global_turbo")
        self.globalLayout.addWidget(self.global_turbo)
        self.verticalLayout_3.addWidget(self.global_box)
        self.exit_button = QtWidgets.QPushButton(parent=self.tab)
        self._apply_size_policy(self.exit_button, QtWidgets.QSizePolicy.Policy.Preferred,
                               QtWidgets.QSizePolicy.Policy.Maximum)
        self.exit_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.exit_button.setFont(self._create_font("TT Squares", 11))
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_3.addWidget(self.exit_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gpu_box = QtWidgets.QGroupBox(parent=self.tab)
        self._setup_group_box(self.gpu_box, QtWidgets.QSizePolicy.Policy.Preferred,
                             QtWidgets.QSizePolicy.Policy.Preferred,
                             self._create_font("TT Squares", 11, bold=True), "gpu_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.gpu_box)
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gpu_auto = QtWidgets.QRadioButton(parent=self.gpu_box)
        self._setup_radio_button(self.gpu_auto, font=self._create_font("TT Squares", 11),
                                object_name="gpu_auto", checked=True)
        self.verticalLayout_5.addWidget(self.gpu_auto)
        self.gpu_manual = QtWidgets.QRadioButton(parent=self.gpu_box)
        self._setup_radio_button(self.gpu_manual, font=self._create_font("TT Squares", 11),
                                object_name="gpu_manual")
        self.verticalLayout_5.addWidget(self.gpu_manual)
        self.gpu_turbo = QtWidgets.QRadioButton(parent=self.gpu_box)
        self._setup_radio_button(self.gpu_turbo, font=self._create_font("TT Squares", 11),
                                object_name="gpu_turbo")
        self.verticalLayout_5.addWidget(self.gpu_turbo)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.gpuManualSlider = QtWidgets.QSlider(parent=self.gpu_box)
        self._setup_slider(self.gpuManualSlider, font=self._create_font("TT Squares", 11),
                          object_name="gpuManualSlider", maximum=20, value=20,
                          vertical=True, enabled=False)
        self.horizontalLayout_5.addWidget(self.gpuManualSlider)
        self.horizontalLayout_2.addWidget(self.gpu_box)
        spacer_item = QtWidgets.QSpacerItem(0, 266, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Maximum)
        self.horizontalLayout_2.addItem(spacer_item)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.fan_control_tab.addTab(self.tab, "")
        self.keyboard_tab = QtWidgets.QWidget()
        self.keyboard_tab.setObjectName("keyboard_tab")
        self.keyboard_tab.setMinimumSize(QtCore.QSize(480, 680))
        self.keyboard_tab.setMaximumSize(QtCore.QSize(480, 680))
        self.keyboard_box = QtWidgets.QGroupBox(parent=self.keyboard_tab)
        self.keyboard_box.setGeometry(QtCore.QRect(4, 4, 461, 631))
        self.keyboard_box.setFont(self._create_font("TT Squares", 12, bold=True))
        self.keyboard_box.setObjectName("keyboard_box")
        self.keyboardBoxLayout = QtWidgets.QVBoxLayout(self.keyboard_box)
        self.keyboardBoxLayout.setObjectName("keyboardBoxLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                         QtCore.Qt.AlignmentFlag.AlignLeft |
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setContentsMargins(8, 8, 8, -1)
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.mode_label = QtWidgets.QLabel(parent=self.keyboard_box)
        self.mode_label.setFont(self._create_font("TT Squares", 12))
        self.mode_label.setObjectName("mode_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.mode_label)
        self.mode_combo = QtWidgets.QComboBox(parent=self.keyboard_box)
        self.mode_combo.setFont(self._create_font("TT Squares", 12))
        self.mode_combo.setObjectName("mode_combo")
        self.mode_combo.addItem("Static")
        self.mode_combo.addItem("Breath")
        self.mode_combo.addItem("Neon")
        self.mode_combo.addItem("Wave")
        self.mode_combo.addItem("Shifting")
        self.mode_combo.addItem("Zoom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mode_combo)
        self.zone_label = QtWidgets.QLabel(parent=self.keyboard_box)
        self.zone_label.setFont(self._create_font("TT Squares", 12))
        self.zone_label.setObjectName("zone_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.zone_label)
        self.zone_combo = QtWidgets.QComboBox(parent=self.keyboard_box)
        self.zone_combo.setFont(self._create_font("TT Squares", 12))
        self.zone_combo.setObjectName("zone_combo")
        self.zone_combo.addItem("all")
        self.zone_combo.addItem("1")
        self.zone_combo.addItem("2")
        self.zone_combo.addItem("3")
        self.zone_combo.addItem("4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.zone_combo)
        self.speed_label = QtWidgets.QLabel(parent=self.keyboard_box)
        self.speed_label.setFont(self._create_font("TT Squares", 12))
        self.speed_label.setObjectName("speed_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.speed_label)
        self.speed_spin = QtWidgets.QSlider(parent=self.keyboard_box)
        self.speed_spin.setFont(self._create_font("TT Squares", 12))
        self.speed_spin.setMaximum(9)
        self.speed_spin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.speed_spin.setTickInterval(1)
        self.speed_spin.setObjectName("speed_spin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.speed_spin)
        self.brightness_label = QtWidgets.QLabel(parent=self.keyboard_box)
        self.brightness_label.setFont(self._create_font("TT Squares", 12))
        self.brightness_label.setObjectName("brightness_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.brightness_label)
        self.brightness_spin = QtWidgets.QSlider(parent=self.keyboard_box)
        self.brightness_spin.setFont(self._create_font("TT Squares", 12))
        self.brightness_spin.setMaximum(100)
        self.brightness_spin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.brightness_spin.setTickInterval(1)
        self.brightness_spin.setObjectName("brightness_spin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.brightness_spin)
        self.direction_label = QtWidgets.QLabel(parent=self.keyboard_box)
        self.direction_label.setFont(self._create_font("TT Squares", 12))
        self.direction_label.setObjectName("direction_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.direction_label)
        self.direction_combo = QtWidgets.QComboBox(parent=self.keyboard_box)
        self.direction_combo.setFont(self._create_font("TT Squares", 12))
        self.direction_combo.setObjectName("direction_combo")
        self.direction_combo.addItem("Left to right")
        self.direction_combo.addItem("Right to left")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.direction_combo)
        self.color_button = QtWidgets.QPushButton(parent=self.keyboard_box)
        self.color_button.setFont(self._create_font("TT Squares", 12))
        self.color_button.setObjectName("color_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.color_button)
        self.verticalLayout_8.addLayout(self.formLayout)
        self.apply_button = QtWidgets.QPushButton(parent=self.keyboard_box)
        self.apply_button.setFont(self._create_font("TT Squares", 12))
        self.apply_button.setObjectName("apply_button")
        self.verticalLayout_8.addWidget(self.apply_button)
        self.save_button = QtWidgets.QPushButton(parent=self.keyboard_box)
        self.save_button.setFont(self._create_font("TT Squares", 12))
        self.save_button.setObjectName("save_button")
        self.verticalLayout_8.addWidget(self.save_button)
        self.load_button = QtWidgets.QPushButton(parent=self.keyboard_box)
        self.load_button.setFont(self._create_font("TT Squares", 12))
        self.load_button.setObjectName("load_button")
        self.verticalLayout_8.addWidget(self.load_button)
        self.keyboardBoxLayout.addLayout(self.verticalLayout_8)
        self.fan_control_tab.addTab(self.keyboard_tab, "")
        self.verticalLayout.addWidget(self.fan_control_tab)
        self.retranslateUi(NitroSense)
        self.fan_control_tab.setCurrentIndex(0)   # 0 = Home
        QtCore.QMetaObject.connectSlotsByName(NitroSense)

    def retranslateUi(self, NitroSense):
        _translate = QtCore.QCoreApplication.translate
        NitroSense.setWindowTitle(_translate("NitroSense", "Nitro Sense™"))
        self.status_box.setTitle(_translate("NitroSense", "Status"))
        self.powerStatusLabel.setText(_translate("NitroSense", "Power Status:"))
        self.powerStatusValue.setText(_translate("NitroSense", "0"))
        self.batteryStatusLabel.setText(_translate("NitroSense", "Battery Status:"))
        self.batteryStatusValue.setText(_translate("NitroSense", "Battery Not In Use"))
        self.batteryChargeLimitLabel.setText(_translate("NitroSense", "Charge Limit:"))
        self.batteryChargeLimitValue.setText(_translate("NitroSense", "Off"))
        self.nitroModeLabel.setText(_translate("NitroSense", "Nitro Mode:"))
        self.nitroModeValue.setText(_translate("NitroSense", "Default"))
        self.predMode.setTitle(_translate("NitroSense", "Mode"))
        self.quietModeCB.setText(_translate("NitroSense", "Quiet"))
        self.defaultModeCB.setText(_translate("NitroSense", "Default"))
        self.extremeModeCB.setText(_translate("NitroSense", "Extreme"))
        self.temp_box.setTitle(_translate("NitroSense", "Temps"))
        self.cpuTempLabel.setText(_translate("NitroSense", "CPU:"))
        self.cpuTempValue.setText(_translate("NitroSense", "100°"))
        self.gpuTempLabel.setText(_translate("NitroSense", "GPU:"))
        self.gpuTempValue.setText(_translate("NitroSense", "100°"))
        self.sysTempLabel.setText(_translate("NitroSense", "SYS:"))
        self.sysTempValue.setText(_translate("NitroSense", "100°"))
        self.fan_box.setTitle(_translate("NitroSense", "Fan RPM"))
        self.cpuFanSpeedLabel.setText(_translate("NitroSense", "CPU:"))
        self.cpuFanSpeedValue.setText(_translate("NitroSense", "5660 RPM"))
        self.gpuFanSpeedLabel.setText(_translate("NitroSense", "GPU:"))
        self.gpuFanSpeedValue.setText(_translate("NitroSense", "5660 RPM"))
        self.KB_box.setTitle(_translate("NitroSense", "Misc"))
        self.KBTimerCB.setText(_translate("NitroSense", "KB Timeout"))
        self.usbChargingCB.setText(_translate("NitroSense", "USB Charging"))
        self.chargeLimit.setText(_translate("NitroSense", "Charge Limit"))
        self.undervolt_box.setTitle(_translate("NitroSense", "Undervolt"))
        self.voltageLabel.setText(_translate("NitroSense", "Voltage:"))
        self.voltageValue.setText(_translate("NitroSense", "0.00"))
        self.voltageMinMaxLabel.setText(_translate("NitroSense", "Min / Max:"))
        self.voltageMinMaxValue.setText(_translate("NitroSense", "0.00"))
        self.cpu_box.setTitle(_translate("NitroSense", "CPU Fan"))
        self.cpu_auto.setText(_translate("NitroSense", "Auto"))
        self.cpu_manual.setText(_translate("NitroSense", "Manual"))
        self.cpu_turbo.setText(_translate("NitroSense", "Max speed"))
        self.undervolt_dropdown.setItemText(0, _translate("NitroSense", "0mV"))
        self.undervolt_dropdown.setItemText(1, _translate("NitroSense", "-100mV"))
        self.undervolt_dropdown.setItemText(2, _translate("NitroSense", "-200mV"))
        self.undervolt_dropdown.setItemText(3, _translate("NitroSense", "-300mV"))
        self.undervolt_dropdown.setItemText(4, _translate("NitroSense", "-400mV"))
        self.undervolt_dropdown.setItemText(5, _translate("NitroSense", "-500mV"))
        self.undervolt_dropdown.setItemText(6, _translate("NitroSense", "-600mV"))
        self.undervolt_dropdown.setItemText(7, _translate("NitroSense", "-700mV"))
        self.undervolt_button.setText(_translate("NitroSense", "Undervolt"))
        self.global_box.setTitle(_translate("NitroSense", "Global"))
        self.global_auto.setText(_translate("NitroSense", "Auto"))
        self.global_turbo.setText(_translate("NitroSense", "Turbo"))
        self.exit_button.setText(_translate("NitroSense", "Exit"))
        self.gpu_box.setTitle(_translate("NitroSense", "GPU Fan"))
        self.gpu_auto.setText(_translate("NitroSense", "Auto"))
        self.gpu_manual.setText(_translate("NitroSense", "Manual"))
        self.gpu_turbo.setText(_translate("NitroSense", "Max speed"))
        self.fan_control_tab.setTabText(self.fan_control_tab.indexOf(self.tab),
                                       _translate("NitroSense", "Home"))
        self.keyboard_box.setTitle(_translate("NitroSense", "Keyboard"))
        self.mode_label.setText(_translate("NitroSense", "Mode:"))
        self.mode_combo.setItemText(0, _translate("NitroSense", "Static"))
        self.mode_combo.setItemText(1, _translate("NitroSense", "Breath"))
        self.mode_combo.setItemText(2, _translate("NitroSense", "Neon"))
        self.mode_combo.setItemText(3, _translate("NitroSense", "Wave"))
        self.mode_combo.setItemText(4, _translate("NitroSense", "Shifting"))
        self.mode_combo.setItemText(5, _translate("NitroSense", "Zoom"))
        self.zone_label.setText(_translate("NitroSense", "Zone:"))
        self.zone_combo.setItemText(0, _translate("NitroSense", "all"))
        self.zone_combo.setItemText(1, _translate("NitroSense", "1"))
        self.zone_combo.setItemText(2, _translate("NitroSense", "2"))
        self.zone_combo.setItemText(3, _translate("NitroSense", "3"))
        self.zone_combo.setItemText(4, _translate("NitroSense", "4"))
        self.speed_label.setText(_translate("NitroSense", "Speed:"))
        self.brightness_label.setText(_translate("NitroSense", "Brightness:"))
        self.direction_label.setText(_translate("NitroSense", "Direction:"))
        self.direction_combo.setItemText(0, _translate("NitroSense", "Left to right"))
        self.direction_combo.setItemText(1, _translate("NitroSense", "Right to left"))
        self.color_button.setText(_translate("NitroSense", "Select Color"))
        self.apply_button.setText(_translate("NitroSense", "Apply"))
        self.save_button.setText(_translate("NitroSense", "Save"))
        self.load_button.setText(_translate("NitroSense", "Load"))
        self.fan_control_tab.setTabText(self.fan_control_tab.indexOf(self.keyboard_tab),
                                       _translate("NitroSense", "Keyboard"))