import os
import shutil

def organize_directory(path):
    if not os.path.isdir(path):
        print(f"Error: The path '{path}' is not a valid directory.")
        return
    
    FILE_TYPES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
        'Scripts': ['.py', '.js', '.html', '.css', '.sh', '.bat'],
    }

    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f != os.path.basename(__file__)]
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return

    print(f"Scanning {len(files)} files in '{path}'...")

    for file in files:
        file_path = os.path.join(path, file)
        file_extension = os.path.splitext(file)[1].lower()

        moved = False
        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                target_folder_path = os.path.join(path, folder_name)
                
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path)
                    print(f"Created folder: {target_folder_path}")
                
                shutil.move(file_path, os.path.join(target_folder_path, file))
                print(f"  -> Moved '{file}' to '{folder_name}'")
                moved = True
                break
        
        if not moved:
            other_folder_path = os.path.join(path, 'Other')
            if not os.path.exists(other_folder_path):
                os.makedirs(other_folder_path)
                print(f"Created folder: {other_folder_path}")
            
            shutil.move(file_path, os.path.join(other_folder_path, file))
            print(f"  -> Moved '{file}' to 'Other'")

    print("\nFile organization complete!")

if __name__ == "__main__":
    target_directory = " "

    organize_directory(target_directory)
