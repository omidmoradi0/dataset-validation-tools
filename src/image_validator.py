import os
import cv2


class ImageValidator:
    def __init__(self,image_size,address):
        self.image_size = image_size
        self.images = {}
        self.address = address

    def check_image_size(self , delete_empty = False):
        print("---> start checking image size : ")
        count_mismatched = 0

        for file in os.listdir(self.address):
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(self.address, file)
                self.images[image_path] = self.get_image_size(image_path)
                if self.images[image_path] != self.image_size:
                    
                    count_mismatched += 1

                if self.images[image_path] == (0, 0):
                    print(f"Image {image_path} is empty")
                    if delete_empty == True:
                        os.remove(image_path)
                    
        return count_mismatched 

    def check_single_files(self):
        count_single = 0

        for file in os.listdir(self.address):
            if file.endswith(('.jpg', '.jpeg', '.png')):
                file_name,extension = os.path.splitext(file)
                xml_path = os.path.join(self.address,file_name + ".xml")
                if os.path.isfile(xml_path):
                    continue
                else:
                    print(f"{file_name} have no xml file")
                    count_single += 1

        print(f"we have {count_single} file that have no image or xml file\n\n")

    
    def get_image_size(self, image_path):
        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(f"Cannot read image: {image_path}")

        return image.shape[:2]

    def image_validation(self,delete_empty = False):
        self.check_image_size(delete_empty=delete_empty)
        self.check_single_files()