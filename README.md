# HandGesture Volume Control

This project is a gesture-controlled volume application written in Python. It allows users to control the system volume using hand gestures captured by a webcam.

## Requirements

To run the application, you need to have the following installed:

- Python 3 (version 3.6 or later)
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- Tkinter (usually included with Python installations)
- PIL (`pip install pillow`)

## Prerequisites

Before running the application, ensure that you have a webcam connected to your computer. The application uses the webcam to capture hand gestures.

## How to Run the Application

To run the application, follow these steps:

1. Clone or download the project to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

### Running the main.py file

1. Run the following command to start the application:
   `python main.py`
   This will open a GUI window with a "Run File" button.
2. Click the "Run File" button to start the gesture-controlled volume application. The webcam feed will be displayed, and you can control the volume by following these instructions:

- Place your hand in front of the webcam, ensuring that your thumb and forefinger are extended.
- Move your thumb and forefinger closer together to decrease the volume.
- Move your thumb and forefinger farther apart to increase the volume.
- The volume level will be displayed on the volume bar and as a percentage on the volume label.

### Exiting the Application

To exit the application, simply close the GUI window or press Ctrl + C in the terminal or command prompt where the application is running.

## Additional Notes

- The application is designed to work on macOS due to the usage of the osascript command to set the system volume. If you are running the application on a different operating system, you may need to modify the set_system_volume() function in the Volcontrol.py file to set the volume using the appropriate system commands.
- The application assumes the existence of a background image file (bg.jpg) in a folder named "Assets" in the same directory as the Python files. If you want to use a different background image, replace the existing bg.jpg file with your desired image, ensuring it has the same name and is placed in the "Assets" folder.
