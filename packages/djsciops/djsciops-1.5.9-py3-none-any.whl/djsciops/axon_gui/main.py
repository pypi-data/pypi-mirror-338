# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

from multiprocessing import freeze_support
import sys
import os
import platform
import traceback
import logging
import yaml
from datetime import datetime
from pathlib import Path, PurePosixPath

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from djsciops import __version__ as axon_version
from djsciops import axon as djsciops_axon
from djsciops import authentication as djsciops_authentication
from djsciops import settings as djsciops_settings
from djsciops.log import log, log_format
import djsciops

from djsciops.axon_gui.modules import *
from djsciops.axon_gui.widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
basedir = os.path.dirname(__file__)

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.signals.error.connect(self.log_exception)

    def log_exception(self, exc):
        if log.getEffectiveLevel() == 10:
            log.debug(f"Uncaught exception: {exc[2]}")
        else:
            log.error(f"Uncaught exception: {exc[1]}")

    @Slot()
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # DEFINE LOG HANDLER
        # ///////////////////////////////////////////////////////////////
        class Main(QObject):
            log = Signal(str)

        class GuiLogHandler(logging.Handler):
            def __init__(self, emitter):
                super().__init__()
                self._emitter = emitter
                self.widget = widgets.upload_status
                self._emitter.log.connect(self.widget.append)
                # self.widget.verticalScrollBar().setValue(
                #     self.widget.verticalScrollBar().maximum()
                # )
                # self.widget.ensureCursorVisible()

            @property
            def emitter(self):
                return self._emitter

            def emit(self, record):
                msg = self.format(record)
                self.emitter.log.emit(msg)

        gui_handler = GuiLogHandler(Main())
        gui_handler.setFormatter(
            logging.Formatter("[%(asctime)s][%(levelname)s]: %(message)s", "%H:%M:%S")
        )
        log.addHandler(gui_handler)

        # SET VERSION
        # ///////////////////////////////////////////////////////////////
        widgets.version.setText(f"v{axon_version}")

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        # APPLY TEXTS
        self.setWindowTitle("Axon")
        widgets.titleRightInfo.setText("Axon Upload")

        # Session Token
        # ///////////////////////////////////////////////////////////////
        self.session = None

        # TOGGLE BUTTONS
        # ///////////////////////////////////////////////////////////////
        # tab expansion
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # config menu
        widgets.toggleLeftBox.clicked.connect(
            lambda: UIFunctions.toggleLeftBox(self, True)
        )
        widgets.extraCloseColumnBtn.clicked.connect(
            lambda: UIFunctions.toggleLeftBox(self, True)
        )
        # switch theme
        widgets.themeSwitchBtn.clicked.connect(lambda: self.switch_themes())
        # console
        widgets.toggleConsoleBtn.clicked.connect(
            lambda: UIFunctions.toggleConsole(self)
        )

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # SET CONFIG
        # ///////////////////////////////////////////////////////////////
        self.config = djsciops_settings.get_config(stdin_enabled=False)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        widgets.btn_upload.clicked.connect(self.buttonClick)
        widgets.btn_bucket.clicked.connect(self.buttonClick)
        widgets.btn_browse_dir.clicked.connect(self.buttonClick)
        widgets.btn_upload_files.clicked.connect(self.buttonClick)
        widgets.btn_save_config.clicked.connect(self.buttonClick)
        widgets.refreshTokenBtn.clicked.connect(self.generate_auth_token)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET THREADPOOL
        # ///////////////////////////////////////////////////////////////
        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        self.theme = "dark"  # Default theme

        # SET THEME AND HACKS
        if useCustomTheme:
            widgets.themeSwitchBtn.setVisible(True)
            # LOAD AND APPLY STYLE
            UIFunctions.theme(
                self,
                os.path.join(basedir, "themes", f"py_dracula_{self.theme}.qss"),
                True,
            )

            # SET HACKS
            AppFunctions.setThemeHack(self)
        else:
            widgets.themeSwitchBtn.setVisible(False)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.pageUpload)
        widgets.btn_upload.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_upload.styleSheet())
        )

        # FETCH CONFIG
        # ///////////////////////////////////////////////////////////////
        widgets.aws_acc_id.setText(self.config["aws"]["account_id"])
        widgets.s3_role.setText(self.config["s3"]["role"])
        widgets.s3_bucket.setText(self.config["s3"]["bucket"])
        widgets.dj_acc_client_id.setText(self.config["djauth"]["client_id"])

        # LOAD DIR TREE
        # ///////////////////////////////////////////////////////////////
        widgets.browse_s3_dir.returnPressed.connect(self.load_bucket_dir)
        widgets.btn_refresh_browser.clicked.connect(self.load_bucket_dir)
        widgets.s3_dir.returnPressed.connect(self.load_bucket_preview)
        widgets.btn_refresh_preview.clicked.connect(self.load_bucket_preview)
        widgets.local_dir_tree.itemClicked.connect(self.load_bucket_preview)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW UPLOAD PAGE
        if btnName == "btn_upload":
            widgets.titleRightInfo.setText("Axon Upload")
            widgets.stackedWidget.setCurrentWidget(widgets.pageUpload)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW BROWSE BUCKET PAGE
        elif btnName == "btn_bucket":
            widgets.titleRightInfo.setText("S3 Bucket Browser")
            widgets.stackedWidget.setCurrentWidget(widgets.pageS3Browse)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # BROWSE LOCAL DIRECTORIES
        elif btnName == "btn_browse_dir":
            widgets.local_dir.setText(
                str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            )
            if widgets.local_dir.text():
                UIFunctions.refresh_tree(
                    widgets.local_dir_tree, widgets.local_dir.text(), "path"
                )
                if widgets.s3_dir.text():
                    self.load_bucket_preview()
            else:
                widgets.local_dir_tree.clear()
                widgets.s3_bucket_dir.clear()

        # UPLOAD FILES
        elif btnName == "btn_upload_files":
            if not widgets.local_dir.text() or not widgets.s3_dir.text():
                log.warning("Select a source and destination to begin uploading")
            elif (
                not widgets.aws_acc_id.text()
                or not widgets.dj_acc_client_id.text()
                or not widgets.s3_role.text()
                or not widgets.s3_bucket.text()
            ):
                log.warning("Set up your djsciops config to begin uploading")
            elif self.check_auth_token():
                widgets.btn_upload_files.setEnabled(False)
                checked_items, dest = self.map_checked_items(widgets.local_dir_tree)

                worker = Worker(
                    djsciops_axon.upload_files,
                    session=self.session,
                    s3_bucket=self.config["s3"]["bucket"],
                    source=checked_items,
                    destination=dest,
                    boto3_config=self.config["boto3"],
                )
                worker.signals.result.connect(self.upload_result)
                worker.signals.finished.connect(self.upload_finished)
                self.threadpool.start(worker)

        # SAVE CONFIG
        elif btnName == "btn_save_config":
            self.config["aws"]["account_id"] = widgets.aws_acc_id.text()
            self.config["djauth"]["client_id"] = widgets.dj_acc_client_id.text()
            self.config["s3"]["role"] = widgets.s3_role.text()
            self.config["s3"]["bucket"] = widgets.s3_bucket.text()
            config_directory = djsciops_settings.appdirs.user_data_dir(
                appauthor="datajoint", appname="djsciops"
            )
            djsciops_settings.save_config(yaml.dump(self.config), config_directory)
            log.info("Config has been saved")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # WORKER SIGNAL FUNCTIONS
    # ///////////////////////////////////////////////////////////////
    def upload_finished(self):
        widgets.btn_upload_files.setEnabled(True)

    def upload_result(self, r):
        log.info("Upload complete")

    def auth_finished(self):
        widgets.refreshTokenBtn.setEnabled(True)

    def auth_result(self, s):
        self.session = s
        time = datetime.fromtimestamp(self.session.jwt["exp"]).strftime("%H:%M %p")
        widgets.expTime.setText(f"Token Expiration Time: {time}")

    # UTIL FUNCTIONS
    # ///////////////////////////////////////////////////////////////
    def generate_auth_token(self):
        widgets.refreshTokenBtn.setEnabled(False)
        worker = Worker(
            djsciops_authentication.Session,
            aws_account_id=self.config["aws"]["account_id"],
            s3_role=self.config["s3"]["role"],
            auth_client_id=self.config["djauth"]["client_id"],
            auth_client_secret=self.config["djauth"].get("client_secret", None),
        )
        worker.signals.result.connect(self.auth_result)
        worker.signals.finished.connect(self.auth_finished)
        self.threadpool.start(worker)

    def load_bucket_dir(self):
        if self.check_auth_token():
            UIFunctions.update_bucket_tree(self)

    def load_bucket_preview(self):
        if widgets.local_dir.text() and widgets.s3_dir.text():
            UIFunctions.update_bucket_preview(self)

    def map_checked_items(self, tree):
        items = []
        dest = []
        widgets.local_dir.setText(
            widgets.local_dir.text() + "/"
            if widgets.local_dir.text()[-1] != "/"
            else widgets.local_dir.text()
        )
        widgets.s3_dir.setText(
            widgets.s3_dir.text() + "/"
            if widgets.s3_dir.text()[-1] != "/"
            else widgets.s3_dir.text()
        )
        iterator = QTreeWidgetItemIterator(tree, QTreeWidgetItemIterator.Checked)
        while iterator.value():
            item = iterator.value()
            if os.path.isfile(item.text(1)):
                items.append(Path(item.text(1)))
                dest.append(
                    PurePosixPath(
                        item.text(1).replace(
                            widgets.local_dir.text(), widgets.s3_dir.text()
                        )
                    )
                )
            iterator += 1
        return items, dest

    def switch_themes(self):
        if self.theme == "light":
            self.theme = "dark"
            # LOAD AND APPLY STYLE
            UIFunctions.theme(
                self,
                os.path.join(basedir, "themes", f"py_dracula_{self.theme}.qss"),
                True,
            )
            widgets.themeSwitchBtn.setIcon(QIcon(":/icons/images/icons/cil-sun.png"))

        elif self.theme == "dark":
            self.theme = "light"
            # LOAD AND APPLY STYLE
            UIFunctions.theme(
                self,
                os.path.join(basedir, "themes", f"py_dracula_{self.theme}.qss"),
                True,
            )

            widgets.themeSwitchBtn.setIcon(QIcon(":/icons/images/icons/cil-moon.png"))

    def check_auth_token(self):
        if not self.session:
            log.warning("Generate a new authentication token to begin using Axon")
            return False
        else:
            time_to_live = (
                (self.session.jwt["exp"] - datetime.now().timestamp()) / 60 / 60
            )
            if time_to_live <= 0:
                log.warning(
                    "Authentication token has expired. Please generate a new token"
                )
                return False
            else:
                log.info(
                    f"Using valid authentication token with a life of {'{:.2f}'.format(time_to_live)} [HR]"
                )
                return True

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")


if __name__ == "__main__":
    freeze_support()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, "icon.ico")))
    window = MainWindow()
    sys.exit(app.exec())
