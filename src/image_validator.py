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
        unsupported_images = []

        for file in os.listdir(self.address):
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(self.address, file)
                self.images[image_path] = self.get_image_size(image_path , delete_empty=delete_empty)
                if self.images[image_path] != self.image_size:

                    count_mismatched += 1
                    unsupported_images.append(image_path)

                if self.images[image_path] == (0, 0):
                    print(f"Image {image_path} is empty")
                    if delete_empty == True:
                        os.remove(image_path)

                    
        return count_mismatched  , unsupported_images

    def check_single_files(self):
        count_single = 0
        single_files = []

        for file in os.listdir(self.address):
            if file.endswith(('.jpg', '.jpeg', '.png')):
                file_name,extension = os.path.splitext(file)
                xml_path = os.path.join(self.address,file_name + ".xml")
                if os.path.isfile(xml_path):
                    continue
                else:
                    print(f"{file_name} have no xml file")
                    count_single += 1
                    single_files.append(file_name)

        print(f"we have {count_single} image that have no xml file\n\n")
        return count_single , single_files

    
    def get_image_size(self, image_path,delete_empty = False):
        image = cv2.imread(image_path)

        if image is None:
            if delete_empty == True:
                os.remove(image_path)
            raise ValueError(f"Cannot read image: {image_path}")


        return image.shape[:2]

    def image_validation(self, delete_empty=False, output_file=None):

        count_mismatched, unsupported_images = self.check_image_size(
            delete_empty=delete_empty
        )

        count_single, single_files = self.check_single_files()

        with open(output_file, "a") as f:
            f.write(f"Image validation started for {self.address}\n")

            f.write(
                f"We have {count_mismatched} images "
                f"that have unsupported sizes\n"
            )

            for image_path in unsupported_images:
                f.write(f"Unsupported image: {image_path}\n")

            f.write(
                f"We have {count_single} images without XML files\n"
            )

            for file_name in single_files:
                f.write(f"Image without XML: {file_name}.\n")

            f.write("\n")
            f.close()