# This Python file uses the following encoding: utf-8
import sys
import requests
import ui_form
from datetime import date, timedelta, datetime
from PySide6 import QtWidgets, QtCore, QtGui

states_dict = {}
district_dict = {}


class CowinSlots(QtWidgets.QWidget):
    dialog = None

    def __init__(self):
        super(CowinSlots, self).__init__()
        self.window = ui_form.Ui_CowinSlots()
        self.window.setupUi(self)
        self.populate_states()
        self.initialize_signals()
        self.window.slotsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.window.runButton.setEnabled(True)
        self.window.districtSelect.setEnabled(True)
        self.window.stateSelect.setEnabled(True)
        self.window.stopButton.setEnabled(False)
        self.timer = QtCore.QTimer(self, interval=5 * 60 * 1000, timeout=self.check_slots)
        icon = QtGui.QIcon("images/icon.png")
        self.tray_icon = QtWidgets.QSystemTrayIcon(icon)
        self.tray_icon.setIcon(icon)
        self.tray_icon.setVisible(True)

        self.menu = QtWidgets.QMenu()

        self.quit_action = QtGui.QAction("Quit")
        self.quit_action.triggered.connect(app.quit)
        self.menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.menu)

    def initialize_signals(self):
        self.window.stateSelect.currentIndexChanged.connect(self.state_selected)
        self.window.runButton.clicked.connect(self.run_check)
        self.window.stopButton.clicked.connect(self.stop_check)

    # def load_ui(self):
    #     """
    #     Function to be used in case somebody wants to work directly with the UI file.
    #     :return: void
    #     """
    #     loader = QUiLoader()
    #     path = os.fspath(Path(__file__).resolve().parent / "form.ui")
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()

    def populate_states(self):
        response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states',
                                headers={
                                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()
        for state in response['states']:
            states_dict[state['state_name']] = state['state_id']
            self.window.stateSelect.addItem(state['state_name'])

    def state_selected(self):
        if self.window.stateSelect.currentIndex() != 0:
            self.populate_districts()
        else:
            self.window.districtSelect.clear()
            district_dict.clear()
            self.window.districtSelect.addItem('Select District')

    def populate_districts(self):
        self.window.districtSelect.clear()
        district_dict.clear()
        self.window.districtSelect.addItem('Select District')
        state = states_dict[self.window.stateSelect.currentText()]
        response = requests.get(f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state}',
                                headers={
                                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()
        for district in response['districts']:
            district_dict[district['district_name']] = district['district_id']
            self.window.districtSelect.addItem(district['district_name'])

    def run_check(self):
        if self.window.stateSelect.currentIndex() != 0 and self.window.districtSelect.currentIndex() != 0:
            QtCore.QTimer.singleShot(0, self.check_slots)
            self.timer.start()
            self.window.runButton.setEnabled(False)
            self.window.districtSelect.setEnabled(False)
            self.window.stateSelect.setEnabled(False)
            self.window.stopButton.setEnabled(True)
            self.window.runningStatus.setText('Application is running..')
        else:
            self.window.runningStatus.setText('Please select state and district!')

    def stop_check(self):
        self.timer.stop()
        self.window.runButton.setEnabled(True)
        self.window.districtSelect.setEnabled(True)
        self.window.stateSelect.setEnabled(True)
        self.window.stopButton.setEnabled(False)
        self.window.runningStatus.setText('Currently Not Running!')

    def check_slots(self):
        self.window.slotsTable.clearContents()
        self.window.slotsTable.setRowCount(0)
        dates = [date.today(), date.today() + timedelta(7), date.today() + timedelta(14), date.today() + timedelta(28)]
        district = district_dict[self.window.districtSelect.currentText()]
        centre_found = False
        time_of_check = datetime.now()
        for current_date in dates:
            response = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
                                    f'?district_id={district}&date={current_date.strftime("%d-%m-%Y")}',
                                    headers={
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()
            centers = response['centers']
            for center in centers:
                center_sessions = center['sessions']
                for session in center_sessions:
                    if session['min_age_limit'] != 45 and session["available_capacity"] > 0:
                        row = self.window.slotsTable.rowCount()
                        self.window.slotsTable.insertRow(row)
                        self.window.slotsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(session["date"]))
                        self.window.slotsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(session["vaccine"]))
                        self.window.slotsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(center["name"]))
                        self.window.slotsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(center["address"]))
                        self.window.slotsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(center["block_name"]))
                        self.window.slotsTable.setItem(row, 5,
                                                       QtWidgets.QTableWidgetItem(str(session["available_capacity"])))
                        centre_found = True

        if not centre_found:
            self.window.label.setText(f'Slots not found!! Last checked at {time_of_check}')
            palette = self.window.label.palette()
            palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.WindowText, QtGui.QColor('red'))
            self.window.label.setPalette(palette)
        else:
            self.window.label.setText(f'Slots found!! Last checked at {time_of_check}')
            palette = self.window.label.palette()
            palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.WindowText, QtGui.QColor('green'))
            self.window.label.setPalette(palette)
            # self.dialog = QtWidgets.QMessageBox()
            # self.dialog.setIcon(QtWidgets.QMessageBox.Information)
            # self.dialog.setText('Vaccine Slots Found!! Please check the app for more details.')
            # self.dialog.setWindowTitle('Vaccine Slots Found')
            # self.dialog.show()
            # self.dialog.activateWindow()

            self.tray_icon.showMessage('Vaccine Slots Found',
                                  'Vaccine Slots Found!! Please check the app for more details.',
                                  QtWidgets.QSystemTrayIcon.Information, 1000)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = CowinSlots()
    widget.show()
    sys.exit(app.exec_())
