# file_organizer
# Organize Downloads Script

A Python script to automatically organize files in your given folder based on their file extensions.

## Features
✅ Categorizes files into subfolders (Images, Documents, Videos, etc.)
✅ Moves files automatically based on their extension
✅ Creates missing folders if they don’t exist
✅ Keeps your downloads folder clean & organized

## Installation
1. **Clone the repository** (or download the script manually):
   ```sh
   git clone https://github.com/yourusername/organize-downloads.git
   cd organize-downloads
   ```
2. **Install required dependencies** (Python 3 required):
   ```sh
   pip install -r requirements.txt  # No extra dependencies needed for this script
   ```

## Usage
1. **Modify the `download_folder` path in the script** to match your actual downloads directory:
   ```python
   download_folder = "C:/Users/YourName/Downloads"  # Change this to your folder path
   ```
2. **Run the script**:
   ```sh
   python organize_downloads.py
   ```

## Example Output
### **Before Running**
```
Downloads/
  ├── image1.jpg
  ├── video.mp4
  ├── report.pdf
  ├── notes.txt
```

### **After Running**
```
Downloads/
  ├── Images/
  │   ├── image1.jpg
  ├── Videos/
  │   ├── video.mp4
  ├── Documents/
  │   ├── report.pdf
  │   ├── notes.txt
```

## Customization
- Modify the `file_types` dictionary in the script to define your own categories.
  ```python
  file_types = {
      "Images": [".jpg", ".png", ".gif"],
      "Documents": [".pdf", ".docx", ".txt"],
      "Videos": [".mp4", ".mov"]
  }
  ```

## Contributing
Feel free to submit issues or pull requests to improve the script!

## License


