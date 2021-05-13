# cowinSlotTracker
This is a simple application that will automatically check slots for you for vaccination on the Cowin portal. Feel free to take the code.

The dev folder contains the code for the application.

The folder CowinSlotTracker contains the executable.

The application currently pings the servers every half an hour. If you wish to change this interval in the code, update the interval parameter for QtCore.QTimer().

_**Note**_: As per the updates published by API Setu, the responses will be cached and can be as old as half an hour. Also as per the guidelines please limit your calls to 100 per 5 minutes (keeping in mind that each iteration triggers four API calls).

The GUI was made using QT designer along with PySide6 for the code interface.

Anybody who wishes to run the python script needs to install the following dependencies:
1. PySide6
2. requests

The code was frozen and executable generated using cxfreeze.

The compiled program is currently available only for Windows. Working on getting a MacOS version out. In the meantime you can run the python script after installing all dependencies on any platform.

In case you face any issues while running the app or updating it to suit your preferences, please feel free to reach out.

Hope you all find vaccine slots at the earliest.

Stay safe.
