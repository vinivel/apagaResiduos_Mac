# Delete Files with `._` Prefix Using Tkinter
This Python program scans a selected folder (and its subfolders) for files with names starting with `._` and provides an interface for the user to delete them. The program uses **Tkinter** to create a graphical user interface (GUI).
## Features
- Select a folder and recursively search for files starting with `._`.
- Display the found files in a selectable list.
- Delete specific files selected by the user.
- Delete all found files at once.
- Informative labels to display the number of files located.

## Requirements
- Python 3.6+
- Libraries:
    - `tkinter` (pre-installed with Python)
    - `os` (standard library)

## How to Use
1. Clone this repository or download the script.
2. Run the script:
``` bash
   python script_name.py
```
1. The application provides the following functionality:
    - **Select a folder**: Click the "Select Folder" button and choose a directory.
    - **Search for files**: The program will find and display all files starting with `._`.
    - **Delete specific files**: Select files from the list and click "Delete Selected".
    - **Delete all files**: Click "Delete All" to remove all found files with one action.

## Interface Summary
- **Folder Selection**: Choose a folder for the scan.
- **File Display List**: Shows all `._` files found in the selected folder and its subfolders.
- **Actions**:
    - Delete specific files selected.
    - Delete all found files.

## Warning
Deleting files is **irreversible**. Use this program carefully, as files are permanently deleted from your system.
## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
