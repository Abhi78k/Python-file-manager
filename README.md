# 📂 Download Folder Organizer (File Sorter by Type)

This Python script helps you **organize your download folder** by automatically moving files into categorized subfolders based on their file extensions. It's useful for keeping your workspace neat and sorted.

## ✅ What It Does

- Scans your **Downloads** folder
- Detects file types like:

  - `.pdf` → **PDF Files**
  - `.txt` → **Notepad/Text Files**
  - `.jpg`, `.png`, `.mp4`, etc. → **Media/Image Files**
- Moves them to respective folders:

  - `pdf files/`
  - `notepad files/`
  - `media or image files/`
- Creates these folders if they don't exist

## 🗂️ File Types Handled

- **PDF files:** `.pdf`
- **Text files:** `.txt`
- **Media files:** `.jpg`, `.jpeg`, `.PNG`, `.png`, `.mp4`, `.ico`

## 🛠️ Requirements

- Python 3.x
- Windows OS (currently uses Windows-specific file paths)

## 📦 Folder Structure (After Sorting)

```
Downloads/
├── pdf files/
│   └── example.pdf
├── notepad files/
│   └── notes.txt
├── media or image files/
│   ├── image.png
│   └── video.mp4
```

## 📌 How to Use

1. Make sure Python is installed.
2. Update the paths in the script to match your actual folder locations.
3. Run the script:

```bash
python pythonfilemanager.py
```

Your files will be moved automatically to their appropriate folders.

## 🧠 Logic Highlights

- Uses `glob` to list all files in the Downloads directory
- Uses `os.path.splitext()` to get file extensions
- Uses `shutil.move()` to transfer files
- Creates target folders dynamically using `os.mkdir()` if needed

## 🛡️ Safety Tips

- Test on a sample folder first if you have important files
- Script **moves** files (does not copy), so ensure backups if necessary

## 💡 Improvements You Can Add

- Logging of moved files
- Handling other file types like `.zip`, `.docx`, etc.
- Allow user input for folder paths
- Cross-platform support (Linux, macOS)

## 📝 License

Free to use and modify for personal or professional use.
