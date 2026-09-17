

import os , cv2


class folderManager:
    def __init__(self,image_size,address):
        self.image_size = image_size
        self.address = address
        self.images = {}

    def check_image_size(self):
        for file in os.listdir(self.address):
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(self.address, file)
                print(image_path)
                self.images[image_path] = self.get_image_size(image_path)

        count_mismatched = 0

        for image_path in self.images:
            if self.images[image_path] != self.image_size:
                print(f"Image {image_path} does not match the specified size {self.image_size}.")
                count_mismatched += 1
        return count_mismatched
    
    def get_image_size(self,image_path):
        image = cv2.imread(image_path)
        image_size = image.shape[:2]
        return image_size