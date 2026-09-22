"""
this class is subclass for agmenting the util function to use in health_checker.py




"""


import os , cv2


class folderManager:
    def __init__(self,image_size,address):
        self.image_size = image_size
        self.address = address
        self.images = {}

    def check_image_size(self , delete_empty = False):
        print("---> start checking file size : ")
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

            elif file.endswith('.xml'):
                xml_path = os.path.join(self.address, file)
                if os.path.getsize(xml_path) == 0:
                    print(f"xml {xml_path} is empty")
                    if delete_empty == True:
                        os.remove(xml_path)
                    
        return count_mismatched 

    def check_single_files(self):

        count_single = 0

        for file in os.listdir(self.address):
            if file.endswith(('.jpg', '.jpeg', '.png' , '.xml')):
                file_name = file.split('.')
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    if os.path.isfile(file_name[0] + ".xml") == True:
                        continue
                    else:
                        print(f"image {file_name} have no xml file")
                        count_single += 1
                if file.endswith(('.xml')):
                    if os.path.isfile(file_name[0] + ".jpg") == True or os.path.isfile(file_name[0] + ".jpeg") == True or os.path.isfile(file_name[0] + ".png") == True :
                        continue
                    else:
                        print(f"xml {file_name} have no image file")
                        count_single += 1

        print(f"we have {count_single} file that have no image or xml file")

    
    def get_image_size(self,image_path):
        image = cv2.imread(image_path)
        image_size = image.shape[:2]
        return image_size
