# 3D-Airdraw-Authentication (Leap Motion Controller 2)
This project epitomizes innovation - transforming biometric security into an intuitive 3D experience using LeapMotion Controller 2. AirSecureX sets a new standard for gesture-based authentication.

AirSecureX: Revolutionizing Authentication with 3D Airdraw Technology

This project demonstrates an innovative approach to securing a simple to-do list application using gesture-based authentication. By leveraging the Ultraleap Controller 2 and a trained autoencoder model, the app only unlocks if a registered 3D hand gesture is successfully recognized.
The system uses Python, TensorFlow, OpenCV, and the Leap Motion API with a machine learning pipeline to capture, train, and verify gesture data in real-time.

1. Software and Library Requirements
Before you begin, make sure you have Python version 3.10 installed.
The required libraries are specified in the requirements.txt file. These include:

After creating a virtual environment, install them using:

'''pip install -r requirements.txt'''

Then, install the LeapC bindings as follows:

1.	Run: '''python -m build leapc-cffi
2.	Then install the generated package: '''pip install leapc-cffi/dist/leapc_cffi-0.0.1.tar.gz'''
3.	Finally, install the LeapC Python API in editable mode: '''pip install -e leapc-python-api'''

Setup Instructions
To get started:

1.	Save all the project files into a single folder.
2.	Open the folder in VSCode (or any other Python-compatible IDE).
3.	Install Python 3.10 if not already installed. It is recommended to use this version for compatibility.
4.	Create a new virtual environment inside the folder.
5.	Activate the virtual environment and install the required libraries using the pip install -r requirements.txt command.
6.	Install the LeapC library as mentioned above.

3. Files Included
   
This project includes three program files:
•	One Python script:
todo_app.py – a basic to-do list application that will be gesture-locked.
•	Two Jupyter Notebooks:
o	register_gesture_app.ipynb – used to capture and train gestures.
o	gesture_app_unlock.ipynb – used to unlock the to-do app based on gesture authentication.

4. Use Case Overview
   
The goal of the project is to lock and unlock a to-do application using a unique hand gesture captured using the Ultraleap sensor. Gesture recognition is done through an autoencoder model that learns and later matches hand gestures based on 3D point cloud frames.

5. Using the Application
   
Step 1: Connect the Ultraleap Sensor
Make sure the Ultraleap Controller 2 is connected and the Ultraleap Hand Tracking Software is running on your system. If you don’t have one, you can purchase it from the official store:
👉 [Buy Ultraleap Controller 2](https://www.thingbits.in/products/leap-motion-controller-2?srsltid=AfmBOooWR9FXHcBO0A3su1bvs7DX_IA2OtwrSN07yvt-YEesMCrmKjI8)

Step 2: Registering a Gesture

To register your password gesture:
1.	Run the register_gesture_app.ipynb Jupyter notebook.
2.	If prompted, install the ipykernel package.
3.	When you run the notebook, you will be asked to begin registering your gesture.
4.	The Ultraleap visualizer window will pop up (check the taskbar if it's not visible).
5.	Show your hand above the sensor — you will see a 3D visualization of your hand.
6.	The program is set to capture 30 frames per gesture by default. You can change this by editing the required_frames parameter in the __init__() method of the GestureCapture class.
7.	Capture your gesture by pressing s. Press x to stop capturing.
8.	It's recommended to capture at least 15–20 gestures or more for better accuracy.
9.	The captured gestures will be saved to the gestures/ folder.
10.	After capturing, the autoencoder model will start training automatically.
11.	Wait for the training to complete. The trained model will be saved in the model/ folder.
12.	A file named threshold.pkl will also be created, storing the matching threshold for authentication.

Step 3: Unlocking the To-Do App with Gesture

To use gesture-based unlocking:
1.	Run the gesture_app_unlock.ipynb notebook.
2.	This will start monitoring whether the to-do app has launched or not.
3.	Now, run the todo_app.py file. When it launches, it will prompt you to enter your gesture-based password.
4.	The Ultraleap visualizer will open again.
5.	Show your hand gesture as before — the captured gesture will be saved in the auth_gesture/ folder.
6.	If the newly captured gesture matches the previously trained gesture, the app will be unlocked.
7.	If it does not match, access will be denied.

6. Final Notes
   
•	Ensure consistent hand placement and gesture positioning when capturing and authenticating gestures.
•	If the visualizer does not appear, check if it is minimized or hidden in the taskbar.
•	You can experiment by modifying the frame capture count, training thresholds, or even customizing gesture definitions.
