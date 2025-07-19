File Organizer 📂
A simple yet powerful Python script to automatically organize files in a directory based on their type. This tool scans a specified folder and moves files into categorized subdirectories (e.g., Images, Documents, Videos), helping you keep your directories clean and tidy.

✨ Features
Automatic Categorization: Sorts files into predefined categories like Images, Documents, Videos, Audio, Archives, and more.

Smart Folder Creation: Automatically creates the necessary category folders if they don't already exist.

'Other' Category: Any file type that doesn't match a known category is moved to an Other folder, ensuring every file is organized.

Safe to Re-run: The script can be run multiple times on the same directory without causing errors.

Easy to Customize: Add new file types and categories by simply editing the FILE_TYPES dictionary in the script.

Cross-Platform: Works on Windows, macOS, and Linux.

🚀 Getting Started
These instructions will get you a copy of the project up and running on your local machine.

Prerequisites
Python 3: This script requires Python 3 to be installed on your system. You can download it from python.org.

Installation & Usage
Clone the repository (or download the script):

git clone [https://github.com/your-username/file-organizer.git](https://github.com/your-username/file-organizer.git)
cd file-organizer

Alternatively, you can just download the organizer.py script directly.

Configure the Target Directory:
Open the organizer.py file in your favorite text editor and find the following lines at the bottom of the script:

# ⚠️ IMPORTANT: Change this path to the directory you want to organize.
# For example: "C:/Users/YourUsername/Downloads" or "/home/yourusername/Documents"
target_directory = "C:/Path/To/Your/Messy/Folder" 

Change the value of target_directory to the absolute path of the folder you want to organize.

Run the Script:
Open a terminal or command prompt, navigate to the project directory, and execute the script:

python organizer.py

The script will then scan the files, create the necessary folders, and move the files accordingly, printing its progress in the terminal.

🔧 Customization
You can easily teach the script about new file types.

Open organizer.py.

Find the FILE_TYPES dictionary near the top of the file.

Add or edit the categories and file extensions as needed.

For example, to add a category for 3D model files, you could add a new line like this:

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt'],
    # ... other categories
    '3D Models': ['.obj', '.fbx', '.stl', '.blend'], # <-- New category
}

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

📄 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
