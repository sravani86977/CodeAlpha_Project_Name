import shutil

# Function to organize files in a directory
def organize_files(directory):
    # Create directories if they don't exist
    categories = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Others': []  # Any other file types will go here
    }

    for category in categories:
        os.makedirs(os.path.join(directory, category), exist_ok=True)

    # Traverse through files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False

            # Move file to respective category directory
            for category, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(
                        os.path.join(directory, filename),
                        os.path.join(directory, category, filename)
                    )
                    moved = True
                    break
            
            # If file doesn't match any category, move to 'Others'
            if not moved:
                shutil.move(
                    os.path.join(directory, filename),
                    os.path.join(directory, 'Others', filename)
                )

    print("File organization completed.")

# Main function to execute the script
def main():
    directory = input("Enter the directory path to organize files: ")
    organize_files(directory)

if __name__ == "__main__":
    # your code here
    main()