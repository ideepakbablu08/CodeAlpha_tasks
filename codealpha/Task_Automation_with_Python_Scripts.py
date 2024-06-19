import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("500x300")
        self.directory = None
        self.original_files = {}
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Select a directory to organize:", font=("Helvetica", 16), fg='black', bg='red')
        self.label.pack(pady=20)

        self.select_button = tk.Button(self.root, text="Select Directory", command=self.select_directory, font=("Helvetica", 14), bg='black', fg='white', width=20)
        self.select_button.pack(pady=10)

        self.organize_button = tk.Button(self.root, text="Organize Files", command=self.organize_files, state=tk.DISABLED, font=("Helvetica", 14), bg='black', fg='white', width=20)
        self.organize_button.pack(pady=10)

        self.undo_button = tk.Button(self.root, text="Undo", command=self.undo_organization, state=tk.DISABLED, font=("Helvetica", 14), bg='black', fg='white', width=20)
        self.undo_button.pack(pady=10)

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.organize_button.config(state=tk.NORMAL)
            messagebox.showinfo("Directory Selected", f"Selected directory: {self.directory}")

    def organize_files(self):
        if not hasattr(self, 'directory'):
            messagebox.showerror("Error", "Please select a directory first.")
            return

        self.original_files = {}
        file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Music': ['.mp3', '.wav', '.aac', '.flac'],
            'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
            'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
        }

        for folder in file_types.keys():
            os.makedirs(os.path.join(self.directory, folder), exist_ok=True)

        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                self.original_files[filename] = file_path
                file_ext = os.path.splitext(filename)[1].lower()
                moved = False
                for folder, extensions in file_types.items():
                    if file_ext in extensions:
                        shutil.move(file_path, os.path.join(self.directory, folder, filename))
                        moved = True
                        break
                if not moved:
                    other_folder = os.path.join(self.directory, 'Others')
                    os.makedirs(other_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(other_folder, filename))

        self.undo_button.config(state=tk.NORMAL)
        messagebox.showinfo("Success", "Files organized successfully!")

    def undo_organization(self):
        for filename, original_path in self.original_files.items():
            current_path = self.find_file(self.directory, filename)
            if current_path:
                shutil.move(current_path, original_path)

        self.undo_button.config(state=tk.DISABLED)
        messagebox.showinfo("Undo", "Organization undone successfully!")

    def find_file(self, directory, filename):
        for root, dirs, files in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='yellow')
    app = FileOrganizerApp(root)
    root.mainloop()
