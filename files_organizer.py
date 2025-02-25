import os
import shutil


def organize_downloads(download_folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt', '.md'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.tar.gz']
    }
    for file in os.listdir(download_folder):
        if os.path.isfile(os.path.join(download_folder, file)):
            file_ext = os.path.splitext(file)[1].lower()
            destination_folder = next((ftype for ftype, exts in file_types.items() if file_ext in exts), 'Others')

            os.makedirs(os.path.join(download_folder, destination_folder), exist_ok=True)
            shutil.move(os.path.join(download_folder, file), os.path.join(download_folder, destination_folder, file))
    print(os.path.basename(download_folder) + " organized!")


if __name__ == "__main__":
    downloads_path = 'C:\\Users\\imran.bhatti\\Desktop'  
    organize_downloads(downloads_path)