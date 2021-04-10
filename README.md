# Introduction

Speed Typing Test is an application which calculates a person's typing speed (in words per minute) and also displays the accuracy of typing. This program lets you know about your speed of typing. 

The application also uses a database to store names and speeds, due to which it even displays a user's leaderboard rank with respect to his/her speed.

This project has been built using Python programming and the GUI has been created using 'tkinter' library.

## Modules and Tech Stack Used

The project is built using Python Programming. The modules used are as follows :
* **Tkinter** for GUI
* **timeit** for timer
* **PIL (pillow)** for loading images and gradients
* **random** for generating random numbers
* **sqlite3** for database connection

### Main Files (Project Structure)

 ```sh
  ├── README.md
  ├── Typing_Speed_Test.py *** the main driver of the GUI app
                    "python Typing_Speed_Test.py" to run after installing dependences
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── leaderboard.db *** contains the database table

  *** rest all files are images and icons for design and graphics ***
  ```

### Development Setup
  ```
  $ cd ~
  $ sudo pip3 install requirements.txt
  $ python Typing_Speed_Test.py
  ```