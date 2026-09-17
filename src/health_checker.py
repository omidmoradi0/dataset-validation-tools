import os
from src.folder_manager import folderManager

class healthChecker:
    def __init__(self, input_folder, output_file , image_size=()):
        self.input_folder = input_folder
        self.output_file = output_file
        self.image_size = image_size
        self.split_folders()

    def split_folders(self):
        # Implement the logic to split folders here
        self.train_folder = os.path.join(self.input_folder, "train")
        self.val_folder = os.path.join(self.input_folder, "val")
        self.test_folder = os.path.join(self.input_folder, "test")

    def check_folders(self):
        folder_paths = [self.train_folder, self.val_folder, self.test_folder]
        results = {}

        for folder_path in folder_paths:
            if os.path.exists(folder_path):
                fm = folderManager(self.image_size, folder_path)
                count_mismatched = fm.check_image_size()
                results[folder_path] = count_mismatched
            else:
                print(f"Folder {folder_path} does not exist.")
                results[folder_path] = None

        return results

    