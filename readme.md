# AD-Blocker Raspberry-Pi Documentation #

This is the documentation of the UserInferface for following Ad-blocker:

https://github.com/magnus-nagarro/Ad-blocker-Raspberry

Please be sure to configure the Ad-blocker first!

## Installation Instructions ##

! This script has only been tested and developed on Windows. Smooth functioning on other systems cannot be guaranteed !

### 1. Clone Repository ###

Please clone this repository to a folder of your choic.

```cmd
cd path/to/your/floder
git clone https://github.com/magnus-nagarro/Ad-blocker-Raspberry-Ui.git
```

### 2. Install dependencies ###

To ensure smooth operation, the following packages must be installed manually if they have not already been installed.

```cmd
cd path/to/your/floder/Ad-blocker-Raspberry-Ui
pip install customtkinter
pip install Pillow 
pip install requests
```

Now you can check if the UserInterface is running. Please note that only the welcomepage.py script needs to be executed to start the user interface, all other scripts do not need to be started:

```cmd
 path/to/your/pythonexe/python.exe path/to/your/folder/Ad-blocker-Raspberry-Ui/welcomepage.py
```
If the WelcomePage is visible, installation was successful. Else please check the Error message.

## Using the User Interface ##

Now, when the UserInterface is running correctly, you can Start using the UserInterface.

### WelcomePage ###

After the first start, or if the IP address of the device with the blocker has changed, you will first see the welcome page. On this page, please enter the IP address of the device on which the blocker is running. 

The script automatically checks whether the entered Ip is correct. 
If this is the case, the user interface starts automatically.
If this is not the case, you will see an error message, please check whether the entered Ip address is correct and whether the corresponding device is switched on, has a network connection and the Docker containers are running. 

### UserInterface ###

Now, when the user interface is started, you can see several frames. 

On the left side you can see the MenueBar. It is static and contains informations about the Windwos Device resources and includes buttons to start/stop the blocker. At the bottom of the MenueBar you can see the navigation of the UI. You can also change the default Themecolor here.

At the bottom of the UI, you can the StatusBar. It shows you the current status of the Blockersoftware.

### 1. MainFrame ###

On the right side there's the MainFrame, including Import/Export of links and a table with all current blocked links, by default. To add links, type it into the textfield and select "Add". If the link has been imported correctly, this is confirmed by the green confirmation. If an error has occurred, this will also be displayed here. If the link you entered already exists, this will also be displayed.

You can export the links here too. A text file with all links will be created and opend so you can device where you want to save it.

There's currently no fuction to import links via textfiles!

On the TableFrame you can search current blocked links. Also there's the opportunity tho delete some of these links. To delete links, select the row and press the delete button. The link is now deleted from the database.


### 2. SettingsFrame ###

If you click the Settingsbutton in the MenueBar the SettingsFrame appears. 

Here you can change the scaling factor of the window, the current theme-color and the Ip address, if that of the blocker device has changed.

### 3. AboutFrame ###

If you click the Aboutbutton in the MenueBar the AboutFrame appears.

Here you can get some informations of our project. 

## Start Blocker ##

Now that you know how the Ui is structured, you can start using the blocker. Please press the Start button. The StatusBar should be green now. Else it's red and shows an error message of the error, which occured while the starting process.