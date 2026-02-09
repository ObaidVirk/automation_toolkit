import os
import shutil

DOWNLOADS = os.path.expanduser("~/Downloads")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Applications": [".exe"]
}


def organize_downloads():
    if not os.path.exists(DOWNLOADS):
        print("Downloads folder not found")
        return

    for filename in os.listdir(DOWNLOADS):
        file_path = os.path.join(DOWNLOADS, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    folder_path = os.path.join(DOWNLOADS, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, filename))
                    break

    print("Downloads organized successfully!")
