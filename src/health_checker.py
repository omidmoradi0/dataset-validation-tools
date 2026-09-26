import os
import json

from src.image_validator import ImageValidator
from src.xml_validator import XmlValidator

class HealthChecker:
    def __init__(self, input_folder, output_file , image_size=()):
        self.input_folder = input_folder
        self.output_file = output_file
        self.image_size = image_size
        self.split_folders()

    def split_folders(self):
        print("----------> start spliting folders")
        # Implement the logic to split folders here
        self.train_folder = os.path.join(self.input_folder, "train")
        self.val_folder = os.path.join(self.input_folder, "validation")
        self.test_folder = os.path.join(self.input_folder, "test")

    def check_folders(self):
        print("----------> start checking")
        folder_paths = [self.train_folder, self.val_folder, self.test_folder]
        results = {}

        for folder_path in folder_paths:
            print(f"checking {folder_path}")
            if os.path.exists(folder_path):
                image_validator = ImageValidator(self.image_size,folder_path)
                xml_validator = XmlValidator(folder_path)

                image_validator.image_validation()
                xml_validator.xml_validation()
            else:
                print(f"Folder {folder_path} does not exist.")
                results[folder_path] = None

        return results

    