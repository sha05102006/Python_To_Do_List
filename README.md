# Intern Details:

* Intern ID: CITS1691
* Full Name: Shashath.B.S
* No.Of Weeks: 4 Weeks

# WriteUp - To Do List Application

## Introduction:

The scope of this project is to provide a simple and user-friendly desktop application for managing daily tasks and improving productivity. This project is developed using *Python* and the *Tkinter GUI library*. The application allows users to create, manage, save, and organize their tasks through an interactive graphical interface. The program helps users keep track of pending and completed tasks efficiently. The Python script attached in this repository can perform functions such as:

* Adding new tasks to a to-do list.
* Deleting selected tasks from the list.
* Marking tasks as completed by crossing them off.
* Restoring crossed-off tasks back to active status.
* Removing all completed tasks from the list.
* Saving task lists into external ".dat" files for future use.
* Opening previously saved task lists.
* Clearing the entire task list when required.
* Providing both vertical and horizontal scrolling support for easier navigation through long task lists.

This project helps users manage their personal tasks, improve organization, and maintain productivity through a simple desktop interface.

## Features:

### Task Management

* Add new tasks using the input field.
* Delete selected tasks instantly.
* Mark completed tasks by crossing them off.
* Restore completed tasks back to pending status.

### File Management

* Save task lists into ".dat" files using file dialogs.
* Open previously saved task lists.
* Automatically load stored tasks from saved files.

### User Interface

* Built using Python Tkinter.
* Easy-to-use graphical interface.
* Scrollbars for handling large numbers of tasks.
* Menu-based options for file operations and task handling.

## Modules Used:

### Os

Used for easy access operating system dependent functionality

https://docs.python.org/3/library/os.html

### Tkinter

Used for creating the graphical user interface.

https://docs.python.org/3/library/tkinter.html

### Pickle

Used for saving and loading task data from files.

https://docs.python.org/3/library/pickle.html

### File Dialog

Used for selecting files and save locations through graphical dialogs.

https://docs.python.org/3/library/dialog.html

### Tkinter Font

Used for customizing the appearance of text in the application.

https://docs.python.org/3/library/tkinter.font.html

## Output (Video):

https://github.com/user-attachments/assets/f24da4a1-3ebe-4a60-b2d5-fb6662342c9c

## Output (Images):

### Main Application Window:

<img width="619" height="660" alt="Screenshot 2026-06-25 214723" src="https://github.com/user-attachments/assets/aa9d7a7f-1d2a-4f08-8617-d99e3699942e" />

### Adding Tasks:

<img width="621" height="660" alt="Screenshot 2026-06-25 214807" src="https://github.com/user-attachments/assets/b22b4513-88a6-4481-9334-4078dadde0ae" />

### Saving Task List:

<img width="625" height="659" alt="Screenshot 2026-06-25 214828" src="https://github.com/user-attachments/assets/842c7dbe-931e-424d-8620-517b2627acea" />

### Opening Saved Task List:

<img width="618" height="660" alt="Screenshot 2026-06-25 214858" src="https://github.com/user-attachments/assets/ab0a6404-ac72-4c75-8023-1b9599f57ad3" />

## Issues:

* The application does not automatically save tasks when closing the program.
* Crossed-off tasks are permanently removed when saving the list.
* No task priority system is available.
* No due date or reminder functionality.
* Error handling for empty task entries is limited.
* Application icon path is hardcoded and may not work on different systems without modification.
